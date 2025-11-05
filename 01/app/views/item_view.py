from app.models.item import Item
from app.controllers.item_controller import ItemController
import streamlit


def items_to_dataframe(items: list["Item"]) -> None:
    items_data = [vars(item) for item in items]
    streamlit.dataframe(items_data)

def create_item_ui():
    description = streamlit.text_area("Description")
    quantity = streamlit.number_input("Quantity", min_value=0, step=1)

    if streamlit.button("Submit"):
        item_controller = ItemController()
        data = {"description": description, "quantity": quantity}
        item = item_controller.create(**data)
        streamlit.success("Item created successfully!")
        items_to_dataframe([item])

def read_items_ui():
    item_controller = ItemController()
    items = item_controller.list_all()
    items_to_dataframe(items)

def main():
    menu_option = streamlit.sidebar.selectbox(
        "Select an operation:",
        ["Create", "Read"]
    )

    match menu_option:
        case "Create": create_item_ui()
        case "Read": read_items_ui()
