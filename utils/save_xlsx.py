import pandas as pd

diretorio = "./relatorios"

def save_to_xlsx(data, filename, diretorio=diretorio, columns=["Domínios", "Ocorrências"]):
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(f"{diretorio}/{filename}", index=False, columns=columns)
    print(f"Relatório salvo com sucesso em {diretorio}/{filename}\n")