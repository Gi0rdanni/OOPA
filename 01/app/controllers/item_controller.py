from app.models.item import Item
from app.daos.item_dao import ItemDAO


class ItemController():
    @staticmethod
    def create(**data) -> Item:
        dao = ItemDAO()
        item = Item(**data)
        return dao.insert(item)
    
    @staticmethod
    def list_all() -> list[Item]:
        dao = ItemDAO()
        return dao.list_all()