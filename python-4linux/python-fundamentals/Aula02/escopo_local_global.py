#!/usr/bin/python3

var = 10

def escopo():
    # Caso nao definir ela como global a variavel var sera local na funcao
    global var
    var = 5
    print(var)

escopo()
print(var)

# Passando variavel default caso nao tenha passado para uma variavel da funcao
def soma(x,y=10):
    return x + y

# Usando o pass nao executa o codigo na funcao e ignora caso nao tenha passado as variaveis da funcao
def dividir():
    pass

a = soma(5)
b = soma(5,5)

print(a,b)
