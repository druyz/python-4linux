#!/usr/bin/python3

class Dog():
    '''Tentando abstrair cachorro'''
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print('latindo....')

dog1 = Dog('bilu', 'pitbul', 2)
dog2 = Dog('rex', 'poodle', 1)

print(dog1.nome, dog1.raca, dog1.idade)
dog1.latir()
