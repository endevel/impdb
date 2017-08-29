import postgresql


class DBConnect:
    """
    Соединение с PostgreSQL
    """
    db = None

    @classmethod
    def connection(self):
        if DBConnect.db is None:
            DBConnect.db = postgresql.open(user = 'postgres',
                                           password = 'DBPartizan',
                                           database = 'ccb',
                                           host = 'localhost', port = 5432)
        return DBConnect.db
