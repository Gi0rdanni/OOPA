from app.models.item import Item
from app.controllers.item_controller import ItemController
import streamlit


def items_to_dataframe(items: list["Item"]) -> None:
    items_data = [vars(item) for item in items]
    streamlit.dataframe(items_data)

def main():
    menu_option = streamlit.sidebar.selectbox(
        "Select an operation:",
        ["Create", "Read"]
    )

    if menu_option == "Create":
        description = streamlit.text_area("Description")
        quantity = streamlit.number_input("Quantitty", min_value = 0, step = 1)

        if streamlit.button("Submit"):
            item_controller = ItemController()
            data = {"description": description, "quantity": quantity}
            item = item_controller.create(**data)
            items_to_dataframe([item])

    elif menu_option == "Read":
        item_controller = ItemController()
        items = item_controller.list_all()
        items_to_dataframe(items)