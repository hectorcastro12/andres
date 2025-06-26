# 📚 RIWI BOOKSTORE MANAGEMENT SYSTEM 

# BY ANDRES CASTRO

## Description

This system allows you to manage inventory, sales, and reports for a bookstore. It includes functions to register products, view product details, register sales, and generate sales and author reports.

---

## Code Structure

### Inventory

The inventory is a dictionary where each key is the product ID and the value is another dictionary with the book's data:

```python
inventory = {
    1: {'title': 'Book A', 'author': 'Author X', 'category': 'Fiction', 'price': 10.0, 'stock': 20},
    ...
}
```

---

### Main Functions

- **register_product(product_id, title, author, category, price, stock):**  
  Registers a new product in the inventory if the ID does not already exist.

- **view_product(product_id):**  
  Displays the details of a product by its ID.

- **register_sale(client, product_id, quantity, discount=0):**  
  Registers a sale, updates the stock, and stores the sale information.

- **calculate_income():**  
  Calculates and prints the gross and net income from all sales.

- **top_selling_products():**  
  Shows the top 3 best-selling products.

- **sales_by_author():**  
  Shows the total sales grouped by author.

- **get_positive_integer(prompt):**  
  Asks the user for a positive integer, validating the input.

---

### Main Flow (`main()`)

Displays an interactive menu to:
- Register products
- View products
- Register sales
- View reports (top-selling products, sales by author, income)
- Exit the system

---

## Running the Program

Run the main file to start the system:

```bash
python pruebafin.py
```

---

## Notes

- The system validates numeric inputs to avoid errors.
- Reports use the `collections.Counter` library to count sales.
- Inventory and sales are kept in memory (no file or database persistence).

---