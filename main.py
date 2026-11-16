from manager import menu_manager, create_initial_products

def main():
    products = create_initial_products()
    menu_manager(products)

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("\nbye!🙋")


