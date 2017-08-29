import csv
from _csv import QUOTE_MINIMAL

class Excel(csv.Dialect):
    delimiter = ';'
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\r\n'
    quoting = QUOTE_MINIMAL

class ImpAccount:
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
        with open(file_name) as csv_file:
            reader = csv.DictReader(csv_file, dialect=Excel)

            for line in reader:
                self.__id = line["ACCT_ID"]
                self.__row_count += 1

    @property
    def row_count(self):
        return self.__row_count
