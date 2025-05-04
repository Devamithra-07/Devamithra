products = {}
def add_product(pid, name, price, qty):
    products[pid] = {'name': name, 'price': price, 'quantity': qty}
def display_products():
    print("\nAvailable Products:")
    for pid, p in products.items():
        print(f"ID: {pid}, Name: {p['name']}, Price: ₹{p['price']}, Qty: {p['quantity']}")