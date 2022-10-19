# Test translator.py functions
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        # Test for the translation of the world 'Hello' and 'Bonjour'.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Test for null input for englishToFrench
        self.assertNotEqual(english_to_french(''), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        # Test for the translation of the world 'Bonjour' and 'Hello'.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # Test for null input for frenchToEnglish
        self.assertNotEqual(french_to_english(''), 'Hello')


unittest.main()