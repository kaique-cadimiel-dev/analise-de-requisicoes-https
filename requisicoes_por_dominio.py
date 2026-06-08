from utils.leitura_de_arquivo import ler_arquivo
from utils.montar_head import montar_head
from utils.save_xlsx import save_to_xlsx
from simple_term_menu import TerminalMenu
from utils.escolher_arquivos import escolher_arquivos
import re
import tabulate


pattern = r"https:\/\/([^\/]+)\/"

def obter_destino(entrie):
    destino = next((atributo["value"] for atributo in entrie["request"]["headers"] if atributo["name"] == "sec-fetch-dest"), "desconecido")
    return destino

def registra_requisicoes_por_dominio(entries, palavra_chave):
    requests = list()

    for entrie in entries:
        dominio = re.search(pattern, entrie["request"]["url"])
        if palavra_chave in dominio.group(0):
            destino = obter_destino(entrie)
            request = [
                dominio.group(0),
                entrie["request"]["method"],
                destino,
                entrie["request"]["url"]
            ]
            requests.append(request)
    
    return requests

def listar_requisicoes_por_dominio(requests):
    header = ["Domínio", "Método HTTP", "Destino", "URL"]
    table = tabulate.tabulate(requests, headers=header, tablefmt="grid")
    print(f"\nForam encontradas {len(requests)} requests")
    print(table)

def main():
    print(f"""
Analise de requisições http
          
Obtenha seu arquivo "net.har" em "https://speedvitals.com"
e adicione na raiz. Para mais instruções leia o README.md

""")
    arquivos, indice_menu_arquivo = escolher_arquivos()

    try:
        logs = ler_arquivo(arquivos[indice_menu_arquivo])
    except (FileNotFoundError, ValueError) as error:
        print(f"\nErro ao ler o arquivo: {error}\n")
        return

    head = montar_head(logs["log"]["pages"], logs["log"]["entries"])
    entries = logs["log"]["entries"]

    print("Escolha uma opcao: ")

    indice_do_menu = 0

    while indice_do_menu != 3:
        opcoes_principais = ["Listar requisicao por dominio", "Salvar em formato .xlsx", "Sair"]
        terminal_menu = TerminalMenu(opcoes_principais)
        indice_do_menu = terminal_menu.show() + 1
        if indice_do_menu == 1:
            print(head["mensagem"])
            palavra_chave = input("\nInforme a palavra chave: ")
            lista_de_requisicoes = registra_requisicoes_por_dominio(entries, palavra_chave)
            listar_requisicoes_por_dominio(lista_de_requisicoes)
            escolheu_sair = False
            while escolheu_sair == False:
                opcoes_de_filtro = ["Filtar por método HTTP", "Filtrar por destino", "Voltar"]
                terminal_menu_filtro = TerminalMenu(opcoes_de_filtro)
                indice_do_menu_filtar = terminal_menu_filtro.show()
                if indice_do_menu_filtar == 0:
                    opcoes_de_metodos = list(set([request[1] for request in lista_de_requisicoes]))
                    terminal_menu_metodos = TerminalMenu(opcoes_de_metodos)
                    indice_do_menu_metodos = terminal_menu_metodos.show()
                    print(f"Método escolhido: {opcoes_de_metodos[indice_do_menu_metodos]}\n")
                    requests = [request for request in lista_de_requisicoes if str(request[1]).lower() == str(opcoes_de_metodos[indice_do_menu_metodos]).lower()]
                    listar_requisicoes_por_dominio(requests)
                elif indice_do_menu_filtar == 1:
                    opcoes_de_destino = list(set([request[2] for request in lista_de_requisicoes]))
                    terminal_menu_destino = TerminalMenu(opcoes_de_destino)
                    indice_do_menu_destino = terminal_menu_destino.show()
                    print(f"Destino escolhido: {opcoes_de_destino[indice_do_menu_destino]}\n")
                    requests = [request for request in lista_de_requisicoes if str(request[2]).lower() == str(opcoes_de_destino[indice_do_menu_destino]).lower()]
                    listar_requisicoes_por_dominio(requests)
                elif indice_do_menu_filtar == 2:
                    escolheu_sair = True

        elif indice_do_menu == 2:
            print("Em desenvolvimento")
        elif indice_do_menu == 3:
            print("Programa encerrado com sucesso!")

if __name__ == "__main__":
    main()