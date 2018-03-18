import unittest
from card import *


class TestCardMethods(unittest.TestCase):

    def test_possible_solutions(self):
        self.assertEqual(len(possible_solutions(all_cards())), 324)


if __name__ == '__main__':
    unittest.main()
