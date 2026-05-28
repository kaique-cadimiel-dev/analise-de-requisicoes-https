from utils.leitura_de_arquivo import ler_arquivo
from utils.montar_head import montar_head
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

def listarOcorrencias_de_dominios(ocorrencias, limite=-1):
    header = ["Domínio", "Ocorrências"]
    table = tabulate.tabulate(ocorrencias[:limite], headers=header, tablefmt="grid")
    print(f"Foram encontradas ocorrencias em {len(ocorrencias)} domínios")
    print(table)

print(head)


ocorrencias = obter_ocorrencias(entries)
ocorrencias = ordenar_ocorrencias(ocorrencias)
listarOcorrencias_de_dominios(ocorrencias)