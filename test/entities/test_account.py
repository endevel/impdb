import unittest

import datetime

from dao.account import Account


class TestAccount(unittest.TestCase):
    def test_create(self):
        account = Account()
        self.assertIsNotNone(account)

    def test_insert(self):
        account = Account()
        account.id = '1000'
        account.cis_division = 'SESB'
        account.bill_cycle = 'NTFL'
        account.setup_dt = datetime.datetime.strptime("01.01.2015", "%d.%m.%Y")
        account.premise_id = '22222'
        account.append()

if __name__ == '__main__':
    unittest.main()
