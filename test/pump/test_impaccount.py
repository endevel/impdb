import unittest

from pump.impaccount import ImpAccount


class TestImpAccount(unittest.TestCase):
    def test_create(self):
        imp = ImpAccount()
        self.assertIsNotNone(imp)

    def test_simple_imp(self):
        imp = ImpAccount()
        imp.read('C:/Data/ci_acct_test.csv')
        self.assertEqual(42 , imp.row_count)

if __name__ == '__main__':
    unittest.main()
