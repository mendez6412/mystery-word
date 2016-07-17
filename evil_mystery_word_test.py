
import unittest
from evil_mystery_word import *

word_list4 = ['bird', 'calf', 'fore']

family4 = {'----': ['bird', 'calf'], '---e': ['fore']}

class TestMysteryWord(unittest.TestCase):

    def test_partition_word_list(self):
        self.assertEqual(partition_word_list('e', word_list4), {'----': ['bird', 'calf'], '---e': ['fore']})
    #TEST 4:
    def test_longest_family_tuple(self):
        self.assertEqual(longest_family_tuple(family4), ('----', ['bird', 'calf']))
    # def test_easy_words(self):
    #     self.assertEqual(easy_words(word_list), ["bird", "calf", "river", "stream", "brain"])
    def test_word_list_length(self):
        self.assertEqual(word_list_length(word_list4), 3)

    def test_check_guess(self):
        self.assertTrue(check_guess('e'))

if __name__ == '__main__':
    unittest.main()
