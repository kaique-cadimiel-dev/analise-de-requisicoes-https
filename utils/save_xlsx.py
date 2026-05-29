import pandas as pd

diretorio = "./relatorios"

def save_to_xlsx(
    data,
    filename,
    campos_head=None,
    diretorio=diretorio,
    columns=["Domínios", "Ocorrências"]
):
    caminho_arquivo = f"{diretorio}/{filename}"
    df = pd.DataFrame(data, columns=columns)

    if campos_head:
        head_df = pd.DataFrame(
            [["Matéria", campos_head[0]],
             ["Data de leitura dos logs", campos_head[1]],
             ["Quantidade de logs", campos_head[2]]],
            columns=["Informação", "Valor"]
        )

        with pd.ExcelWriter(caminho_arquivo) as writer:
            head_df.to_excel(writer, index=False, sheet_name="Relatório")
            df.to_excel(writer, index=False, sheet_name="Relatório", startrow=len(head_df) + 3)
    else:
        df.to_excel(caminho_arquivo, index=False)

    print(f"Relatório salvo com sucesso em {diretorio}/{filename}\n")
