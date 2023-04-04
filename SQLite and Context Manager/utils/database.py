from typing import List, Tuple

from utils.database_connection import DatabaseConnection

Book = Tuple[int, str, str, int]


# The -> (arrow) is used to annotate the return value for a function in Python 3.0 or later.
# It does not affect the program but is intend to be consumed by other users or libraries as documentation for the function.


def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        # SQLite automatically makes `integer primary key` row auto-incrementing (see link in further reading)
        cursor.execute('CREATE TABLE books (id integer primary key, name text, author text, read integer default 0)')


def get_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        #cusrosr
        books = cursor.fetchall()
    return books


def insert_book(name: str, author: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        #using paranthesis avoid sql injection attacks
        cursor.execute('INSERT INTO books (name, author) VALUES (?, ?)', (name, author))


def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))
