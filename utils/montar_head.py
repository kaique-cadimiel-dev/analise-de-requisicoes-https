from datetime import datetime

def formatar_data_logs(data_de_leitura):
    data_iso = data_de_leitura.replace("Z", "+00:00")
    return datetime.fromisoformat(data_iso).date().strftime("%d/%m/%Y")

def montar_head(paginas_processadas, requisicoes):
    materia_url = paginas_processadas[0]["title"]
    data_de_leitura = paginas_processadas[0]["startedDateTime"]
    qnt_logs = len(requisicoes)

    data_logs = formatar_data_logs(data_de_leitura)

    head = f"""
\nRelatorio de Análise de Logs \n
Materia: {materia_url} \n
Data de leitura dos logs: {data_logs} \n
Quantidade de logs: {qnt_logs} \n
    """

    return {
        "mensagem": head,
        "campos": [materia_url, data_logs, qnt_logs]
    }
