# CRUD Simples em Python

Sistema de cadastro via terminal. CRUD completo com persistência em arquivo `.txt`, usando modularização.

## Funcionalidades

1. **Cadastrar nova pessoa** - salva `Nome;Idade` em `cadastros.txt`
2. **Ver pessoas cadastradas** - lista no formato `ID: X - Nome ... Y anos` (ID começa em 0)
3. **Atualizar um cadastro** - edita por ID
4. **Remover um cadastro** - exclui por ID
5. **Sair do sistema**

Validação de entrada inteira (`leiaInt`), tratamento de `ValueError`/`KeyboardInterrupt` e verificação de ID válido.

## Estrutura
```
Crud_simples/
├── __main__.py           # cria/abre cadastros.txt e roda o loop do menu
├── README.md
├── .gitignore            # ignora __pycache__/ e *.txt
├── menuLib/
│   ├── __init__.py
│   ├── formato.py        # cabeçalho(), hudMenuOpções(), opçõesdesc
│   ├── leiaNum.py        # leiaInt(txt)
│   └── opções.py         # dispatcher opção() + op1..op5
```

O arquivo `cadastros.txt` (uma linha por cadastro: `Nome;Idade`) não é versionado — é criado automaticamente na primeira execução.

## Como executar

Pré-requisitos: Python 3 (sem dependências externas, só `time` e `os` da stdlib). Funciona em Linux, macOS e Windows (limpeza de tela multiplataforma via `os.name`).

```bash
python .
# ou
python __main__.py
# ou
python3 .
```

Na primeira execução o arquivo `cadastros.txt` é criado automaticamente se não existir.
