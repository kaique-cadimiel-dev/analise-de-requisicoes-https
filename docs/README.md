# Documentação do Projeto

## Visão Geral

Este projeto analisa arquivos HAR (exportados por serviços como speedvitals.com) e gera
relatórios sobre os domínios acessados nas requisições HTTP(S).

Funcionalidades principais:
- Contagem de ocorrências por domínio
- Listagem ordenada por número de ocorrências
- Exportação para Excel (.xlsx) com cabeçalho de relatório

## Pré-requisitos
- Python 3.8+
- Ambiente virtual recomendado

## Instalação

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Uso
1. Exporte seu arquivo HAR (por exemplo em https://speedvitals.com) e salve como `net.har` na raiz do projeto.
2. Execute:

```bash
python ocorrencias.py
```

3. Siga as instruções interativas no terminal para listar ou salvar o relatório.

Os relatórios gerados são salvos na pasta `relatorios/` como arquivos `.xlsx`.

## Gerando o arquivo HAR no speedvitals

1. Acesse o site `https://speedvitals.com` e execute a análise da página desejada.
2. Aguarde a conclusão do relatório (o processamento pode levar alguns segundos a minutos).
3. Clique na aba **Waterfall** para ver a lista de requisições.
4. Role a página até o final da lista de requisições — o botão **Download HAR** aparece abaixo da tabela.
5. Clique em **Download HAR** e salve o arquivo como `net.har` na raiz deste projeto.

Observação: em alguns navegadores o botão só fica disponível após a lista completar o carregamento; se não aparecer, aguarde alguns segundos e role novamente.

## Estrutura do Projeto

- `ocorrencias.py`: ponto de entrada e lógica de interação com o usuário
- `utils/`: funções utilitárias (leitura de arquivo, montagem de cabeçalho, salvar xlsx)
- `relatorios/`: saída padrão para arquivos gerados
- `docs/`: documentação do projeto (esta pasta)

## Mais informações
- API e detalhes das funções em [docs/API.md](API.md)
- Diretrizes de contribuição em [CONTRIBUTING.md](../CONTRIBUTING.md)
