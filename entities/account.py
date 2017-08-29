import datetime


class Account:
    """
    Лицевой счет
    """
    def __init__(self):
        self.__id = ""
        self.__premise_id = ""
        self.__cis_division = ""
        self.__bill_cycle = ""
        self.__setup_dt = datetime.datetime.now()

