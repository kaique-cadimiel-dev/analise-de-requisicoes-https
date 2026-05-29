from utils.leitura_de_arquivo import ler_arquivo
from utils.montar_head import montar_head
from utils.save_xlsx import save_to_xlsx
from simple_term_menu import TerminalMenu
import re
import tabulate

logs = ler_arquivo('net.har')
head = montar_head(logs["log"]["pages"], logs["log"]["entries"])

entries = logs["log"]["entries"]

pattern = r"https:\/\/([^\/]+)\/"

def obter_ocorrencias(entries):
    ocorrencias = dict()
    for entrie in entries:
        dominio = re.search(pattern, entrie["request"]["url"])
        if dominio.group(0) in ocorrencias:
            ocorrencia = {
                "dominio": dominio.group(0),
                "ocorrencia": ocorrencias[dominio.group(0)] + 1
            }
    
            ocorrencias[dominio.group(0)] = ocorrencia["ocorrencia"]
        else:
            ocorrencia = {
                "dominio": dominio.group(0),
                "ocorrencia": 1
            }
    
            ocorrencias[dominio.group(0)] = ocorrencia["ocorrencia"]
    return ocorrencias

def ordenar_ocorrencias(ocorrencias):
    return sorted(ocorrencias.items(), key=lambda item: item[1], reverse=True)

def listar_ocorrencias_de_dominios(ocorrencias, limite=-1):
    header = ["Domínio", "Ocorrências"]
    table = tabulate.tabulate(ocorrencias[:limite], headers=header, tablefmt="grid")
    print(f"\nForam encontradas ocorrencias em {len(ocorrencias)} domínios")
    print(table)


def main():
    print(f"""
Analise de requisições http
          
Obtenha seu arquivo "net.har" em "https://speedvitals.com"
e adicione na raiz. Para mais instruções leia o README.md
          
Para comecar escolha uma opcao:

""")

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
