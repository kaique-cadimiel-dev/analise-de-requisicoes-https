from datetime import datetime

def montar_head(paginas_processadas, requisicoes):
    materia_url = paginas_processadas[0]["title"]
    data_de_leitura = paginas_processadas[0]["startedDateTime"]
    qnt_logs = len(requisicoes)

    data_logs = datetime.strptime(data_de_leitura, "%Y-%m-%dT%H:%M:%S.%fZ").date().strftime("%d/%m/%Y")

    head = f"""
    Relatorio de Análise de Logs \n
    Materia: {materia_url} \n
    Data de leitura dos logs: {data_logs} \n
    Quantidade de logs: {qnt_logs} \n
    """

    return head