import os
from simple_term_menu import TerminalMenu

caminho = "."

def escolher_arquivos():
    arquivos = os.listdir(caminho)
    opcoes_de_arquivos = []
    for arquivo in arquivos:
        # obtém a extensão (inclui o ponto, ex: '.har')
        extensao = os.path.splitext(arquivo)[1]
        if extensao == ".har":
            opcoes_de_arquivos.append(arquivo)

    if len(arquivos) < 1:
        print("\nSem arquivos na raiz!\n")
        return
    
    terminal_menu_arquivo = TerminalMenu(opcoes_de_arquivos)

    print("Para comecar selecione o arquivo: \n")
    indice_menu_arquivo = terminal_menu_arquivo.show()
    print(f"Arquivo selecionado: {opcoes_de_arquivos[indice_menu_arquivo]}\n")

    return opcoes_de_arquivos, indice_menu_arquivo