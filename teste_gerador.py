import unittest
import entidades.Gerador.gerador as ge

class TestExtraiConteudoDaPasta(unittest.TestCase):

    def test_01_extrai_arquivos_python(self):
        print("Caso de Teste 01 - Buscar arquivos com sucesso")

        caminho = "/home/tomas/PUC/Modular/modulos"

        retorno_esperado = ge.pegaArquivos(caminho)

        self.assertEqual(retorno_esperado, ["Lista_Generica.py", "Gera_Dicionario.py"])



if __name__ == '__main__':
    unittest.main()