import os
from entidades.dicionario.Gera_Dicionario import *

__all__ = ["generator"]

def pegaDicionario(caminho_arquivo: str):

    with open(caminho_arquivo, 'r') as arquivo:

        conteudo = arquivo.read()
        dicionario = geraDicionario(conteudo)

    return dicionario

def pegaArquivos(caminho_pasta: str):
    
    lista = os.listdir(caminho_pasta)
    return lista

def generator(caminho_pasta: str):

    arquivos = pegaArquivos(caminho_pasta)
    dicionario = dict()

    for arq in arquivos:
        if arq[-3:] == ".py":
            dicionario[arq[:-3]] = pegaDicionario(caminho_pasta+'/'+arq)
    
    return dicionario

