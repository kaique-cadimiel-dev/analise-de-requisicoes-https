from utils.leitura_de_arquivo import ler_arquivo
from utils.montar_head import montar_head
from utils.save_xlsx import save_to_xlsx
from simple_term_menu import TerminalMenu

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

    while indice_do_menu != 3:
        opcoes_principais = ["Listar requisicao por dominio", "Salvar em formato .xlsx", "Sair"]
        terminal_menu = TerminalMenu(opcoes_principais)
        indice_do_menu = terminal_menu.show() + 1
        if indice_do_menu == 1:
            print(head["mensagem"])
        elif indice_do_menu == 2:
            ...
        elif indice_do_menu == 3:
            print("Programa encerrado com sucesso!")

if __name__ == "__main__":
    main()