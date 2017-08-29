import unittest

from entities.account import Account


class TestAccount(unittest.TestCase):
    def test_create(self):
        acc = Account()
        self.assertIsNotNone(acc)


if __name__ == '__main__':
    unittest.main()
