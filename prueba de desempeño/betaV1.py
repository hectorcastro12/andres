from datetime import datetime
from typing import Dict, List, Tuple, Optional
import json


# Constants
MIN_STOCK = 0
MIN_PRICE = 0.01
MIN_QUANTITY = 1
MAX_DISCOUNT = 100.0


class BookstoreManager:
    """Main class for managing bookstore operations"""
    
    def __init__(self):
        """Initialize the bookstore with sample data"""
        self.inventory = {}
        self.sales = []
        self.customers = {}
        self._load_sample_data()
    
    def _load_sample_data(self) -> None:
        """Load initial sample data for testing"""
        sample_books = [
            {
                "id": "B001",
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "category": "Classic Literature",
                "price": 150.900,
                "stock": 25
            },
            {
                "id": "B002", 
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "category": "Classic Literature",
                "price": 145.500,
                "stock": 30
            },
            {
                "id": "B003",
                "title": "1984",
                "author": "George Orwell",
                "category": "Dystopian Fiction",
                "price": 130.250,
                "stock": 20
            },
            {
                "id": "B004",
                "title": "Animal Farm",
                "author": "George Orwell", 
                "category": "Political Satire",
                "price": 125.000,
                "stock": 15
            },
            {
                "id": "B005",
                "title": "Pride and Prejudice",
                "author": "Jane Austen",
                "category": "Romance",
                "price": 162.750,
                "stock": 18
            },
            {
                "id": "B006",
                "title": "The Principle",
                "author": "Antoine de saint-exupery",
                "category": "literature childrens ",
                "price": 58.000,
                "stock": 550
            }
        ]
        
        for book in sample_books:
            self.inventory[book["id"]] = book
        
    # ================== INVENTORY MANAGEMENT ==================

    def add_product(self, product_id: str, title: str, author: str, 
                   category: str, price: float, stock: int) -> bool:
        """
        Add a new product to inventory
        
        Args:
            product_id: Unique identifier for the product
            title: Book title
            author: Book author
            category: Book category
            price: Book price (must be positive)
            stock: Initial stock quantity (must be positive)
            
        Returns:
            bool: True if product added successfully, False otherwise
        """
        try:
            if not self._validate_product_data(product_id, title, author, 
                                             category, price, stock):
                return False
            
            if product_id in self.inventory:
                print(f"Error: Product ID {product_id} already exists!")
                return False
            
            self.inventory[product_id] = {
                "id": product_id,
                "title": title.strip(),
                "author": author.strip(),
                "category": category.strip(),
                "price": round(price, 2),
                "stock": stock
            }
            
            print(f"Product '{title}' added successfully!")
            return True
            
        except Exception as e:
            print(f"Error adding product: {str(e)}")
            return False

    def update_product(self, product_id: str, **kwargs) -> bool:
        """
        Update existing product information
        
        Args:
            product_id: Product ID to update
            **kwargs: Fields to update (title, author, category, price, stock)
            
        Returns:
            bool: True if updated successfully, False otherwise
        """
        try:
            if product_id not in self.inventory:
                print(f"Error: Product ID {product_id} not found!")
                return False
            
            product = self.inventory[product_id]
            
            for field, value in kwargs.items():
                if field in ["title", "author", "category"]:
                    if not isinstance(value, str) or not value.strip():
                        print(f"Error: {field} must be a non-empty string!")
                        return False
                    product[field] = value.strip()
                    
                elif field == "price":
                    if not isinstance(value, (int, float)) or value < MIN_PRICE:
                        print(f"Error: Price must be at least ${MIN_PRICE}!")
                        return False
                    product[field] = round(float(value), 2)
                    
                elif field == "stock":
                    if not isinstance(value, int) or value < MIN_STOCK:
                        print(f"Error: Stock must be at least {MIN_STOCK}!")
                        return False
                    product[field] = value
            
            print(f"Product {product_id} updated successfully!")
            return True
            
        except Exception as e:
            print(f"Error updating product: {str(e)}")
            return False

    def delete_product(self, product_id: str) -> bool:
        """
        Delete a product from inventory
        
        Args:
            product_id: Product ID to delete
            
        Returns:
            bool: True if deleted successfully, False otherwise
        """
        try:
            if product_id not in self.inventory:
                print(f"Error: Product ID {product_id} not found!")
                return False
            
            title = self.inventory[product_id]["title"]
            del self.inventory[product_id]
            print(f"Product '{title}' deleted successfully!")
            return True
            
        except Exception as e:
            print(f"Error deleting product: {str(e)}")
            return False

    def get_product(self, product_id: str) -> Optional[Dict]:
        """
        Retrieve product information
        
        Args:
            product_id: Product ID to retrieve
            
        Returns:
            Dict or None: Product information if found, None otherwise
        """
        return self.inventory.get(product_id)

    def list_products(self) -> None:
        """Display all products in inventory"""
        if not self.inventory:
            print("No products in inventory.")
            return
        
        print("\n" + "="*80)
        print("INVENTORY LISTING")
        print("="*80)
        print(f"{'ID':<8} {'Title':<25} {'Author':<20} {'Category':<15} {'Price':<8} {'Stock':<6}")
        print("-"*80)
        
        for product in self.inventory.values():
            print(f"{product['id']:<8} {product['title'][:24]:<25} "
                  f"{product['author'][:19]:<20} {product['category'][:14]:<15} "
                  f"${product['price']:<7.2f} {product['stock']:<6}")

    # ================== SALES MANAGEMENT ==================

    def register_sale(self, customer_id: str, product_id: str, 
                     quantity: int, custom_discount: float = 0.0) -> bool:
        """
        Register a new sale
        
        Args:
            customer_id: Customer identifier
            product_id: Product being sold
            quantity: Quantity to sell
            custom_discount: Additional discount percentage (0-100)
            
        Returns:
            bool: True if sale registered successfully, False otherwise
        """
        try:
            # Validate inputs
            if not self._validate_sale_data(customer_id, product_id, quantity, custom_discount):
                return False
            
            product = self.inventory[product_id]
            
            # Check stock availability
            if product["stock"] < quantity:
                print(f"Error: Insufficient stock! Available: {product['stock']}, "
                      f"Requested: {quantity}")
                return False
            
            # Calculate pricing
            unit_price = product["price"]
            gross_amount = unit_price * quantity
            
            # Apply discounts
            customer_discount = self.customers.get(customer_id, {}).get("discount_rate", 0.0)
            total_discount = min(customer_discount + custom_discount, MAX_DISCOUNT)
            discount_amount = gross_amount * (total_discount / 100)
            net_amount = gross_amount - discount_amount
            
            # Create sale record
            sale = {
                "sale_id": f"S{len(self.sales) + 1:04d}",
                "customer_id": customer_id,
                "product_id": product_id,
                "product_title": product["title"],
                "author": product["author"],
                "quantity": quantity,
                "unit_price": unit_price,
                "gross_amount": round(gross_amount, 2),
                "discount_rate": total_discount,
                "discount_amount": round(discount_amount, 2),
                "net_amount": round(net_amount, 2),
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Update inventory and record sale
            self.inventory[product_id]["stock"] -= quantity
            self.sales.append(sale)
            
            print(f"\nSale registered successfully!")
            print(f"Sale ID: {sale['sale_id']}")
            print(f"Product: {product['title']}")
            print(f"Quantity: {quantity}")
            print(f"Gross Amount: ${gross_amount:.2f}")
            print(f"Discount Applied: {total_discount:.1f}% (${discount_amount:.2f})")
            print(f"Net Amount: ${net_amount:.2f}")
            
            return True
            
        except Exception as e:
            print(f"Error registering sale: {str(e)}")
            return False

    def list_sales(self) -> None:
        """Display all sales records"""
        if not self.sales:
            print("No sales records found.")
            return
        
        print("\n" + "="*100)
        print("SALES RECORDS")
        print("="*100)
        print(f"{'Sale ID':<8} {'Customer':<10} {'Product':<25} {'Qty':<4} "
              f"{'Unit Price':<10} {'Discount':<8} {'Net Amount':<10} {'Date':<16}")
        print("-"*100)
        
        for sale in self.sales:
            print(f"{sale['sale_id']:<8} {sale['customer_id']:<10} "
                  f"{sale['product_title'][:24]:<25} {sale['quantity']:<4} "
                  f"${sale['unit_price']:<9.2f} {sale['discount_rate']:<7.1f}% "
                  f"${sale['net_amount']:<9.2f} {sale['date'][:16]:<16}")

    # ================== REPORTING MODULE ==================

    def get_top_selling_products(self, top_n: int = 3) -> List[Dict]:
        """
        Get top N selling products by quantity
        
        Args:
            top_n: Number of top products to return
            
        Returns:
            List[Dict]: Top selling products with sales data
        """
        # Aggregate sales by product using lambda functions
        product_sales = {}
        
        for sale in self.sales:
            product_id = sale["product_id"]
            if product_id not in product_sales:
                product_sales[product_id] = {
                    "product_id": product_id,
                    "title": sale["product_title"],
                    "author": sale["author"],
                    "total_quantity": 0,
                    "total_revenue": 0.0,
                    "sales_count": 0
                }
            
            product_sales[product_id]["total_quantity"] += sale["quantity"]
            product_sales[product_id]["total_revenue"] += sale["net_amount"]
            product_sales[product_id]["sales_count"] += 1
        
        # Sort by total quantity sold using lambda
        sorted_products = sorted(product_sales.values(), 
                               key=lambda x: x["total_quantity"], 
                               reverse=True)
        
        return sorted_products[:top_n]

    def get_sales_by_author(self) -> Dict[str, Dict]:
        """
        Generate sales report grouped by author
        
        Returns:
            Dict: Sales data grouped by author
        """
        author_sales = {}
        
        for sale in self.sales:
            author = sale["author"]
            if author not in author_sales:
                author_sales[author] = {
                    "total_books_sold": 0,
                    "gross_revenue": 0.0,
                    "net_revenue": 0.0,
                    "total_discount": 0.0,
                    "sales_count": 0
                }
            
            author_sales[author]["total_books_sold"] += sale["quantity"]
            author_sales[author]["gross_revenue"] += sale["gross_amount"]
            author_sales[author]["net_revenue"] += sale["net_amount"]
            author_sales[author]["total_discount"] += sale["discount_amount"]
            author_sales[author]["sales_count"] += 1
        
        return author_sales

    def calculate_financial_summary(self) -> Dict:
        """
        Calculate overall financial summary
        
        Returns:
            Dict: Financial summary with gross/net revenue and discounts
        """
        if not self.sales:
            return {
                "total_sales": 0,
                "gross_revenue": 0.0,
                "net_revenue": 0.0,
                "total_discounts": 0.0,
                "average_sale_value": 0.0
            }
        
        # Use lambda functions for calculations
        total_gross = sum(map(lambda sale: sale["gross_amount"], self.sales))
        total_net = sum(map(lambda sale: sale["net_amount"], self.sales))
        total_discounts = sum(map(lambda sale: sale["discount_amount"], self.sales))
        
        return {
            "total_sales": len(self.sales),
            "gross_revenue": round(total_gross, 2),
            "net_revenue": round(total_net, 2),
            "total_discounts": round(total_discounts, 2),
            "average_sale_value": round(total_net / len(self.sales), 2)
        }

    def display_comprehensive_report(self) -> None:
        """Display a comprehensive business report"""
        print("\n" + "="*80)
        print("COMPREHENSIVE BUSINESS REPORT")
        print("="*80)
        
        # Financial Summary
        financial_summary = self.calculate_financial_summary()
        print(f"\n📊 FINANCIAL SUMMARY")
        print(f"   Total Sales: {financial_summary['total_sales']}")
        print(f"   Gross Revenue: ${financial_summary['gross_revenue']:.2f}")
        print(f"   Net Revenue: ${financial_summary['net_revenue']:.2f}")
        print(f"   Total Discounts: ${financial_summary['total_discounts']:.2f}")
        print(f"   Average Sale Value: ${financial_summary['average_sale_value']:.2f}")
        
        # Top Selling Products
        print(f"\n 🏆 TOP 3 SELLING PRODUCTS")
        top_products = self.get_top_selling_products(3)
        if top_products:
            for i, product in enumerate(top_products, 1):
                print(f"   {i}. {product['title']} by {product['author']}")
                print(f"      Quantity Sold: {product['total_quantity']} | "
                      f"Revenue: ${product['total_revenue']:.2f} | "
                      f"Sales: {product['sales_count']}")
        else:
            print("   No sales data available")
        
        # Sales by Author
        print(f"\n👨‍💼 SALES BY AUTHOR")
        author_sales = self.get_sales_by_author()
        if author_sales:
            # Sort authors by net revenue
            sorted_authors = sorted(author_sales.items(), 
                                  key=lambda x: x[1]["net_revenue"], 
                                  reverse=True)
            
            for author, data in sorted_authors:
                print(f"   {author}:")
                print(f"      Books Sold: {data['total_books_sold']} | "
                      f"Net Revenue: ${data['net_revenue']:.2f} | "
                      f"Sales Count: {data['sales_count']}")
        else:
            print("   No sales data available")

    # ================== VALIDATION FUNCTIONS ==================

    def _validate_product_data(self, product_id: str, title: str, author: str,
                              category: str, price: float, stock: int) -> bool:
        """Validate product data before adding/updating"""
        if not product_id or not product_id.strip():
            print("Error: Product ID cannot be empty!")
            return False
        
        if not title or not title.strip():
            print("Error: Title cannot be empty!")
            return False
        
        if not author or not author.strip():
            print("Error: Author cannot be empty!")
            return False
        
        if not category or not category.strip():
            print("Error: Category cannot be empty!")
            return False
        
        if not isinstance(price, (int, float)) or price < MIN_PRICE:
            print(f"Error: Price must be at least ${MIN_PRICE}!")
            return False
        
        if not isinstance(stock, int) or stock < MIN_STOCK:
            print(f"Error: Stock must be at least {MIN_STOCK}!")
            return False
        
        return True

    def _validate_sale_data(self, customer_id: str, product_id: str,
                           quantity: int, custom_discount: float) -> bool:
        """Validate sale data before processing"""
        if not customer_id or not customer_id.strip():
            print("Error: Customer ID cannot be empty!")
            return False
        
        if product_id not in self.inventory:
            print(f"Error: Product ID {product_id} not found in inventory!")
            return False
        
        if not isinstance(quantity, int) or quantity < MIN_QUANTITY:
            print(f"Error: Quantity must be at least {MIN_QUANTITY}!")
            return False
        
        if not isinstance(custom_discount, (int, float)) or custom_discount < 0 or custom_discount > MAX_DISCOUNT:
            print(f"Error: Custom discount must be between 0 and {MAX_DISCOUNT}%!")
            return False
        
        return True


# ================== USER INTERFACE ==================

class BookstoreUI:
    """User interface for the bookstore management system"""
    
    def __init__(self):
        self.manager = BookstoreManager()
    
    def display_main_menu(self) -> None:
        """Display the main menu options"""
        print("\n" + "="*60)
        print("📚 BOOKSTORE MANAGEMENT SYSTEM")
        print("="*60)
        print("1. 📦 Inventory Management")
        print("2. 💰 Sales Management")
        print("3. 📊 Reports and Analytics")
        print("4. 👥 Customer Management")
        print("5. ❌ Exit")
        print("="*60)
    
    def display_inventory_menu(self) -> None:
        """Display inventory management menu"""
        print("\n📦 INVENTORY MANAGEMENT")
        print("1. Add New Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Product Details")
        print("5. List All Products")
        print("6. Back to Main Menu")
    
    def display_sales_menu(self) -> None:
        """Display sales management menu"""
        print("\n💰 SALES MANAGEMENT")
        print("1. Register New Sale")
        print("2. View All Sales")
        print("3. Back to Main Menu")
    
    def display_reports_menu(self) -> None:
        """Display reports menu"""
        print("\n📊 REPORTS AND ANALYTICS")
        print("1. Top 3 Selling Products")
        print("2. Sales by Author")
        print("3. Financial Summary")
        print("4. Comprehensive Report")
        print("5. Back to Main Menu")
    
    def get_user_input(self, prompt: str, input_type: type = str, 
                      min_value: float = None, max_value: float = None):
        """
        Get validated user input
        
        Args:
            prompt: Input prompt message
            input_type: Expected input type (str, int, float)
            min_value: Minimum allowed value for numeric inputs
            max_value: Maximum allowed value for numeric inputs
            
        Returns:
            Validated user input
        """
        while True:
            try:
                user_input = input(prompt).strip()
                
                if input_type == str:
                    if not user_input:
                        print("Error: Input cannot be empty!")
                        continue
                    return user_input
                
                elif input_type == int:
                    value = int(user_input)
                    if min_value is not None and value < min_value:
                        print(f"Error: Value must be at least {min_value}!")
                        continue
                    if max_value is not None and value > max_value:
                        print(f"Error: Value cannot exceed {max_value}!")
                        continue
                    return value
                
                elif input_type == float:
                    value = float(user_input)
                    if min_value is not None and value < min_value:
                        print(f"Error: Value must be at least {min_value}!")
                        continue
                    if max_value is not None and value > max_value:
                        print(f"Error: Value cannot exceed {max_value}!")
                        continue
                    return value
                
            except ValueError:
                print(f"Error: Please enter a valid {input_type.__name__}!")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                return None
    
    def handle_inventory_management(self) -> None:
        """Handle inventory management operations"""
        while True:
            self.display_inventory_menu()
            choice = self.get_user_input("Enter your choice (1-6): ", int, 1, 6)
            
            if choice is None:
                continue
            
            if choice == 1:
                self._add_product()
            elif choice == 2:
                self._update_product()
            elif choice == 3:
                self._delete_product()
            elif choice == 4:
                self._view_product()
            elif choice == 5:
                self.manager.list_products()
            elif choice == 6:
                break
    
    def handle_sales_management(self) -> None:
        """Handle sales management operations"""
        while True:
            self.display_sales_menu()
            choice = self.get_user_input("Enter your choice (1-3): ", int, 1, 3)
            
            if choice is None:
                continue
            
            if choice == 1:
                self._register_sale()
            elif choice == 2:
                self.manager.list_sales()
            elif choice == 3:
                break
    
    def handle_reports(self) -> None:
        """Handle reports and analytics"""
        while True:
            self.display_reports_menu()
            choice = self.get_user_input("Enter your choice (1-5): ", int, 1, 5)
            
            if choice is None:
                continue
            
            if choice == 1:
                self._show_top_products()
            elif choice == 2:
                self._show_sales_by_author()
            elif choice == 3:
                self._show_financial_summary()
            elif choice == 4:
                self.manager.display_comprehensive_report()
            elif choice == 5:
                break
    
    def _add_product(self) -> None:
        """Add a new product to inventory"""
        print("\n➕ ADD NEW PRODUCT")
        
        product_id = self.get_user_input("Product ID: ")
        if product_id is None:
            return
        
        title = self.get_user_input("Title: ")
        if title is None:
            return
        
        author = self.get_user_input("Author: ")
        if author is None:
            return
        
        category = self.get_user_input("Category: ")
        if category is None:
            return
        
        price = self.get_user_input("Price ($): ", float, MIN_PRICE)
        if price is None:
            return
        
        stock = self.get_user_input("Initial Stock: ", int, MIN_STOCK)
        if stock is None:
            return
        
        self.manager.add_product(product_id, title, author, category, price, stock)
    
    def _update_product(self) -> None:
        """Update an existing product"""
        print("\n✏️ UPDATE PRODUCT")
       
        product_id = self.get_user_input("Product ID to update: ")
        if product_id is None:
            return
        
        product = self.manager.get_product(product_id)
        if not product:
            print("⚠️ ERROR,PRODUCT NOT FOUND")
            return 
        
        print(f"\nCurrent product details:")
        print(f"Title: {product['title']}")
        print(f"Author: {product['author']}")
        print(f"Category: {product['category']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Stock: {product['stock']}")
        
        updates = {}
        
        # Get updates from user (empty input keeps current value)
        new_title = input(f"New title (current: {product['title']}) [Enter to skip]: ").strip()
        if new_title:
            updates["title"] = new_title
        
        new_author = input(f"New author (current: {product['author']}) [Enter to skip]: ").strip()
        if new_author:
            updates["author"] = new_author
        
        new_category = input(f"New category (current: {product['category']}) [Enter to skip]: ").strip()
        if new_category:
            updates["category"] = new_category
        
        new_price = input(f"New price (current: ${product['price']:.2f}) [Enter to skip]: ").strip()
        if new_price:
            try:
                updates["price"] = float(new_price)
            except ValueError:
                print("Invalid price format!")
                return
        
        new_stock = input(f"New stock (current: {product['stock']}) [Enter to skip]: ").strip()
        if new_stock:
            try:
                updates["stock"] = int(new_stock)
            except ValueError:
                print("Invalid stock format!")
                return
        
        if updates:
            self.manager.update_product(product_id, **updates)
        else:
            print("No updates provided.")
    
    def _delete_product(self) -> None:
        """Delete a product from inventory"""
        print("\n🗑️ DELETE PRODUCT")
        
        product_id = self.get_user_input("Product ID to delete: ")
        if product_id is None:
            return
        
        product = self.manager.get_product(product_id)
        if not product:
            print("⚠️ ERROR,PRODUCT NOT FOUND")
            return
        
        confirm = input(f"Are you sure you want to delete '{product['title']}'? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            self.manager.delete_product(product_id)
        else:
            print("Delete operation cancelled.")
    
    def _view_product(self) -> None:
        """View details of a specific product"""
        print("\n🔍 VIEW PRODUCT DETAILS")
        
        product_id = self.get_user_input("Product ID: ")
        if product_id is None:
            print("⚠️ ERROR,PRODUCT NOT FOUND")
            return
        
        product = self.manager.get_product(product_id)
        if product:
            print("\n" + "="*50)
            print("PRODUCT DETAILS")
            print("="*50)
            print(f"ID: {product['id']}")
            print(f"Title: {product['title']}")
            print(f"Author: {product['author']}")
            print(f"Category: {product['category']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("="*50)
    
    def _register_sale(self) -> None:
        """Register a new sale"""
        print("\n💰 REGISTER NEW SALE")
    
        
        customer_name = self.get_user_input("Customer Name: ")
        if customer_name is None:
            return
        
        # Show available products
        print("\nAvailable Products:")
        for product in self.manager.inventory.values():
            print(f"  {product['id']}: {product['title']} - Stock: {product['stock']} - ${product['price']:.2f}")
        
        product_id = self.get_user_input("Product ID: ")
        if product_id is None:
            return
        
        quantity = self.get_user_input("Quantity: ", int, MIN_QUANTITY)
        if quantity is None:
            return
        
        custom_discount = self.get_user_input("Additional discount % (0 for none): ", float, 0, MAX_DISCOUNT)
        if custom_discount is None:
            return
        
        self.manager.register_sale(customer_name, product_id, quantity, custom_discount)
    
    def _show_top_products(self) -> None:
        """Display top selling products"""
        print("\n🏆 TOP 3 SELLING PRODUCTS")
        top_products = self.manager.get_top_selling_products(3)
        if not top_products:
            print("No sales data available.")
            return
        
        print("="*70)
        print(f"{'Rank':<5} {'Title':<25} {'Author':<20} {'Qty Sold':<10} {'Revenue':<10}")
        print("-"*70)
        
        for i, product in enumerate(top_products, 1):
            print(f"{i:<5} {product['title'][:24]:<25} {product['author'][:19]:<20} "
                  f"{product['total_quantity']:<10} ${product['total_revenue']:<9.2f}")
    
    def _show_sales_by_author(self) -> None:
        """Display sales grouped by author"""
        print("\n👨‍💼 SALES BY AUTHOR")
        author_sales = self.manager.get_sales_by_author()
        
        if not author_sales:
            print("No sales data available.")
            return
        
        print("="*80)
        print(f"{'Author':<25} {'Books Sold':<12} {'Gross Revenue':<15} {'Net Revenue':<15} {'Sales':<8}")
        print("-"*80)
        
        # Sort by net revenue
        sorted_authors = sorted(author_sales.items(), 
                              key=lambda x: x[1]["net_revenue"], 
                              reverse=True)
        
        for author, data in sorted_authors:
            print(f"{author[:24]:<25} {data['total_books_sold']:<12} "
                  f"${data['gross_revenue']:<14.2f} ${data['net_revenue']:<14.2f} {data['sales_count']:<8}")
    
    def _show_financial_summary(self) -> None:
        """Display financial summary"""
        print("\n📊 FINANCIAL SUMMARY")
        summary = self.manager.calculate_financial_summary()
        
        print("="*50)
        print("FINANCIAL OVERVIEW")
        print("="*50)
        print(f"Total Sales Transactions: {summary['total_sales']}")
        print(f"Gross Revenue: ${summary['gross_revenue']:.2f}")
        print(f"Net Revenue: ${summary['net_revenue']:.2f}")
        print(f"Total Discounts Given: ${summary['total_discounts']:.2f}")
        print(f"Average Sale Value: ${summary['average_sale_value']:.2f}")
        
        if summary['total_sales'] > 0:
            discount_percentage = (summary['total_discounts'] / summary['gross_revenue']) * 100
            print(f"Overall Discount Rate: {discount_percentage:.1f}%")
    
    def run(self) -> None:
        """Main application loop"""
        print("Welcome to the Bookstore Management System!")
        print("Loading sample data...")
        
        while True:
            try:
                self.display_main_menu()
                choice = self.get_user_input("Enter your choice (1-5): ", int, 1, 5)
                
                if choice is None:
                    continue
                
                if choice == 1:
                    self.handle_inventory_management()
                elif choice == 2:
                    self.handle_sales_management()
                elif choice == 3:
                    self.handle_reports()
                elif choice == 4:
                    self._show_customers()
                elif choice == 5:
                    print("\nThank you for using the Bookstore Management System!")
                    print("Goodbye! 👋")
                    break
                
            except KeyboardInterrupt:
                print("\n\nApplication interrupted by user.")
                print("Thank you for using the Bookstore Management System!")
                break
            except Exception as e:
                print(f"\nAn unexpected error occurred: {str(e)}")
                print("Please try again or contact support.")
    
    def _show_customers(self) -> None:
        """Display customer information"""
        print("\n👥 CUSTOMER MANAGEMENT")
        print("="*60)
        print(f"{'Customer ID':<12} {'Name':<25} {'Discount Rate':<15}")
        print("-"*60)
        
        for cust_id, cust_data in self.manager.customers.items():
            print(f"{cust_id:<12} {cust_data['name']:<25} {cust_data['discount_rate']:<15.1f}%")
        
        print(f"\nTotal Customers: {len(self.manager.customers)}")


# ================== MAIN EXECUTION ==================

def main():
    """Main function to run the bookstore application"""
    try:
        app = BookstoreUI()
        app.run()
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        print("Application terminated.")


if __name__ == "__main__":
    main()