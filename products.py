from validations import validate_product_input, validate_category, validate_id


def print_products_menu():
    print("""
--------- PRODUCTS MANAGEMENT ---------

1. Add product
2. Display all products
3. Search product
4. Update product
5. Delete product
6. Back to Main Menu
""")

# 1
def input_product_to_add(products):
    product_name = validate_product_input(input("Enter product name: ").strip(), "name")
    category = validate_product_input(input("Enter category: ").strip(), "category")
    price = validate_product_input(input("Enter price: ").strip(), "price")
    quantity = validate_product_input(input("Enter quantity: ").strip(), "quantity")
    return (product_name, category, price, quantity)

def id_maker(items) -> int:
    if not items:
        return 1
    return max(item["id"] for item in items) + 1
    
def add_products(products) -> list:
    product_id = id_maker(products)
    product_name, category, price, quantity = input_product_to_add(products)
    products.append({"id": product_id, "name": product_name, "category": category, "price": float(price), "stock": int(quantity), "active": True})
    return products   

# 2
def show_active_products(products):
    active_products = get_active_products(products)
    print(active_products)

def get_active_products(products) -> list:
    return list(filter(lambda a: a["active"] == True, products))

# 3    
def search_product(products):
    search_menu()
    user_choice, search_value = ask_product_details(3)
    search_list = []
    product = validate_id(search_value, products)
    if user_choice == "1" and product:
        print_search_results(product)
    elif user_choice in ("2", "3"):
        for product in products:
            if user_choice == "2" and (product["name"][:len(search_value)]).lower() == search_value.lower():
                search_list.append(product)
            elif user_choice == "3" and product["category"].strip() == search_value:
                search_list.append(product)
        print_search_results(search_list)
    else:
        print_try_again()

def ask_product_details(options) ->tuple:
    user_choice = input(f"Chose from 1 to {options}: ").strip()
    value = input("Enter value: ").strip()
    return (user_choice, value)

def print_search_results(result):
    print(result)

def print_try_again():
    print("try again!")

def search_menu():
    print(f"""
Chose what to update:
1. ID
2. name
3. category""")   

# 4
def update_product(products):
    product_id = enter_id(products)
    update_print()
    user_choice, update_value = ask_product_details(4)
    for product in products:
        if validate_id(product_id, products) == product:
            if user_choice == "1" and validate_product_input(update_value, "name"):
                product["name"] = update_value
            elif user_choice == "2" and validate_product_input(update_value, "category"):
                product["category"] = update_value
            elif user_choice == "3" and validate_product_input(update_value, "price"):
                product["price"] = float(update_value)
            elif user_choice == "4" and validate_product_input(update_value, "active"):
                product["active"] = (update_value == "True")
            else:
                print_try_again()
            break

def enter_id(products):
    product_id = input("Enter product ID: ").strip()
    if validate_id(product_id, products):
        return product_id
    return False

def update_print():
    print(f"""
Chose what to update:
1. name
2. category
3. price
4. active""")

# 5
def delete_product(products):
    product_id = ask_to_delete()
    if product_id:
        for product in products:
            if product_id == str(product["id"]):
                products.remove(product)
                delete_print()
                break

def ask_to_delete() -> (bool, str):
    product_id = input("Enter product ID: ").strip()
    is_delete = input("Do you want to delete this product? (y/n): ").strip().lower()
    if is_delete == "y":
        return product_id
    return False

def delete_print():
    print("product deleted!")





