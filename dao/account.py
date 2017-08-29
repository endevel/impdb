import datetime

from db.dbconnect import DBConnect


class Account:
    """
    Лицевой счет
    """
    def __init__(self):
        self.id = ''
        self.cis_division = ''
        self.bill_cycle = ''
        self.premise_id = ''
        self.setup_dt = datetime.datetime.now()
        self.db_connect = DBConnect.connection()
        self.__sql_append = "insert into account (id, setup_dt, cis_division, bill_cyc_cd, prem_id) " \
              "values ($1, $2::DATE, $3, $4, $5)"
        self.__sql_delete_all = "delete from account"

        self.__ps_append = self.db_connect.prepare(self.__sql_append)
        self.__ps_delete_all = self.db_connect.prepare(self.__sql_delete_all)

    def append(self):
        self.__ps_append(self.id, self.setup_dt, self.cis_division, self.bill_cycle, self.premise_id)

    def delete_all(self):
        self.__ps_delete_all()


