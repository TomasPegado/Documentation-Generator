"""
Descrição do Módulo:
Esse módulo foi feito para ter funções que manipulam listas.
    
"""
"""
Nome: Lista_Generica
"""

def insereElemento(dicionario, dado, chave, posicao=None):
    """
    Insere um elemento em uma lista dentro do dicionário.
    
    Parâmetros:
    - dicionario (dict): O dicionário onde a lista é mantida.
    - dado: O elemento a ser inserido na lista.
    - chave: A chave da lista dentro do dicionário.
    - posicao (int, opcional): A posição na lista onde o elemento deve ser inserido.
    """
    if chave not in dicionario:
        dicionario[chave] = []
    if posicao is None:
        dicionario[chave].append(dado)
    else:
        dicionario[chave].insert(posicao, dado)

def removeElemento(dicionario, dado, chave, posicao=None):
    """
    Remove um elemento de uma lista dentro do dicionário.

    Parâmetros
    ----------
    dicionario : dict
        O dicionário de onde a lista será modificada.
    dado : any
        O elemento a ser removido da lista.
    chave : any
        A chave da lista dentro do dicionário.
    posicao : int, opcional
        A posição do elemento a ser removido.

    """
    if chave in dicionario:
        if posicao is None:
            dicionario[chave].remove(dado)
        else:
            dicionario[chave].pop(posicao)

def buscaElemento(dado, posicao, chave, dicionario):
    """
    Procura por um elemento em uma lista dentro do dicionário.

    Parâmetros
    ----------
    dado : any
        O elemento a ser procurado na lista.
    posicao : int
        A posição específica na lista para verificar o elemento.
    chave : any
        A chave da lista dentro do dicionário.
    dicionario : dict
        O dicionário onde a lista é mantida.

    Retorna
    -------
    bool
        Verdadeiro se o elemento for encontrado, Falso caso contrário.

    """
    if chave in dicionario:
        if posicao is None:
            return dado in dicionario[chave]
        else:
            return dicionario[chave][posicao] == dado
    return False

def insereChave(dicionario, chave):
    """
    Adiciona uma chave ao dicionário com uma lista vazia como valor se não existir.

    Parâmetros
    ----------
    dicionario : dict
        O dicionário a ser modificado.
    chave : any
        A chave para a nova lista a ser adicionada.

    Retorna
    -------
    dict
        O dicionário atualizado.

    """
    if chave not in dicionario:
        dicionario[chave] = []
    return dicionario
