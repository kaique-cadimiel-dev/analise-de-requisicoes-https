import json
from pathlib import Path

EXTENSOES_PERMITIDAS = {'.har'}

def ler_arquivo(caminho_do_arquivo):
    path = Path(caminho_do_arquivo)

    if not path.exists():
        raise FileNotFoundError(f"O arquivo '{caminho_do_arquivo}' não foi encontrado.")

    if not path.is_file():
        raise ValueError(f"'{caminho_do_arquivo}' não é um arquivo.")

    if path.suffix.lower() not in EXTENSOES_PERMITIDAS:
        raise ValueError(f"Extensão inválida '{path.suffix}'. Permitidas: {', '.join(EXTENSOES_PERMITIDAS)}")

    with open(caminho_do_arquivo, 'r', encoding="utf-8") as arquivo:
        return json.load(arquivo)
