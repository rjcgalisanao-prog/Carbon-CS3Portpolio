class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def sell_item(store, item_name, quantity):
    for item in store:
        if item.name == item_name:
            if item.quantity >= quantity:
                item.quantity -= quantity
                total_price = item.price * quantity
                print(f"Sold {quantity} of {item.name} for ${total_price:.2f}.")
            else:
                print(f"Not enough {item.name} in stock. Available: {item.quantity}.")
            return
    print(f"{item_name} not found in the store.")

def restock_item(store, item_name, quantity):
    for item in store:
        if item.name == item_name:
            item.quantity += quantity
            print(f"Restocked {quantity} of {item.name}. New quantity: {item.quantity}.")
            return
    print(f"{item_name} not found in the store.")

def display_info():
    for item in store:
        print(f"Item: {item.name}, Price: ${item.price:.2f}, Quantity: {item.quantity}")

item1 = product("Soda", 20, 10)

item1.display_info()
item1.sell_item(3)
item1.display_info()
item1.restock_item(5)
item1.display_info()