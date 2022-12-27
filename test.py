import unittest
from card import *


class TestCardMethods(unittest.TestCase):

    def test_all_cards(self):
        self.assertEqual(len(list(all_cards())), 21)

def test_possible_solutions(self):
        self.assertEqual(len(list(all_solutions())), 324)


if __name__ == '__main__':
    unittest.main()
