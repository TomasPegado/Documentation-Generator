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
# class TestExtrairModulo(unittest.TestCase):
#     def test_01_busca_modulo_ok_condicao_retorno(self):
#         print("Caso de Teste 01 - Buscar Modulo com sucesso")

#         with open("/home/tomas/PUC/Modular/arquivoTeste.txt", 'r') as arquivo:
#             conteudo = arquivo.read()

#         dicionario = gd.geraDicionario(conteudo)

#         retorno_esperado = dicionario['modulos']

#         self.assertEqual(retorno_esperado, {"Gera_Dicionario": {}, "Documentacao": {}})

if __name__ == '__main__':
    unittest.main()


