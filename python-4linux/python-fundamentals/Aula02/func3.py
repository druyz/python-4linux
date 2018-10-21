#!/usr/bin/python3

# Transforma em tupla, acessa por indice e pode percorrer
def teste(*args):
    print(args)

# Transforma em dicionario, te retorna a chave e valor do campo requerido e tanto faz a ordem
def teste2(**kwargs):
    print(kwargs)

teste('daniel',2,5,6,'prata')

teste2(nome='daniel', sobrenome='prata', idade=24)