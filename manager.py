from products import *
from inventory import *
from sales import *
from reports import *
from validations import *

def print_menu():
    print("""
=================================
       COMPUTER STORE SYSTEM
=================================

1. Products Management
2. Inventory Management
3. Sales Management
4. Reports
5. Exit
""")

def get_input(input_type) -> int:
    user_choice = input("Choose an option: ").strip()
    return validate_manager_input(user_choice, input_type)

def menu_manager(products):
    user_choice = 0
    sales = []
    while user_choice != 5:
        try:
            print_menu()
            user_choice = get_input("menu")
            if user_choice == 1:
                products_manager(products)
            elif user_choice == 2:
                inventory_manager(products)
            elif user_choice == 3:
                sales_manager(products, sales)
            elif user_choice == 4:
                reports_manager(sales)
            elif user_choice == 5:
                print("bye!🙋")
        except ValueError as e:
            print(f"Error: {e}")

def products_manager(products):
    user_choice = 0
    while user_choice != 6:
        try:
            print_products_menu()
            user_choice = get_input("products menu")
            if user_choice == 1:
                products = add_products(products)
            elif user_choice == 2:
                show_active_products(products)
            elif user_choice == 3:
                search_product(products)
            elif user_choice == 4:
                update_product(products)
            elif user_choice == 5:
                delete_product(products)
        except ValueError as e:
            print(f"Error: {e}")

def inventory_manager(products):
    user_choice = 0
    while user_choice != 7:
        try:
            print_inventory_menu()
            user_choice = get_input("inventory menu")
            if user_choice == 1:
                show_active_products(products)            
            elif user_choice == 2:
                search_product(products)
            elif user_choice == 3:
                change_stock(products)
            elif user_choice == 4:
                change_stock(products)
            elif user_choice == 5:
                show_status(products, "sold out")
            elif user_choice == 6:
                show_status(products, "low stock")
        except ValueError as e:
            print(f"Error: {e}")

def sales_manager(products, sales):
    user_choice = 0
    while user_choice != 2:
        try:
            print_sales_menu()
            user_choice = get_input("sales menu")
            if user_choice == 1:
                new_sale_manager(products, sales)
        except ValueError as e:
            print(f"Error: {e}")

def new_sale_manager(products: list, sales: list):
    """Run one sale session: build a cart, then complete or cancel it."""
    print("\n=========== NEW SALE ===========")
    cart = []
    discount_percent = 0.0
    choice = ""
    while choice != 6:
        show_cart(cart, discount_percent)
        print_cart_menu()
        try:
            choice = get_input("cart menu")
            if choice == 1:
                handle_add_item(cart, products)
            elif choice == 2:
                handle_update_item(cart, products)
            elif choice == 3:
                handle_remove_item(cart, products)
            elif choice == 4:
                print("Discount percent (0-100): ")
                discount_percent = get_input("discount")
            elif choice == 5:
                sale = complete_sale(cart, products, sales, discount_percent)
                print_sale_summary(sale)
                print("Sale completed successfully!")
                return
            elif choice == 6:
                print("Sale cancelled.")
        except ValueError as error:
            print(f"Error: {error}")

def reports_manager(sales):
    user_choice = 0
    while user_choice != 7:
        try:
            print_reports_menu()
            user_choice = get_input("reports menu")
            if user_choice == 1:
                show_total_sales(sales)
            elif user_choice == 2:
                show_total_revenue(sales)
            elif user_choice == 3:
                show_best_selling(sales)
            elif user_choice == 4:
                show_average_sale(sales)
            elif user_choice == 5:
                sales_history(sales)
            elif user_choice == 6:
                show_category_statistics(sales)
        except ValueError as e:
            print(f"Error: {e}")


def create_initial_products() -> list:
    return [
        {"id": 1, "name": "Gaming Mouse", "category": "Gaming", "price": 150.0, "stock": 20, "active": True},
        {"id": 2, "name": "Mechanical Keyboard", "category": "Accessories", "price": 350.0, "stock": 10, "active": True},
        {"id": 3, "name": "Gaming Headset", "category": "Gaming", "price": 280.0, "stock": 4, "active": True},
        {"id": 4, "name": "RGB Mouse Pad XL", "category": "Gaming", "price": 89.9, "stock": 35, "active": True},
        {"id": 5, "name": "Gaming Chair Pro", "category": "Gaming", "price": 1199.0, "stock": 3, "active": True},
        {"id": 6, "name": "Wireless Mouse", "category": "Accessories", "price": 99.0, "stock": 42, "active": True},
        {"id": 7, "name": "USB-C Hub 7-in-1", "category": "Accessories", "price": 179.0, "stock": 0, "active": True},
        {"id": 8, "name": "Laptop Stand Aluminum", "category": "Accessories", "price": 129.0, "stock": 18, "active": True},
        {"id": 9, "name": "Webcam Full HD 1080p", "category": "Accessories", "price": 249.0, "stock": 2, "active": True},
        {"id": 10, "name": "Gaming Laptop 15.6\"", "category": "Computers", "price": 5899.0, "stock": 5, "active": True},
        {"id": 11, "name": "Ultrabook 14\"", "category": "Computers", "price": 4290.0, "stock": 7, "active": True},
        {"id": 12, "name": "Mini PC i5", "category": "Computers", "price": 2390.0, "stock": 0, "active": True},
        {"id": 13, "name": "Graphics Card RTX 4060", "category": "Components", "price": 1490.0, "stock": 6, "active": True},
        {"id": 14, "name": "SSD NVMe 1TB", "category": "Components", "price": 329.0, "stock": 25, "active": True},
        {"id": 15, "name": "RAM DDR5 16GB", "category": "Components", "price": 219.0, "stock": 1, "active": True},
        {"id": 16, "name": "Power Supply 750W", "category": "Components", "price": 459.0, "stock": 9, "active": True},
        {"id": 17, "name": "Monitor 27\" 144Hz", "category": "Monitors", "price": 1290.0, "stock": 8, "active": True},
        {"id": 18, "name": "Monitor 24\" Full HD", "category": "Monitors", "price": 599.0, "stock": 12, "active": True},
        {"id": 19, "name": "Bluetooth Speaker", "category": "Audio", "price": 199.0, "stock": 15, "active": True},
        {"id": 20, "name": "Studio Headphones", "category": "Audio", "price": 549.0, "stock": 0, "active": True},
        {"id": 21, "name": "WiFi 6 Router", "category": "Networking", "price": 399.0, "stock": 11, "active": True},
        {"id": 22, "name": "Network Switch 8-Port", "category": "Networking", "price": 149.0, "stock": 3, "active": True},
        {"id": 23, "name": "External HDD 2TB", "category": "Storage", "price": 389.0, "stock": 14, "active": True},
        {"id": 24, "name": "USB Flash Drive 64GB", "category": "Storage", "price": 39.9, "stock": 60, "active": True},
        {"id": 25, "name": "VGA Cable 1.5m", "category": "Accessories", "price": 19.9, "stock": 30, "active": False},
        {"id": 26, "name": "DVD Writer External", "category": "Storage", "price": 149.0, "stock": 0, "active": False},
    ]

