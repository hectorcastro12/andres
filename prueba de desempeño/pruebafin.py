# Inventory Management
inventory = {
    1: {'title': 'Book A', 'author': 'Author X', 'category': 'Fiction', 'price': 10.0, 'stock': 20},
    2: {'title': 'Book B', 'author': 'Author Y', 'category': 'Science', 'price': 15.0, 'stock': 30},
    3: {'title': 'Book C', 'author': 'Author Z', 'category': 'History', 'price': 12.0, 'stock': 25},
    4: {'title': 'Book D', 'author': 'Author X', 'category': 'Fiction', 'price': 8.0, 'stock': 10},
    5: {'title': 'Book E', 'author': 'Author Y', 'category': 'Science', 'price': 20.0, 'stock': 15}
}


# Register Product
def register_product(product_id, title, author, category, price, stock):
    if product_id in inventory:
        print("Product ID already exists.")
    else:
        inventory[product_id] = {'title': title, 'author': author, 'category': category, 'price': price, 'stock': stock}
        print(f"Product '{title}' has been registered.")

# View Product Details
def view_product(product_id):
    product = inventory.get(product_id)
    if product:
        print(f"Product: {product['title']}, Author: {product['author']}, Category: {product['category']}, Price: {product['price']}, Stock: {product['stock']}")
    else:
        print("Product not found.")

# Sales Management
sales = []

def register_sale(client, product_id, quantity, discount=0):
    if product_id not in inventory:
        print("Product not found.")
        return

    product = inventory[product_id]
    if product['stock'] < quantity:
        print("Not enough stock available.")
        return

    total_price = product['price'] * quantity
    total_discount = total_price * (discount / 100)
    final_price = total_price - total_discount

# Update stock
    product['stock'] -= quantity

    sale = {
        'client': client,
        'product_id': product_id,
        'quantity': quantity,
        'discount': discount,
        'final_price': final_price
    }

    sales.append(sale)
    print(f"Sale registered for {client} with {quantity} units of '{product['title']}'.")

# Calculate Gross and Net Income

def calculate_income():
    gross_income = sum(sale['final_price'] + sale['discount'] for sale in sales)
    net_income = sum(sale['final_price'] for sale in sales)
    print(f"Gross Income: {gross_income}, Net Income: {net_income}")
    
# Report Management
from collections import Counter

def top_selling_products():
    product_sales = Counter([sale['product_id'] for sale in sales])
    top_3 = product_sales.most_common(3)

    print("Top 3 Bestselling Products:")
    for product_id, count in top_3:
        product = inventory[product_id]
        print(f"Product: {product['title']}, Sold: {count}")

# Report Sales by Author
def sales_by_author():
    author_sales = {}
    for sale in sales:
        product = inventory[sale['product_id']]
        author = product['author']
        if author not in author_sales:
            author_sales[author] = 0
        author_sales[author] += sale['final_price']

    print("Sales by Author:")
    for author, total_sales in author_sales.items():
        print(f"Author: {author}, Total Sales: {total_sales}")
        
def main():
    while True:
        print("\n" + "="*60)
        print("📚 RIWI BOOKSTORE MANAGEMENT SYSTEM")
        print("="*60)
        print("\nMenu:")
        print("1. Register Product")
        print("2. View Product")
        print("3. 💰 Register Sale")
        print("4. 📊 View Reports")
        print("5. ❌ Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            product_id = int(input("Enter Product ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock: "))
            register_product(product_id, title, author, category, price, stock)
        elif choice == '2':
            product_id = int(input("Enter Product ID: "))
            view_product(product_id)
        elif choice == '3':
            client = input("Enter Client Name: ")
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter Quantity: "))
            discount = float(input("Enter Discount Percentage: "))
            register_sale(client, product_id, quantity, discount)
        elif choice == '4':
            print("1. Top Selling Products")
            print("2. Sales by Author")
            print("3. Gross and Net Income")
            report_choice = input("Enter report choice: ")
            if report_choice == '1':
                top_selling_products()
            elif report_choice == '2':
                sales_by_author()
            elif report_choice == '3':
                calculate_income()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            
# Handling invalid inputs
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    
            
if __name__ == "__main__":
    main()
    
    
    