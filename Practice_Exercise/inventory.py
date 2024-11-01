'''
Create an `Item` class that represents an item in a store. Each item has the following attributes:

- `name`: The name of the item.
- `price`: The price of the item.
- `quantity`: The quantity of the item in stock.

Create an `Inventory` class that manages a collection of items. The `Inventory` class should have the following:

1. **Attributes**:
    - A list of `Item` objects.
2. **Methods**:
    - `add_item(item)`: Adds an `Item` object to the inventory.
    - `remove_item(item_name)`: Removes an item from the inventory by name. If the item does not exist, print an error message.
    - `update_quantity(item_name, quantity)`: Updates the quantity of the item with the given name. If the item does not exist, print an error message.
    - `display_inventory()`: Displays all items in the inventory with their names, prices, and quantities.

Simulate adding, removing, and updating items in an inventory system.
'''


class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quanity = quantity
    
class Inventory:
    def __init__(self):
        self.items = []
    
    def add_item(self,item):
        self.items.append(item)
        print(f"Item '{item.name}' added in the inventory ")
    
    def remove_item(self,item_name):
        for item in self.items:
            if item_name == item_name:
                self.items.remove(item)
                print(f"Item '{item_name}' removed from the inventory")
                return
            print(f"Item {item_name} not found in inventory")

    def update_quantity(self,item_name,quantity):
        for item in self.items:
            if item_name == item_name:
                self.quantity == quantity
                print(f"Item {item_name} quantity uodated to {quantity}")
                return
            print("item not found")
    
    def display_inventory(self):
        if not self.items:
            print("Inventory empty")
        else:
            for item in self.items:
                print(f"Item {item_name} price {item.price} quantity {item.quantity}")

inventory = Inventory()

inventory.add_item(Item("sar",12,12))
inventory.remove_item("as")
inventory.display_inventory()