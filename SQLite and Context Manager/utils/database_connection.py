import sqlite3


class DatabaseConnection:
    def __init__(self, host: str):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        #will make connection object and return it
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type, exc_val, exc_tb  contains the error info if block get executed with error

        self.connection.commit()
        self.connection.close()
