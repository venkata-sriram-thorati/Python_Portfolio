import uuid
import entities as et,services as se

# Menu-Driven Interface
def admin_menu(product_service, order_service):
    while True:
        print("\nAdmin Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Products")
        print("4. View Orders")
        print("5. Update Order Status")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            stock_quantity = int(input("Enter Stock Quantity: "))
            product_service.add_product(et.Product(product_id, name, price, stock_quantity))
            print("Product added successfully!")
        elif choice == "2":
            product_id = input("Enter Product ID to remove: ")
            product_service.remove_product(product_id)
            print("Product removed successfully!")
        elif choice == "3":
            print("Products:")
            for product in product_service.get_all_products():
                print(product)
        elif choice == "4":
            print("Orders:")
            for order in order_service.orders:
                print(order)
        elif choice == "5":
            order_id = input("Enter Order ID: ")
            status = input("Enter new status (Pending/Completed/Delivered/Cancelled): ")
            order = order_service.update_order_status(order_id, status)
            if order:
                print(f"Order {order_id} updated to {status}.")
            else:
                print("Order not found.")
        elif choice == "6":
            break


def customer_menu(product_service, order_service, customers):
    while True:
        print("\nCustomer Menu:")
        print("1. Create Customer")
        print("2. View Customers")
        print("3. Place Order")
        print("4. View Orders")
        print("5. View Products")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            user_id = input("Enter User ID: ")
            username = input("Enter Username: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            customers[user_id] = et.Customer(user_id, username, email, address)
            print("Customer created successfully!")
        elif choice == "2":
            print("Customers:")
            for customer in customers.values():
                print(customer)
        elif choice == "3":
            customer_id = input("Enter Customer ID: ")
            customer = customers.get(customer_id)
            if not customer:
                print("Customer not found!")
                continue

            items = {}
            while True:
                product_id = input("Enter Product ID to add (or -1 to complete): ")
                if product_id == "-1":
                    break
                product = product_service.products.get(product_id)
                if product:
                    quantity = int(input(f"Enter quantity for {product.name}: "))
                    items[product] = quantity
                else:
                    print("Product not found!")
            order = order_service.place_order(customer, items)
            print(f"Order placed successfully! Order ID: {order.order_id}")
        elif choice == "4":
            customer_id = input("Enter Customer ID: ")
            customer = customers.get(customer_id)
            if not customer:
                print("Customer not found!")
                continue

            print("Orders:")
            for order in order_service.orders:
                if order.customer == customer:
                    print(order)
        elif choice == "5":
            print("Products:")
            for product in product_service.get_all_products():
                print(product)
        elif choice == "6":
            break


# Main Driver Code
def main():
    product_service = se.ProductService()
    order_service = se.OrderService()
    customers = {}

    while True:
        print("\nMain Menu:")
        print("1. Admin Menu")
        print("2. Customer Menu")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            admin_menu(product_service, order_service)
        elif choice == "2":
            customer_menu(product_service, order_service, customers)
        elif choice == "3":
            break


if __name__ == "__main__":
    main()
