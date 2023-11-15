"""
    Descrição do Projeto:
Esse módulo foi feito para gerar um dicionario a partir de um arquivo
    
"""
"""
Modulo: Gera_Dicionario
"""

import regex as re

__all__ = ["geraDicionario"]

def geraDicionario(conteudo):
    
    dicionario = dict()
    buscaDescricaoDoProjeto(conteudo, dicionario)

    return dicionario

def buscaDescricaoDoProjeto(conteudo, dicionario):

    # Definir o padrão de regex
    padrao = r'Descrição do Módulo:(.*?)"""'

    # Buscar pela descrição do módulo
    match = re.search(padrao, conteudo, re.DOTALL)

    if match:
        match = match.group(1).strip()  # Retorna o texto capturado, removendo espaços extras
        dicionario['descrição'] = match
        return match
    else:
        return "Descrição do módulo não encontrada."
    
"""
Modulo: documentacao
"""