import unittest
import entidades.Gerenciador.gerenciador as ge

class TestExtraiConteudoDaPasta(unittest.TestCase):

    def test_01_extrai_arquivos_python(self):
        print("Caso de Teste 01 - Buscar arquivos com sucesso")

        caminho = "modulos"

        retorno_esperado = ge.pegaArquivos(caminho)

        self.assertEqual(retorno_esperado, ['Formata_HTML.py','Lista_Generica.py','Gera_Dicionario.py','static','home.txt','Gerenciador.py'])


if __name__ == '__main__':
    unittest.main()