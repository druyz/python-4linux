#!/usr/bin/python3

'''Criar uma lista com o quadrado perfeito de 2 a 10''' 
quadrado = [(lambda y: y**2)(x) for x in range(2,11)]

print(quadrado)
