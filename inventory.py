from products import show_active_products, get_active_products, enter_id
from validations import validate_product_input, validate_stock, validate_id


def print_inventory_menu():
    print("""
--------- INVENTORY MANAGEMENT ---------

1. Display all products in stock
2. Search Product in stock
3. Add units to stock
4. Subtract units from stock
5. Display sold out products
6. Display low stock products
7. Back to Main Menu
""")

def show_status(products, status):   
    print(get_status(products, status))

def get_status(products, status):
    active_products = get_active_products(products)
    LOW_STOCK = 5
    if status == "sold out":
        return list(filter(lambda a: a["stock"] == 0, active_products))
    else:
        return list(filter(lambda a: 0 < a["stock"] <= LOW_STOCK, active_products))

def change_stock(products):
    product_id = enter_id(products)
    for product in products:
        if validate_id(product_id, products) == product:
            product["stock"] = validate_stock(product["stock"], enter_stock())
            break

def enter_stock():
    stock_to_change = validate_product_input(input("How many do you want to change? ").strip(), "stock")
    return int(stock_to_change)


