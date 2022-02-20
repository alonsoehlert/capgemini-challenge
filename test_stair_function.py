import unittest
from stair import stair

class StairTestCase(unittest.TestCase):
    """Testes para 'stair.py'."""

    # Definindo um teste que passa
    def test_seven_steps_stair(self):
        """Uma escada de 7 degraus pode ser desenhada?"""
        stair_seven = stair(7)
        output = print('      *','     **','    ***','   ****','  *****',' ******','*******', sep='\n')
        self.assertEqual(stair_seven, output)
    
    # Definindo um teste que não passa
    def test_null_stair(self):
        """Uma escada com entrada de 0 degrau pode ser desenhada?"""
        stair_null = stair(0)
        output = print('')
        self.assertEqual(stair_null, output)


unittest.main()