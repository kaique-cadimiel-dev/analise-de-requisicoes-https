import pandas as pd
from pathlib import Path

diretorio = "./relatorios"

def obter_caminho_disponivel(diretorio, filename):
    caminho = Path(diretorio) / filename

    if not caminho.exists():
        return caminho

    contador = 1
    while True:
        novo_caminho = caminho.with_name(f"{caminho.stem}_{contador}{caminho.suffix}")
        if not novo_caminho.exists():
            return novo_caminho
        contador += 1

def save_to_xlsx(
    data,
    filename,
    campos_head=None,
    diretorio=diretorio,
    columns=["Domínios", "Ocorrências", "Métodos HTTP"]
):
    caminho_arquivo = obter_caminho_disponivel(diretorio, filename)
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

    print(f"Relatório salvo com sucesso em {caminho_arquivo}\n")
