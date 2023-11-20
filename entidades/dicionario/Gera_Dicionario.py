"""
Descrição do Modulo:
Esse projeto foi feito para gerar um dicionario a partir de um arquivo
    
"""
"""
Nome: Gera_Dicionario
"""

import regex as re
import entidades.Lista_Generica.Lista_Generica

__all__ = ["geraDicionario"]

def geraDicionario(conteudo: str):
    """Aqui esta a descrição da função geraDicionario

    Parameters
    ----------
    conteudo : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    
    dicionario = {
        'descrição': '', 
        'nome': '', 
        'imports': [],
        'funcoes': {},
        '_all_': []
    }
    buscaDescricaoDoModulo(conteudo, dicionario)
    buscaNome(conteudo, dicionario) 
    buscaImports(conteudo, dicionario)
    buscaFuncoes(conteudo, dicionario)
    buscaAll(conteudo, dicionario)

    return dicionario

def buscaDescricaoDoModulo(conteudo: str, dicionario: dict):
    """Aqui esta a descrição da função geraDicionario

    Parameters
    ----------
    conteudo : str
        _description_
    dicionario : dict
        _description_

    Returns
    -------
    _type_
        _description_
    """      

    # Definir o padrão de regex
    padrao = r'Descrição do Modulo:(.*?)"""'

    # Buscar pela descrição do modulo
    match = re.search(padrao, conteudo, re.DOTALL)

    if match:
        match = match.group(1).strip()  # Retorna o texto capturado, removendo espaços extras
        dicionario['descrição'] = match
        return match
    else:
        return "Descrição do modulo não encontrada."

def buscaNome(conteudo: str, dicionario: dict):
    """_summary_

    Parameters
    ----------
    conteudo : str
        _description_
    dicionario : dict
        _description_

    Returns
    -------
    _type_
        _description_
    """    
    # Definir o padrão de regex
    padrao = r'Nome:(.*?)"""'

    # Buscar pela descrição do modulo
    match = re.search(padrao, conteudo, re.DOTALL)

    if match:
        match = match.group(1).strip()  # Retorna o texto capturado, removendo espaços extras
        dicionario['nome'] = match
    
    else:
        return "Nome do modulo não encontrada."

def buscaImports(conteudo: str, dicionario: dict):
    """_summary_

    Parameters
    ----------
    conteudo : str
        _description_
    dicionario : dict
        _description_
    """    

    # Definir o padrão de regex
    padrao1 = r'^import\s+([^\n]+)'
    padrao2 = r'from\s+([^\s]+)\s+import\s+'

    # Encontrar todas as correspondências para 'import'
    matches1 = re.findall(padrao1, conteudo, re.MULTILINE)
    matches2 = re.findall(padrao2, conteudo, re.MULTILINE)
    if matches1:
        dicionario['imports'] = matches1
    if matches2:
        dicionario['imports'] += matches2
    return 

def buscaDescricaoFuncao(conteudo: str, dicionario: dict, funcao: str):
    """_summary_

    Parameters
    ----------
    conteudo : str
        _description_
    dicionario : dict
        _description_
    funcao : str
        _description_
    """    

    # Definir o padrão de regex
    padrao1 = rf"def\s+{re.escape(funcao)}\s*\(.*?\):\s*((.|\n)*)" #Padrao para achar a funcao
    # padrao2 = r'Descrição:(.*?)Parameters'
    padrao2 = r'"""(.*?)"""'

    # Encontrar a correpondencia para a funcao
    match = re.search(padrao1, conteudo)
    if match:
        conteudoDaFuncao = match.group(1)  # Obtém o texto capturado após a declaração da função
        match2 = re.search(padrao2, conteudoDaFuncao, re.DOTALL)
        if match2:
            descricao = match2.group(1).strip()  # Remove espaços em branco extras
            dicionario['funcoes'][funcao]['descricao'] = descricao

        else:
            print('Nenhuma descrição para a funcao: ', funcao)
    else:
        print("Não encontrou match para a funcao: ", funcao)
    return

def buscaFuncoes(conteudo: str, dicionario: dict):
    """_summary_

    Parameters
    ----------
    conteudo : str
        _description_
    dicionario : dict
        _description_
    """    

    # Definir o padrão de regex
    padrao = r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('

    # Encontrar todas as correspondências para 'funcoes'
    matche = re.findall(padrao, conteudo, re.MULTILINE)

    if matche:
        for func in matche:
            dicionario['funcoes'][func] = {}
            buscaDescricaoFuncao(conteudo, dicionario, func)
    return

def buscaAll(conteudo: str, dicionario: dict):
    """_summary_

    Parameters
    ----------
    conteudo : str
        _description_
    dicionario : dict
        _description_
    """

    #definir o padrão regex
    padrao = r'__all__\s*=\s*\["(.*?)"\]'
    match = re.search(padrao, conteudo, re.DOTALL)

    if match:
        match = match.group(1).strip()  # Retorna o texto capturado, removendo espaços extras
        lista_funcoes = match.split('", "')
        dicionario['_all_'] += lista_funcoes
    
    else:
        return "Nenhuma restrição de funções disponibilizadas"  

