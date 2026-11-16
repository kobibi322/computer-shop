from sales import print_sale_summary

def print_reports_menu():
    print("""
---------- REPORTS MANAGEMENT ----------

1. Total Sales
2. Total Revenue
3. Best Selling Products
4. Average Sale
5. Sales History
6. Category Statistics
7. Back
""")

# 1
def get_total_sales(sales: list) -> int:
    return len(sales)

def show_total_sales(sales: list):
    print(f"Total sales: {get_total_sales(sales)}")

# 2
def get_total_revenue(sales: list) -> float:
    return round(sum(sale["total"] for sale in sales), 2)

def show_total_revenue(sales: list):
    print(f"Total revenue: {get_total_revenue(sales):.2f}")

# 3
def get_best_selling_products(sales: list, limit: int = 5) -> list:
    totals = {}
    for sale in sales:
        for item in sale["items"]:
            product_id = item["product_id"]
            if product_id not in totals:
                totals[product_id] = {"name": item["name"], "units": 0}
            totals[product_id]["units"] += item["quantity"]
    ranked = sorted(totals.values(), key=lambda entry: entry["units"], reverse=True)
    return [(entry["name"], entry["units"]) for entry in ranked[:limit]]

def show_best_selling(sales: list):
    best = get_best_selling_products(sales)
    if not best:
        print("No sales yet.")
    for rank, (name, units) in enumerate(best, start=1):
        print(f"{rank}. {name} - {units} units") 

# 4
def get_average_sale(sales: list) -> float:
    return round(get_total_revenue(sales) / len(sales), 2) if sales else 0.0

def show_average_sale(sales: list):
    print(f"Average sale: {get_average_sale(sales):.2f}")

# 5
def sales_history(sales: list):
    if not sales:
        print("No sales yet.")
    for sale in sales:
        print_sale_summary(sale)

# 6
def get_category_statistics(sales: list) -> dict:
    """Return {category: units sold}."""
    stats = {}
    for sale in sales:
        for item in sale["items"]:
            stats[item["category"]] = stats.get(item["category"], 0) + item["quantity"]
    return stats

def show_category_statistics(sales: list):
    stats = get_category_statistics(sales)
    if not stats:
        print("No sales yet.")
        return
    for category, units in stats.items():
        print(f"{category}: {units} units")