def validate_manager_input(user_choice: str, input_type: str) -> int:
    if not validate_positive_integer(user_choice):
        raise ValueError("Choice is not a positive integer")
    val = int(user_choice)
    if input_type == "menu":
        if not val in range(1, 6):
            raise ValueError("Must be between 1 and 5")
    elif input_type == "products menu"  or input_type == "cart menu":
        if not val in range(1, 7):
            raise ValueError("Must be between 1 and 6")
    elif input_type == "inventory menu" or input_type == "reports menu":
        if not val in range(1, 8):
            raise ValueError("Must be between 1 and 7")
    elif input_type == "sale menu":
        if not val in range(1, 3):
            raise ValueError("Must be between 1 and 2")
    elif input_type == "discount":
        if not val in range(stop=101):
            raise ValueError("Must be between 1 and 100")
    return val

def validate_product_input(user_choice: str, input_type: str):
    if input_type == "name" and not user_choice:
        raise ValueError("name cannot be empty!")
    elif input_type == "category" and not validate_category(user_choice):
        raise ValueError("category not found!")
    elif input_type == "price" and not validate_positive(user_choice):
        raise ValueError("price must be positive!")
    elif input_type == "quantity" and not validate_positive_integer(user_choice):
        raise ValueError("quantity must be a positive integer!")
    elif input_type == "active" and user_choice not in ("True", "False"):
        raise ValueError("must be 'True' or 'False'!")
    elif input_type == "stock" and not validate_integer(user_choice):
        raise ValueError("must be an integer!")
    return user_choice

def validate_category(user_category) -> bool:
    CATEGORIES = ["Gaming", "Accessories", "Computers", "Components", "Monitors", 
"Audio", "Networking", "Storage"]
    for category in categories:
        if user_category.lower() == category.lower():
            return True
    return False

def validate_integer(user_input: str) -> bool:
    try:
        int(user_input)
        return True
    except ValueError:
        return False

def validate_positive_integer(user_choice) -> bool:
    if not user_choice.isdigit():
        return False
    return validate_positive(user_choice)

def validate_positive(user_choice) -> bool:
    try:  
        val = float(user_choice)
        return val > 0
    except ValueError:
        return False

def validate_id(product_id, products):
    for product in products:
        if str(product["id"]) == str(product_id):
            return product
    return None

def validate_stock(stock, stock_to_change):
    updated_stock = stock + stock_to_change
    if updated_stock >= 0:
        return  updated_stock
    else:
        return stock

def validate_sellable(product, quantity: int):
    if product is None:
        raise ValueError("Product does not exist")
    if not product["active"]:
        raise ValueError("Product is not active")
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    if quantity > product["stock"]:
        raise ValueError(f"Only {product['stock']} units of '{product['name']}' in stock")

def validate_cart(cart: list, products: list):
    if not cart:
        raise ValueError("Cannot complete a sale with an empty cart")
    for item in cart:
        validate_sellable(validate_id(item["product_id"], products), item["quantity"])
