from datetime import datetime

def obter_data_hora_logs(data_de_leitura):
    data_iso = data_de_leitura.replace("Z", "+00:00")
    return datetime.fromisoformat(data_iso)

def formatar_data_logs(data_de_leitura):
    return obter_data_hora_logs(data_de_leitura).date().strftime("%d/%m/%Y")

def formatar_hora_logs(data_de_leitura):
    return obter_data_hora_logs(data_de_leitura).time().strftime("%H:%M:%S")

def montar_head(paginas_processadas, requisicoes):
    materia_url = paginas_processadas[0]["title"]
    data_de_leitura = paginas_processadas[0]["startedDateTime"]
    qnt_logs = len(requisicoes)

    data_logs = formatar_data_logs(data_de_leitura)
    hora_logs = formatar_hora_logs(data_de_leitura)

    head = f"""
Materia: {materia_url} \n
Data de leitura dos logs: {data_logs} \n
Hora de leitura dos logs: {hora_logs} \n
Quantidade de logs: {qnt_logs} \n
    """

    return {
        "mensagem": head,
        "campos": [materia_url, data_logs, hora_logs, qnt_logs]
    }
