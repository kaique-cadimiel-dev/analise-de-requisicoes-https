# Referência da API

Este documento descreve as funções públicas presentes no projeto.

## `ocorrencias.py`

- `obter_ocorrencias(entries)`
  - Descrição: Recebe a lista de `entries` (do HAR) e retorna um dicionário
    mapeando domínio -> quantidade de ocorrências.
  - Parâmetros:
    - `entries` (list): lista de objetos de entrada do HAR (`log.entries`).
  - Retorno: `dict` com chaves sendo strings de domínio (ex: `https://example.com/`) e
    valores inteiros com o número de ocorrências.

- `ordenar_ocorrencias(ocorrencias)`
  - Descrição: Recebe o dicionário de ocorrências e retorna uma lista ordenada de
    tuplas `(domínio, ocorrências)` em ordem decrescente.
  - Parâmetros: `ocorrencias` (dict)
  - Retorno: `list` de tuplas `(domínio, contador)`

- `listar_ocorrencias_de_dominios(ocorrencias, limite=-1)`
  - Descrição: Imprime uma tabela formatada no terminal com os domínios e contadores.
  - Parâmetros:
    - `ocorrencias` (list): lista de tuplas `(domínio, contador)` (tipicamente saída de `ordenar_ocorrencias`).
    - `limite` (int): número máximo de itens a exibir; `-1` para exibir todos.

- `main()`
  - Descrição: Ponto de entrada interativo. Lê o arquivo `.har`, monta o cabeçalho,
    permite listar ocorrências e salvar em `.xlsx`.

## `utils/leitura_de_arquivo.py`

- `ler_arquivo(caminho_do_arquivo)`
  - Descrição: Valida existência e extensão do arquivo e carrega JSON do HAR.
  - Parâmetros:
    - `caminho_do_arquivo` (str / Path-like)
  - Erros lançados:
    - `FileNotFoundError` se o arquivo não existir
    - `ValueError` se o caminho não for arquivo ou extensão inválida

## `utils/montar_head.py`

- `montar_head(paginas_processadas, requisicoes)`
  - Descrição: Extrai metadados do HAR (matéria, data, quantidade de logs) e
    retorna um dicionário com `mensagem` (texto para exibir) e `campos` (lista de valores).
  - Parâmetros:
    - `paginas_processadas` (list): normalmente `logs["log"]["pages"]`
    - `requisicoes` (list): normalmente `logs["log"]["entries"]`

## `utils/save_xlsx.py`

- `save_to_xlsx(data, filename, campos_head=None, diretorio='./relatorios', columns=[...])`
  - Descrição: Salva os dados em Excel. Quando `campos_head` é fornecido,
    escreve o cabeçalho antes da tabela de ocorrências.
  - Parâmetros:
    - `data` (list): lista de pares `(domínio, contador)` ou lista adequada para `pandas.DataFrame`
    - `filename` (str): nome do arquivo a salvar
    - `campos_head` (list | None): campos do cabeçalho para incluir no Excel
    - `diretorio` (str): diretório de saída

