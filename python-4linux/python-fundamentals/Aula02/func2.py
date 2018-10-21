#!/usr/bin/python3

def ler_arquivo(nome):
    """ Funcao para ler conteudo do arquivo
    params -> str
    return -> list
    """
    try:
        with open(nome, 'r') as arq:
            return arq.readlines()
    except FileNotFoundError:
        return []
    

def escrever_arquivo(nome:str, conteudo:list)->bool:
    """ Funcao para escrever e, arquivo
    params -> nome:str conteudo:list
    return -> bool
    """
    with open(nome, 'a') as arq:
        try:
            conteudo = ['{}\n'.format(x) for x in conteudo if x != '\n']
            arq.writelines(conteudo)
            return True
        except Exception:
            return False

letras = [chr(x) for x in range (97, +97+26)]
conteudo = ler_arquivo('teste.csv')
ler_arquivo('texto')
ler_arquivo('texto1.txt')
ler_arquivo('texto2.txt')
ler_arquivo('texto3.txt')
ler_arquivo('texto4.txt')