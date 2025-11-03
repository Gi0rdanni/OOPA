import sys
sys.dont_write_bytecode = True

import streamlit
from app.daos.item_dao import ItemDAO
from app.views.item_view import main as main_view


def main():
    dao = ItemDAO()
    dao.start()
    main_view()

if __name__ == "__main__":
    main()