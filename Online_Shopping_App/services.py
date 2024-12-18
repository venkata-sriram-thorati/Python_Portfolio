import uuid
import entities as et
class ProductService:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def get_all_products(self):
        return list(self.products.values())


class OrderService:
    def __init__(self):
        self.orders = []

    def place_order(self, customer, items):
        order = et.Order(customer, items)
        self.orders.append(order)
        return order

    def update_order_status(self, order_id, status):
        for order in self.orders:
            if order.order_id == order_id:
                order.status = status
                return order
        return None