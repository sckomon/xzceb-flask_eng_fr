import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hi'), 'Bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Goodbye'), 'Revoir')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        self.assertNotEqual(french_to_english('Bonjour'), 'Hi')
        self.assertNotEqual(french_to_english('Revoir'), 'Goodbye')
        self.assertEqual(french_to_english('Revoir'), 'Review')

unittest.main()