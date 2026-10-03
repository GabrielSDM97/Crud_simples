# CRUD Simples em Python

Sistema de cadastro via terminal. CRUD completo com persistência em arquivo `.txt`, usando modularização.

## Funcionalidades

1. **Cadastrar nova pessoa** - salva `Nome;Idade` em `cadastros.txt`
2. **Ver pessoas cadastradas** - lista no formato `ID: X - Nome ... Y anos`
3. **Atualizar um cadastro** - edita por ID
4. **Remover um cadastro** - exclui por ID
5. **Sair do sistema**

Validação de entrada inteira (`leiaInt`), tratamento de `ValueError`/`KeyboardInterrupt` e verificação de ID válido.

## Estrutura
```
Crud_simples/
├── programa_principal.py  # cria/abre cadastros.txt e roda o loop do menu
├── cadastros.txt          # armazenamento (uma linha por cadastro: Nome;Idade)
├── menuLib/
│   ├── formato.py         # cabeçalho(), hudMenuOpções(), lista opçõesdesc
│   ├── leiaNum.py         # leiaInt(txt)
│   └── opções.py          # dispatcher opção() + op1..op5
```

## Como executar

Pré-requisito: Python 3 (sem dependências externas, só `time` da stdlib).

```bash
python programa_principal.py
# ou
python3 programa_principal.py
```

Na primeira execução o arquivo `cadastros.txt` é criado automaticamente se não existir.