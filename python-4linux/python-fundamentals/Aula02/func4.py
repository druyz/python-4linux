#!/usr/bin/python3

# Usando lambda ( é uma funcao anonima ) para calculos matematicos

# Guardo em memoria
a = lambda x, y:  x + y

# Guarda na variavel
a(1,6)
# Imprime a posicao na memoria
# print(a)

# Executa somente se chamado pelo proprio arquivo, nao é executado caso feito o import
if __name__ == "__main__":
    print((lambda x, y: x + y)(5,4))
