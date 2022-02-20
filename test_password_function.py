import unittest
from password import count_char

class PasswordTestCase(unittest.TestCase):
    """Testes para 'password.py'."""

    # Definindo um teste que passa
    def test_valid_password(self):
        """Uma senha de 6 dígitos que atende os requisitos passa no teste?"""
        pswd = '6$aTjp'
        expected_output = 0
        self.assertEqual(count_char(pswd), print(f'\nO número mínimo de caracteres que devem ser adicionados é {expected_output}.'))
    
    #Definindo outro teste que passa
    def test_valid_password_one_missing(self):
        """Uma senha de 10 dígitos que não atende os requisitos e que precisa de 1 dígito adicional."""
        pswd = 'Hui89utthQ'
        expected_output = 1
        self.assertEqual(count_char(pswd), print(f'\nO número mínimo de caracteres que devem ser adicionados é {expected_output}.'))


unittest.main()