"""
    Descrição do Módulo:
Esse módulo foi feito para gerar um dicionario a partir de um arquivo
    
"""


import regex as re

__all__ = ["geraDicionario"]

def geraDicionario(arquivo):
    
    dicionario = {
    "titulo": "1984",
    "autor": "George Orwell",
    "ano_publicacao": 1949
}
    buscaDescricaoDoProjeto(arquivo, dicionario)

    return dicionario

def buscaDescricaoDoProjeto(arquivo, dicionario):

    return