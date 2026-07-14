#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Product Record
# Author: Om Roy
# Date: 14-07-2026
#--------------------------------------------

import os

class DuplicateProductError(Exception):
    """Raised when trying to register a Product ID that is already taken."""
    pass

class ProductNotFoundError(Exception):
    """Raised when a specified Product ID cannot be found in the database."""
    pass

class InvalidProductDataError(Exception):
    """Raised when product pricing, stock, or formatting violates business constraints."""
    pass


class ProductRegistry:
    FILE_NAME = "products.txt"

    @classmethod
    def add_and_save_product(cls, product_id, name, price, stock):
        # 1. Normalize input strings
        product_id = str(product_id).strip().upper()
        name = str(name).strip().title()

        # 2. Field Validations
        if not product_id or not name:
            raise InvalidProductDataError("All product entry fields (ID, Name, Price, Stock) are mandatory.")

        if not (product_id.startswith("PRD") and product_id[3:].isdigit()):
            raise InvalidProductDataError("Format Error: Product ID must start with 'PRD' followed by digits (e.g., PRD101).")

        # 3. Price & Stock Validations
        try:
            price = float(price)
            if price <= 0.0:
                raise ValueError()
        except ValueError:
            raise InvalidProductDataError("Pricing Error: Product price must be a valid number greater than $0.00.")

        try:
            stock = int(stock)
            if stock < 0:
                raise ValueError()
        except ValueError:
            raise InvalidProductDataError("Inventory Error: Stock quantity must be a non-negative whole integer.")

        # 4. Check for duplicate product IDs
        if cls._id_exists(product_id):
            raise DuplicateProductError(f"Database Conflict: Product with ID '{product_id}' is already cataloged.")

        # 5. Append direct to the flat-file database
        record_line = f"{product_id},{name},{price:.2f},{stock}\n"
        try:
            with open(cls.FILE_NAME, "a", encoding="utf-8") as file:
                file.write(record_line)
            print(f"\n[Success]: Product '{name}' cataloged under reference {product_id}.")
        except IOError as e:
            print(f"\n[File Access Error]: Unable to write record to disk. Details: {e}")

    @classmethod
    def display_all_products(cls):
        records = cls._load_records()
        if not records:
            print("\n[Database Status]: The product inventory ledger is currently empty.")
            return

        print("\n📦 === ACTIVE INVENTORY DIRECTORY ===")
        print(f"{'ID':<10} | {'Product Name':<22} | {'Price':<10} | {'Stock':<6} | {'Status'}")
        print("-" * 65)
        for pid, name, price_str, stock_str in records:
            price_val = float(price_str)
            stock_val = int(stock_str)
            
            # Compute live inventory statuses on the fly
            status = "OUT OF STOCK" if stock_val == 0 else "LOW STOCK" if stock_val <= 5 else "IN STOCK"
            print(f"{pid:<10} | {name:<22} | ${price_val:<9.2f} | {stock_val:<6} | {status}")
        print("=" * 65)

    @classmethod
    def search_product(cls, search_id):
        search_id = str(search_id).strip().upper()
        records = cls._load_records()

        for pid, name, price, stock in records:
            if pid == search_id:
                price_val = float(price)
                stock_val = int(stock)
                print(f"\n🎯 [Product Located: {search_id}]")
                print(f" -> Name           : {name}")
                print(f" -> Price          : ${price_val:,.2f}")
                print(f" -> Current Stock  : {stock_val} unit(s)")
                print(f" -> Stock Status   : {'ALERT: Restock Required' if stock_val <= 5 else 'Healthy Level'}")
                return
                
        raise ProductNotFoundError(f"Lookup Failed: Product ID '{search_id}' is not registered in inventory.")

    # --- Secure Internal Helpers ---
    @classmethod
    def _load_records(cls):
        """Safely loads flat-file database lines into memory-efficient lists."""
        if not os.path.exists(cls.FILE_NAME):
            return []

        parsed_records = []
        try:
            with open(cls.FILE_NAME, "r", encoding="utf-8") as file:
                for line in file:
                    cleaned = line.strip()
                    if cleaned:
                        parts = cleaned.split(",")
                        if len(parts) == 4:
                            parsed_records.append(parts)
        except IOError as e:
            print(f"[Critical System Error]: Cannot parse registry database. {e}")
            
        return parsed_records

    @classmethod
    def _id_exists(cls, check_id):
        records = cls._load_records()
        return any(pid == check_id for pid, *rest in records)


def main():
    print("=== Secure Product Inventory Hub ===")
    
    while True:
        print("\n" + "="*35)
        print("          INVENTORY MENU")
        print("="*35)
        print("1. Add & Save New Product")
        print("2. Display Live Inventory")
        print("3. Search Product by ID")
        print("4. Exit Inventory System")
        print("="*35)
        
        choice = input("Select operation (1-4): ").strip()

        try:
            if choice == "1":
                pid = input("Enter Product ID (e.g. PRD101): ")
                name = input("Enter Product Name: ")
                price = input("Enter Unit Price ($): ")
                stock = input("Enter Initial Stock Quantity: ")
                ProductRegistry.add_and_save_product(pid, name, price, stock)

            elif choice == "2":
                ProductRegistry.display_all_products()

            elif choice == "3":
                search_id = input("Enter Product ID to search: ")
                ProductRegistry.search_product(search_id)

            elif choice == "4":
                print("\nInventory session closed safely. Records committed to memory.")
                break
            else:
                print("\n[Input Error]: Select a valid option between 1 and 4.")

        except InvalidProductDataError as e:
            print(f"\n🚨 [Policy Exception]: {e}")
            
        except DuplicateProductError as e:
            print(f"\n🚨 [Database Conflict]: {e}")
            
        except ProductNotFoundError as e:
            print(f"\n🚨 [Lookup Query Missing]: {e}")
            
        except Exception as e:
            print(f"\n🚨 [Unexpected System Exception]: {e}")
            
        finally:
            print("\n" + "-"*40)


if __name__ == "__main__":
    main()