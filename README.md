# analise-de-requisicoes-https

Ferramenta para analisar arquivos HAR (exportados por speedvitals.com) e gerar relatórios
sobre os domínios mais requisitados em requisições HTTPS.

Principais recursos:
- Conta ocorrências de domínios nas requisições
- Exibe relatório em tabela no terminal
- Exporta relatório para arquivo Excel (.xlsx)

Veja a documentação completa em [docs/README.md](docs/README.md)

Uso rápido:
1. Coloque seu arquivo `net.har` na raiz do projeto.
2. Crie um ambiente virtual e instale dependências:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Execute:

```
python ocorrencias.py
```

Entrada: arquivo `.har` com os logs exportados.
Saída: relatório exibido no terminal e opção de salvar em `relatorios/`.

Como obter o arquivo `.har` via speedvitals:

- Execute a análise em `https://speedvitals.com`.
- Abra a aba `Waterfall`, role até o fim da lista de requisições e clique em **Download HAR**.
- Salve o arquivo como `net.har` na raiz do projeto antes de executar o script.

ou

- Execute a análise em `https://www.catchpoint.com/webpagetest`
- Clique em Export, em seguida clique em **Download HAR**

Para detalhes de API e contribuição, veja os arquivos em `docs/` e `CONTRIBUTING.md`.
