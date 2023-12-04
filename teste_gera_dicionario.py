import unittest
import entidades.Gera_Dicionario.geraDicionario as gd


class TestExtrairDescricaoProjeto(unittest.TestCase):

    def test_01_busca_descricao_ok_condicao_retorno(self):
        print("Caso de Teste 01 - Buscar descrição com sucesso")

        with open("ArquivosTestes/arquivoTeste.txt", 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        dicionario = gd.geraDicionario(conteudo, "modulo")

        retorno_esperado = dicionario['descrição']

        self.assertEqual(retorno_esperado, "Esse projeto foi feito para gerar um dicionario a partir de um arquivo")

    def test_02_busca_nome_ok_condicao_retorno(self):
        print("Caso de Teste 02 - Buscar nome com sucesso")

        with open("ArquivosTestes/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()

        dicionario = {'nome': ''}
        gd.buscaNome(conteudo, dicionario)

        retorno_esperado = dicionario['nome']

        self.assertEqual(retorno_esperado, "Gera_Dicionario")

class TestExtraiImports(unittest.TestCase):
    def test_03_busca_imports_ok_condicao_retorno(self):
        print("Caso de Teste 03 - Buscar Imports com sucesso")

        with open("ArquivosTestes/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()

        dicionario = dict()
        gd.buscaImports(conteudo, dicionario)

        retorno_esperado = dicionario['imports']

        self.assertEqual(retorno_esperado, ['regex as re'])

class TestExtraiFuncoes(unittest.TestCase):

    def test_04_busca_funcoes_ok_condicao_retorno(self):

        print("Caso de Teste 04 - Buscar Funções com sucesso")

        with open("ArquivosTestes/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()

        dicionario = {'funcoes': {}}
        gd.buscaFuncoes(conteudo, dicionario)

        retorno_esperado = list(dicionario['funcoes'].keys())

        self.assertEqual(retorno_esperado, ['geraDicionario', 'buscaDescricaoDoModulo'])
    

class TestExtraiFuncoesDisponibilizadas(unittest.TestCase):

    def test_05_busca_funcoes_disponibilizadas_ok_condicao_retorno(self):

        print("Caso de Teste 05 - Buscar Descrição das Funções com sucesso")

        with open("ArquivosTestes/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()
        
        dicionario = {'_all_': []}
        gd.buscaAll(conteudo, dicionario)

        retorno_esperado = dicionario['_all_']

        self.assertEqual(retorno_esperado, ["geraDicionario", 'buscaDescricaoDoModulo'])

if __name__ == '__main__':
    unittest.main()


