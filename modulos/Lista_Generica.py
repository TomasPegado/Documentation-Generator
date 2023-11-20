

def insereElemento(dicionario, dado, chave, posicao=None):
    if chave not in dicionario:
        dicionario[chave] = []
    if posicao is None:
        dicionario[chave].append(dado)
    else:
        dicionario[chave].insert(posicao, dado)

def removeElemento(dicionario, dado, chave, posicao=None):
    if chave in dicionario:
        if posicao is None:
            dicionario[chave].remove(dado)
        else:
            dicionario[chave].pop(posicao)

def buscaElemento(dado, posicao, chave, dicionario):
    if chave in dicionario:
        if posicao is None:
            return dado in dicionario[chave]
        else:
            return dicionario[chave][posicao] == dado
    return False

def insereChave(dicionario, chave):
    if chave not in dicionario:
        dicionario[chave] = []
    return dicionario
