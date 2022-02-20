import unittest
from anagrams import anagram_substring_count

class StairTestCase(unittest.TestCase):
    """Testes para 'anagrams.py'."""

    # Definindo um teste que passa
    def test_anagrams_1(self):
        """A palavra faca deve retornar 2 pares de anagramas (a,a) e (ac,ca)."""
        string = 'faca'
        output = 2
        self.assertEqual(anagram_substring_count(string), print(output))
    
    # Definindo um teste que passa
    def test_anagrams_2(self):
        """A palavra trator deve retornar 4 pares de anagramas (t,t), (r,r), (tr, tr), (rt, tr)."""
        string = 'trator'
        output = 4
        self.assertEqual(anagram_substring_count(string), print(output))
 
unittest.main()