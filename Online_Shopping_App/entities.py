import uuid
class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Product [ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock_quantity}]"


class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email


class Customer(User):
    def __init__(self, user_id, username, email, address):
        super().__init__(user_id, username, email)
        self.address = address
        self.shopping_cart = {}
        self.orders = []

    def __str__(self):
        return f"Customer [ID: {self.user_id}, Username: {self.username}, Email: {self.email}, Address: {self.address}]"


class Admin(User):
    def __init__(self, user_id, username, email):
        super().__init__(user_id, username, email)


class Order:
    def __init__(self, customer, items):
        self.order_id = str(uuid.uuid4())[:8]
        self.customer = customer
        self.items = items
        self.status = "Pending"

    def __str__(self):
        item_details = "\n  ".join([f"{p.name}, Quantity: {q}" for p, q in self.items.items()])
        return f"Order [ID: {self.order_id}, Customer: {self.customer.username}, Status: {self.status}]\n  {item_details}"

