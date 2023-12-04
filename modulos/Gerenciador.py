"""
Descrição do Modulo:
Modulo que gerencia a trnaformação dos dados recebidos nas páginas em html.
Ele usa as funções disponibilizadas pelos modulos de Gera Dicionario e 
Formata HTML e disponibiliza para a main (app.py) a função generator.
    
"""
"""
Nome: Gerenciador
"""

import os
from entidades.Gera_Dicionario.geraDicionario import *
from entidades.Formatador.formata_html import *

__all__ = ["generator"]

def pegaDicionario(caminho_arquivo: str, type: str):
    """
    Função que recebe o caminho do arquivo, le o conteudo e passa
    para a funcao geraDicionario poder gerar o dicionario com os dados
    extraídos formatados.
    
    Parâmetros:
    - caminho_arquivo (str): Caminho para o arquivo a ser lido
    - type: Se é um arquivo de modulo ou a pagina home.
    """

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:

        conteudo = arquivo.read()
        dicionario = geraDicionario(conteudo, type)

    return dicionario

def pegaArquivos(caminho_pasta: str):
    """
    Função que busca os arquivos do diretório passado no caminho.
    
    Parâmetros:
    - caminho_arquivo (str): Caminho para o diretório
    """
    
    lista = os.listdir(caminho_pasta)
    return lista

def generator(caminho_pasta: str):
    """
    Função principal desse módulo. Vai receber o caminho do diretório
    gerar o dicionario com os dados do projeto e vai usar a funcao formataHTML
    para gerar e formatar os arquivos html da documentação.
    
    Parâmetros:
    - caminho_arquivo (str): Caminho para o arquivo a ser lido
    - type: Se é um arquivo de modulo ou a pagina home.
    """

    arquivos = pegaArquivos(caminho_pasta)
    dicionario = dict()

    for arq in arquivos:
        if arq[-3:] == ".py":
            dicionario[arq[:-3]] = pegaDicionario(caminho_pasta+'/'+arq, "modulo")
    if "home.txt" in arquivos:
        dicionario["home"] = pegaDicionario(caminho_pasta+'/'+"home.txt", "home")
    
    # print(dicionario)
    
    formataHTML(dicionario, caminho_pasta)

