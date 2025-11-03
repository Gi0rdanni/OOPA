from typing import Optional
from pathlib import Path
import sqlite3

from app.models.item import Item

APP_PATH = Path(__file__).parents[1].absolute()
DB_PATH = APP_PATH / "db" / "item.db"


class ItemDAO:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __open(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def __close(self):
        if self.connection:
            self.connection.close()
        self.connection = None
        self.cursor = None

    def __commit(self):
        self.connection.commit()

    def __execute(self, command: str, parameters: tuple = ()):
        self.cursor.execute(command, parameters)

    def start(self):
        self.__open()
        self.__execute('''
            CREATE TABLE IF NOT EXISTS item (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                quantity INTEGER
            )''')
        self.__commit()
        self.__close()

    def insert(self, item: Item) -> Optional[Item]:
        self.__open()
        self.__execute('''
            INSERT INTO item (description, quantity)
            VALUES (?, ?)
            ''', (item.description, item.quantity))
        item.id = self.cursor.lastrowid
        self.__commit()
        self.__close()
        return item

    def list_all(self) -> list[Item]:
        self.__open()
        self.__execute("SELECT * FROM item")
        rows = self.cursor.fetchall()
        self.__close()
        return [Item(**dict(row)) for row in rows]