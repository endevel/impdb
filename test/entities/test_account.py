import unittest

import datetime

from dao.account import Account


class TestAccount(unittest.TestCase):
    def test_create(self):
        account = Account()
        self.assertIsNotNone(account)


if __name__ == '__main__':
    unittest.main()
