class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def __repr__(self):
        return f"Product [productId={self.product_id}, name={self.name}, price={self.price}, stockQuantity={self.stock_quantity}]"


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

    def __repr__(self):
        return f"User ID: {self.user_id}, Username: {self.username}, Email: {self.email}, Address: {self.address}"


class Admin(User):
    def __init__(self, user_id, username, email):
        super().__init__(user_id, username, email)


class Order:
    def __init__(self, order_id, customer, products):
        self.order_id = order_id
        self.customer = customer
        self.products = products  # {product: quantity}
        self.status = "Pending"

    def __repr__(self):
        return f"Order ID: {self.order_id}, Status: {self.status}, Products: {[(p.name, q) for p, q in self.products.items()]}"

