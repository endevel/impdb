import datetime

from db.dbconnect import DBConnect


class Account:
    def __init__(self):
        self.id = ''
        self.cis_division = ''
        self.bill_cycle = ''
        self.premise_id = ''
        self.setup_dt = datetime.datetime.now()
        self.db_connect = DBConnect.connection()

    def append(self):
        sql = "insert into account (id, setup_dt, cis_division, bill_cyc_cd, prem_id) " \
              "values ($1, $2::DATE, $3, $4, $5)"
        ps = self.db_connect.prepare(sql)
        ps(self.id, self.setup_dt, self.cis_division, self.bill_cycle, self.premise_id)

