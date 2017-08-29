import unittest

from db.dbconnect import DBConnect


class TestDBConnect(unittest.TestCase):
    def test_connection(self):
        db = DBConnect.connection()
        self.assertIsNotNone(db)
'''
    def test_insert(self):
        db = DBConnect.connection()
        x = db.xact()
        x.start()
        ps = db.prepare("delete from account")
        ps()

        ps = db.prepare("insert into account(id, cis_division) values ($1, $2, $2)")
        ps('111111', '01.01.2015', 'SESB')
        x.commit()
'''

if __name__ == '__main__':
    unittest.main()
