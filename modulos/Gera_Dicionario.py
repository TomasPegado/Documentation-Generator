"""
Descrição do Modulo:
Esse projeto foi feito para gerar um dicionario com as informações 
dos módulos
    
"""
"""
Nome: Gera_Dicionario
"""

import regex as re
import entidades.Lista_Generica.Lista_Generica

__all__ = ["geraDicionario"]

def geraDicionario(conteudo: str, type: str):
    """
    Principal função do módulo. Ela recebe o conteudo do módulo e gera o dicionario.
    Utiliza as outras funções desse módulo para fazer a leitura e extração dos dados.
    
    Parâmetros:
    - conteudo: Conteudo do módulo
    - type: Se é o conteúdo de um módulo ou da página home
    """
    if type == "modulo":

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

    elif type == "home":

        dicionario = dict()
        buscaNomeProjetoHome(conteudo, dicionario)
        buscaDescriçãoProjetoHome(conteudo, dicionario)
        buscaIntegrantesHome(conteudo, dicionario)

    return dicionario

def buscaDescricaoDoModulo(conteudo: str, dicionario: dict):
    """
    Função que busca a descrição do módulo
    
    Parâmetros:
    - conteudo: Conteudo do módulo
    - dicionario: Dicionario para inserir os dados extraidos
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
    """
    Função que busca o nome do módulo
    
    Parâmetros:
    - conteudo: Conteudo do módulo
    - dicionario: Dicionario para inserir os dados extraidos
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
    """
    Função que busca Imports do modulo
    
    Parâmetros:
    - conteudo: Conteudo do módulo
    - dicionario: Dicionario para inserir os dados extraidos
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
    """
    Função que busca a descrição da funcao
    
    Parâmetros:
    - conteudo: Conteudo do módulo
    - dicionario: Dicionario para inserir os dados extraidos
    - funcao: nome da função
    """  
    
    # Definir o padrão de regex para encontrar o começo da docstring da função
    padrao = rf"def\s+{re.escape(funcao)}\s*\(.*?\):\s*\"\"\"(.*?)\"\"\""

    match = re.search(padrao, conteudo, re.DOTALL)
    if match:
        descricao = match.group(1).strip()
        # Se os placeholders não forem necessários, remova-os
        descricao = descricao.replace('_description_', '').replace('_type_', '').strip()
        # Certifique-se de que a chave 'funcoes' exista e de que a função esteja nela
        if 'funcoes' not in dicionario:
            dicionario['funcoes'] = {}
        if funcao not in dicionario['funcoes']:
            dicionario['funcoes'][funcao] = {}
        dicionario['funcoes'][funcao]['descricao'] = descricao
    else:
        print(f'Nenhuma descrição para a função: {funcao}')


def buscaFuncoes(conteudo: str, dicionario: dict):
    """
    Função que busca as funções criadas no módulo
    
    Parâmetros:
    - conteudo: Conteudo do módulo
    - dicionario: Dicionario para inserir os dados extraidos
    - funcao: nome da função
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
    """
    Função que busca as funções contidas no __all__
    
    Parâmetros:
    - conteudo: Conteudo do módulo
    - dicionario: Dicionario para inserir os dados extraidos
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

def buscaNomeProjetoHome(conteudo: str, dicionario: dict):
    """
    Função que busca o nome do Projeto no home.txt
    
    Parâmetros:
    - conteudo: Conteudo do módulo
    - dicionario: Dicionario para inserir os dados extraidos
    """
    # Padrão Regex
    padrao = r'Nome do Projeto:\s*(.*)'

    # Buscar pelo padrão no conteúdo
    match = re.search(padrao, conteudo)

    if match:
        nome_projeto = match.group(1)  # Captura o nome do projeto
        dicionario["nome_projeto"] = nome_projeto
    else:
        print("Nome do Projeto não encontrado.")

def buscaDescriçãoProjetoHome(conteudo: str, dicionario: dict):
    """
    Função que busca a descrição do Projeto no home.txt
    
    Parâmetros:
    - conteudo: Conteudo do módulo
    - dicionario: Dicionario para inserir os dados extraidos
    """   

    # Definir o padrão de regex
    padrao = r'Descrição:(.*?)Integrantes'

    # Buscar pela descrição do modulo
    match = re.search(padrao, conteudo, re.DOTALL)

    if match:
        match = match.group(1).strip()  # Retorna o texto capturado, removendo espaços extras
        dicionario['descricao_projeto'] = match
        return match
    else:
        return "Descrição do modulo não encontrada."

def buscaIntegrantesHome(conteudo: str, dicionario: dict):
    """
    Função que busca o nome dos integrantes na home.txt
    
    Parâmetros:
    - conteudo: Conteudo do módulo
    - dicionario: Dicionario para inserir os dados extraidos
    """

    # Padrão Regex
    padrao = r'Integrantes:\s*(.*)'

    # Buscar pelo padrão no conteúdo
    match = re.search(padrao, conteudo)

    if match:
        integrantes = match.group(1)  # Captura a lista de integrantes
        
        lista_integrantes = integrantes.split(', ') # Dividir a string em uma lista, usando vírgula como separador
        dicionario["integrantes_projeto"] = lista_integrantes 
    else:
        print("Integrantes não encontrados.")

