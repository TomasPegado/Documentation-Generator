import unittest
import Gera_Dicionario as gd


class TestExtrairDescricaoProjeto(unittest.TestCase):

    def test_01_busca_descricao_ok_condicao_retorno(self):
        print("Caso de Teste 01 - Buscar descrição com sucesso")

        with open("/home/tomas/PUC/Modular/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()

        dicionario = gd.geraDicionario(conteudo)

        retorno_esperado = dicionario['descrição']

        self.assertEqual(retorno_esperado, "Esse projeto foi feito para gerar um dicionario a partir de um arquivo")

    def test_02_busca_nome_ok_condicao_retorno(self):
        print("Caso de Teste 02 - Buscar nome com sucesso")

        with open("/home/tomas/PUC/Modular/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()

        dicionario = {'nome': ''}
        gd.buscaNome(conteudo, dicionario)

        retorno_esperado = dicionario['nome']

        self.assertEqual(retorno_esperado, "Gera_Dicionario")

class TestExtraiImports(unittest.TestCase):
    def test_03_busca_imports_ok_condicao_retorno(self):
        print("Caso de Teste 03 - Buscar Imports com sucesso")

        with open("/home/tomas/PUC/Modular/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()

        dicionario = dict()
        gd.buscaImports(conteudo, dicionario)

        retorno_esperado = dicionario['imports']

        self.assertEqual(retorno_esperado, ['regex as re', 'pandas as pd', 'numpy', 'entidades.dicionario.Gera_Dicionario', 'entidades.Gerador.gerador'])

class TestExtraiFuncoes(unittest.TestCase):

    def test_04_busca_funcoes_ok_condicao_retorno(self):

        print("Caso de Teste 04 - Buscar Funções com sucesso")

        with open("/home/tomas/PUC/Modular/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()

        dicionario = {'funcoes': {}}
        gd.buscaFuncoes(conteudo, dicionario)

        retorno_esperado = list(dicionario['funcoes'].keys())

        self.assertEqual(retorno_esperado, ['geraDicionario', 'buscaDescricaoDoModulo'])
    
    def test_05_busca_descricoes_funcoes_ok_condicao_retorno(self):

        print("Caso de Teste 05 - Buscar Descrição das Funções com sucesso")

        with open("/home/tomas/PUC/Modular/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()
        
        funcoes = ['geraDicionario', 'buscaDescricaoDoModulo']
        dicionario = {'funcoes': {'geraDicionario': {'descricao': ''}, 'buscaDescricaoDoModulo': {'descricao': ''}}}
        for func in funcoes:

            gd.buscaDescricaoFuncao(conteudo, dicionario, func)
        descricoes = []
        for key in dicionario['funcoes'].keys():
            descricoes.append(dicionario['funcoes'][key]['descricao'])
        retorno_esperado = descricoes

        self.assertEqual(retorno_esperado, ['Descrição: Aqui esta a descrição da função geraDicionario\n\n    Parameters\n    ----------\n    conteudo : _type_\n        string\n\n    Returns\n    -------\n    _type_\n        _description_', 'Descrição: Aqui esta a descrição da função buscaDescricaoDoModulo\n\n    Parameters\n    ----------\n    conteudo : _type_\n        string\n\n    Returns\n    -------\n    _type_\n        _description_'])
    
    def test_06_busca_descricao_funcao_dentro_de_buscaFuncao_ok_condicao_retorno(self):

        print("Caso de Teste 06 - Buscar Descrição das Funções usando o buscaFuncoes")

        with open("/home/tomas/PUC/Modular/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()

        dicionario = {'funcoes': {}}
        gd.buscaFuncoes(conteudo, dicionario)

        descricoes = []
        for key in dicionario['funcoes'].keys():
            descricoes.append(dicionario['funcoes'][key]['descricao'])
        retorno_esperado = descricoes

        self.assertEqual(retorno_esperado, ['Descrição: Aqui esta a descrição da função geraDicionario\n\n    Parameters\n    ----------\n    conteudo : _type_\n        string\n\n    Returns\n    -------\n    _type_\n        _description_', 'Descrição: Aqui esta a descrição da função buscaDescricaoDoModulo\n\n    Parameters\n    ----------\n    conteudo : _type_\n        string\n\n    Returns\n    -------\n    _type_\n        _description_'])

class TestExtraiFuncoesDisponibilizadas(unittest.TestCase):

    def test_07_busca_funcoes_disponibilizadas_ok_condicao_retorno(self):

        print("Caso de Teste 07 - Buscar Descrição das Funções com sucesso")

        with open("/home/tomas/PUC/Modular/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()
        
        dicionario = {'_all_': []}
        gd.buscaAll(conteudo, dicionario)

        retorno_esperado = dicionario['_all_']

        self.assertEqual(retorno_esperado, ["geraDicionario", "buscaDescricaoDoModulo"])

if __name__ == '__main__':
    unittest.main()


