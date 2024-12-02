import entities as et,services as sr
# Menu-Driven Interface
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Products")
        print("4. View Orders")
        print("5. Update Order Status")
        print("6. Exit")

        choice = int(input("Choose an option: "))
        if choice == 1:
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            stock = int(input("Enter Stock Quantity: "))
            sr.ProductService.add_product(et.Product(product_id, name, price, stock))
            print("Product added successfully!")
        elif choice == 2:
            product_id = int(input("Enter Product ID to remove: "))
            sr.ProductService.remove_product(product_id)
            print("Product removed successfully!")
        elif choice == 3:
            products = sr.ProductService.get_all_products()
            print("Products:")
            for product in products:
                print(product)
        elif choice == 4:
            orders = sr.OrderService.get_all_orders()
            print("Orders:")
            for order in orders:
                print(order)
        elif choice == 5:
            order_id = int(input("Enter Order ID: "))
            status = input("Enter new status (Completed/Delivered/Cancelled): ")
            sr.OrderService.update_order_status(order_id, status)
            print("Order status updated successfully!")
        elif choice == 6:
            break


def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. Create Customer")
        print("2. View Customers")
        print("3. Place Order")
        print("4. View Orders")
        print("5. View Products")
        print("6. Exit")

        choice = int(input("Choose an option: "))
        if choice == 1:
            user_id = int(input("Enter User ID: "))
            username = input("Enter Username: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            sr.CustomerService.create_customer(et.Customer(user_id, username, email, address))
            print("Customer created successfully!")
        elif choice == 2:
            customers = sr.CustomerService.get_all_customers()
            print("Customers:")
            for customer in customers:
                print(customer)
        elif choice == 3:
            customer_id = int(input("Enter Customer ID: "))
            customer = sr.CustomerService.get_customer_by_id(customer_id)
            if not customer:
                print("Customer not found!")
                continue

            products = {}
            while True:
                product_id = int(input("Enter Product ID to add to order (or -1 to complete): "))
                if product_id == -1:
                    break
                quantity = int(input("Enter quantity: "))
                product = sr.ProductService.products.get(product_id)
                if product and product.stock_quantity >= quantity:
                    products[product] = quantity
                else:
                    print("Invalid product ID or insufficient stock.")

            order = sr.OrderService.place_order(customer, products)
            print(f"Order placed successfully! Order ID: {order.order_id}")
        elif choice == 4:
            customer_id = int(input("Enter Customer ID: "))
            customer = sr.CustomerService.get_customer_by_id(customer_id)
            if customer:
                print("Orders:")
                for order in customer.orders:
                    print(order)
            else:
                print("Customer not found!")
        elif choice == 5:
            products = sr.ProductService.get_all_products()
            print("Products:")
            for product in products:
                print(product)
        elif choice == 6:
            break


def main():
    while True:
        print("\nMain Menu:")
        print("1. Admin Menu")
        print("2. Customer Menu")
        print("3. Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            admin_menu()
        elif choice == 2:
            customer_menu()
        elif choice == 3:
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
