from validations import *
from products import id_maker


def print_sales_menu():
    print("""
----------- SALES MANAGEMENT -----------

1. New Sale
2. Back to Main Menu
""")    

def print_cart_menu():
    print(f""" 
1. Add product to cart
2. Update product quantity
3. Remove product from cart
4. Set discount
5. Complete Sale
6. Cancel Sale
""")

def show_cart(cart: list, discount_percent: float):
    print("\n--- Cart ---")
    if not cart:
        print("(empty)")
        return
    for item in cart:
        print(f"[{item['product_id']}] {item['name']} {item['quantity']} x {item['unit_price']:.2f} = {(item['total']):.2f}")
    subtotal = calculate_subtotal(cart)
    print(f"Subtotal: {subtotal:.2f}, Discount: {discount_percent:g}%, Total: {(subtotal - calculate_discount(subtotal, discount_percent)):.2f}")

def print_sale_summary(sale: dict):
    print(f"=========== SALE #{sale['id']} SUMMARY ===========")
    for item in sale["items"]:
        print(f"""
{item['name']} {item['quantity']} x {(item['unit_price']):.2f} = {(item['total']):.2f}""")
    print(f"""
------------------------------------
Subtotal: {(sale['subtotal']):.2f}
Discount: {(sale['discount']):.2f}
Total: {(sale['total']):.2f}
====================================""")

# 1
def add_to_cart(cart: list, products: list, product_id: int, quantity: int):
    """Add units of a product to the cart (merging with an existing line).""" 
    product = validate_id(product_id, products)
    item = get_cart_item(cart, product_id)
    already_in_cart = item["quantity"] if item else 0
    validate_sellable(product, quantity + already_in_cart)
    if item:
        set_item_quantity(item, already_in_cart + quantity)
    else:
        cart.append({"product_id": product["id"], "name": product["name"],
                     "category": product["category"], "quantity": quantity,
                     "unit_price": product["price"],
                     "total": round(quantity * product["price"], 2)})

def handle_add_item(cart: list, products: list):
    product = ask_existing_product(products)
    quantity = int(validate_product_input(input("Quantity: ").strip(), "quantity"))
    if product is None:
        return
    add_to_cart(cart, products, product["id"], quantity)
    print("Added to cart!")

def ask_existing_product(products):
    product = validate_id(input("Enter product ID: ").strip(), products)
    if product is None:
        print("Product not found!")
    return product

# 2
def update_cart_quantity(cart: list, products: list, product_id: int, quantity: int):
    item = get_cart_item(cart, product_id)
    if item is None:
        raise ValueError("Product is not in the cart")
    validate_sellable(validate_id(product_id, products), quantity)
    set_item_quantity(item, quantity)

def handle_update_item(cart: list, products: list):
    product = ask_existing_product(products)
    if product is None:
        return
    quantity = int(validate_product_input(input("New quantity: ").strip(), "quantity"))
    update_cart_quantity(cart, products, product["id"], quantity)
    print("Quantity updated!")

# 3
def remove_from_cart(cart: list, product_id: int):
    item = get_cart_item(cart, product_id)
    if item is None:
        raise ValueError("Product is not in the cart")
    cart.remove(item)

def handle_remove_item(cart: list, products: list):
    product = ask_existing_product(products)
    if product is None:
        return
    remove_from_cart(cart, product["id"])
    print("Removed from cart!")

# 4
def get_discount(input_type) -> int:
    return validate_manager_input(input("Discount percent (0-100): ").strip(), input_type)

# 5
def complete_sale(cart: list, products: list, sales: list, discount_percent: float = 0.0) -> dict:
    validate_cart(cart, products)
    subtotal = calculate_subtotal(cart)
    discount = calculate_discount(subtotal, discount_percent)
    for item in cart:
        validate_id(item["product_id"], products)["stock"] -= item["quantity"]
    sale = {"id": id_maker(sales), "items": [dict(item) for item in cart],
            "subtotal": subtotal, "discount": discount,
            "total": round(subtotal - discount, 2)}
    sales.append(sale)
    return sale

# helpers
def calculate_subtotal(cart: list) -> float:
    return round(sum(item["total"] for item in cart), 2)

def calculate_discount(subtotal: float, discount_percent: float) -> float:
    return round(subtotal * discount_percent / 100, 2)


def get_cart_item(cart: list, product_id: int):
    for item in cart:
        if item["product_id"] == product_id:
            return item
    return None

def set_item_quantity(item: dict, quantity: int):
    item["quantity"] = quantity
    item["total"] = round(quantity * item["unit_price"], 2)
