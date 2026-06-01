from utils.leitura_de_arquivo import ler_arquivo
from utils.montar_head import montar_head
from utils.save_xlsx import save_to_xlsx
from simple_term_menu import TerminalMenu
from destinos_http import obter_mensagem_destino_http
import re
import tabulate

pattern = r"https:\/\/([^\/]+)\/"
separador_de_texto = "; "

def obter_ocorrencias(entries):
    ocorrencias = dict()
    for entrie in entries:
        dominio = re.search(pattern, entrie["request"]["url"])

        if not dominio:
            continue

        dominio_url = dominio.group(0)
        metodo = entrie["request"]["method"]
        destino = next((atributo["value"] for atributo in entrie["request"]["headers"] if atributo["name"] == "sec-fetch-dest"), "desconecido")

        if dominio_url not in ocorrencias:
            ocorrencias[dominio_url] = {
                "dominio": dominio_url,
                "ocorrencia": 0,
                "metodos": set(),
                "destino": set(),
                "ocorrencia_destino": dict(),
                "descricao_destino": set()
            }

        ocorrencias[dominio_url]["ocorrencia"] += 1
        ocorrencias[dominio_url]["metodos"].add(metodo)
        ocorrencias[dominio_url]["destino"].add(destino)
        ocorrencias[dominio_url]["ocorrencia_destino"][destino] = (
            ocorrencias[dominio_url]["ocorrencia_destino"].get(destino, 0) + 1
        )

    return ocorrencias

def normalizar_metodos(metodos):
    metodos_normalizados = set()
    for metodo in metodos:
        if metodo == None:
            metodos_normalizados.add("NULL")
        else:
            metodos_normalizados.add(metodo)
    return metodos_normalizados

def obter_destinos_ordenados(destinos, ordem):
    return sorted(destinos, key=lambda campo: ordem.get(campo, 999))

def ordenar_ocorrencias(ocorrencias):
    ordem = {
        "audio": 1,
        "audioworklet": 2,
        "desconecido": 3,
        "document": 4,
        "embed": 5,
        "empty": 6,
        "fencedframe": 7,
        "font": 8,
        "frame": 9,
        "iframe": 10,
        "image": 11,
        "json": 12,
        "manifest": 13,
        "object": 14,
        "paintworklet": 15,
        "report": 16,
        "script": 17,
        "serviceworker": 18,
        "sharedworker": 19,
        "style": 20,
        "track": 21,
        "video": 22,
        "webidentity": 23,
        "worker": 24,
        "xslt": 25
    }

    ocorrencias_ordenadas = sorted(
        ocorrencias.values(),
        key=lambda item: item["ocorrencia"],
        reverse=True
    )

    return [
        (
            item["dominio"],
            item["ocorrencia"],
            separador_de_texto.join(normalizar_metodos(item["metodos"])),
            separador_de_texto.join(obter_destinos_ordenados(item["destino"], ordem)),
            separador_de_texto.join(
                f"{destino}: {item['ocorrencia_destino'][destino]}"
                for destino in obter_destinos_ordenados(item["destino"], ordem)
            ),
            separador_de_texto.join(
                obter_mensagem_destino_http(destino)
                for destino in obter_destinos_ordenados(item["destino"], ordem)
            )
        )
        for item in ocorrencias_ordenadas
    ]

def listar_ocorrencias_de_dominios(ocorrencias, limite=-1):
    header = ["Domínio", "Ocorrências", "Métodos HTTP", "Destino", "Ocorrências do Destino", "Descrição do Destino"]
    table = tabulate.tabulate(ocorrencias[:limite], headers=header, tablefmt="grid")
    print(f"\nForam encontradas ocorrencias em {len(ocorrencias)} domínios")
    print(table)


def main():
    print(f"""
Analise de requisições http
          
Obtenha seu arquivo "net.har" em "https://speedvitals.com"
e adicione na raiz. Para mais instruções leia o README.md
          
Para comecar digite o nome do arquivo .har:

""")
    
    nome_do_arquivo = input("Insira o nome do arquivo .har: ")
    try:
        logs = ler_arquivo(nome_do_arquivo)
    except (FileNotFoundError, ValueError) as error:
        print(f"Erro ao ler o arquivo: {error}")
        return

    head = montar_head(logs["log"]["pages"], logs["log"]["entries"])
    entries = logs["log"]["entries"]

    print("Escolha uma opcao: ")

    indice_do_menu = 0
    limite = -1
    while indice_do_menu != 3:
        opcoes_principais = ["Analisar Requisições", "Salvar em formato .xlsx", "Sair"]
        terminal_menu = TerminalMenu(opcoes_principais)
        indice_do_menu = terminal_menu.show() + 1
        if indice_do_menu == 1:
            escolheu = False
            while escolheu == False:
                print("Gostaria de definir limite para listagem de itens?")
                options_limite_de_listagem = ["Sim", "Nao"]
                terminal_menu_limite = TerminalMenu(options_limite_de_listagem)
                indice_menu_limite = terminal_menu_limite.show()
                if indice_menu_limite == 0:
                    limite = int(input("\nQual o limite de visualização? "))
                    print(head["mensagem"])
                    ocorrencias = obter_ocorrencias(entries)
                    ocorrencias = ordenar_ocorrencias(ocorrencias)
                    listar_ocorrencias_de_dominios(ocorrencias, limite)
                    escolheu = True
                elif indice_menu_limite == 1:
                    print(head["mensagem"])
                    ocorrencias = obter_ocorrencias(entries)
                    ocorrencias = ordenar_ocorrencias(ocorrencias)
                    listar_ocorrencias_de_dominios(ocorrencias)
                    escolheu = True
        elif indice_do_menu == 2:
            print(head["mensagem"])
            ocorrencias = obter_ocorrencias(entries)
            ocorrencias = ordenar_ocorrencias(ocorrencias)
            dados_para_salvar = ocorrencias if limite == -1 else ocorrencias[:limite]
            save_to_xlsx(dados_para_salvar, "ocorrencias.xlsx", head["campos"])
        elif indice_do_menu == 3:
            print("Programa encerrado com sucesso!")

if __name__ == "__main__":
    main()
