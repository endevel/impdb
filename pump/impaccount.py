import csv
from _csv import QUOTE_MINIMAL

import datetime

from dao.account import Account
from db.dbconnect import DBConnect


class Excel(csv.Dialect):
    """
    Настройки CSV-файла
    """

    delimiter = ';'
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\r\n'
    quoting = QUOTE_MINIMAL


class ImpAccount:
    """
    импорт лицевых счетов из CSV-файла
    """
    def __init__(self):
        self.__row_count = 0



    def read(self, file_name):
        fieldnames = ['ACCT_ID',
                      'BILL_CYC_CD',
                      'SETUP_DT',
                      'CURRENCY_CD',
                      'CIS_DIVISION',
                      'MAILING_PREM_ID']
        self.__row_coun = 0
        account = Account()

        with open(file_name) as csv_file:
            reader = csv.DictReader(csv_file, dialect=Excel)
            db = DBConnect.connection().xact()
            db.start()
            account.delete_all()

            for line in reader:

                account.id = line["ACCT_ID"]
                account.cis_division = line["CIS_DIVISION"]
                account.bill_cycle = line["BILL_CYC_CD"]
                account.premise_id = line["MAILING_PREM_ID"]
                account.setup_dt = datetime.datetime.strptime(line["SETUP_DT"], "%d.%m.%Y")
                account.append()

                self.__row_count += 1
                if self.__row_coun > 20000:
                    self.__row_count = 0
                    db.commit()
                    db.start()

            db.commit()

    @property
    def row_count(self):
        return self.__row_count
