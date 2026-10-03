from menuLib.leiaNum import *
from menuLib.formato import hudMenuOpções
from menuLib.opções import opção
from os import system

nome_arq = 'cadastros.txt'

def sistema():
    try:
        arq = open(nome_arq, 'xt+')
        print(f'\nArquivo \'{nome_arq}\' criado com sucesso!\n')
        arq.close()
    except FileExistsError:
        print(f'\nArquivo \'{nome_arq}\' já existe!\n')
    finally:
        while True:
            system("clear")
            hudMenuOpções()
            op = leiaInt('Sua opção: ')
            opção(op, nome_arq)


if __name__ == "__main__":
    sistema()
