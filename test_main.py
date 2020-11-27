"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
import random
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_main(self):
        """Função que testa se a saída do programa corresponde ao que foi especificado."""
        # Lista de valores que serão retornados pela função input.
        valor = str(random.randint(1, 1000))
        taxa = str(random.randint(0, 200))
        tempo = str(random.randint(1,240))
        input_returns = [valor, taxa, tempo]
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            assert mock_input.call_count == 3
            valor, taxa, tempo = map(float, [valor, taxa, tempo])
            resultado = valor * (1 + taxa/100)**tempo
            juros = resultado - valor
            mock_print.assert_called_with(f'O valor dos juros é igual à {juros:.2f}.')

if __name__ == '__main__':
    unittest.main()
