import entities as et
class ProductService:
    products = {}

    @classmethod
    def add_product(cls, product):
        cls.products[product.product_id] = product

    @classmethod
    def remove_product(cls, product_id):
        if product_id in cls.products:
            del cls.products[product_id]

    @classmethod
    def get_all_products(cls):
        return cls.products.values()


class AdminService:
    admins = {}

    @classmethod
    def create_admin(cls, admin):
        cls.admins[admin.user_id] = admin

    @classmethod
    def get_all_admins(cls):
        return cls.admins.values()


class CustomerService:
    customers = {}

    @classmethod
    def create_customer(cls, customer):
        cls.customers[customer.user_id] = customer

    @classmethod
    def get_all_customers(cls):
        return cls.customers.values()

    @classmethod
    def get_customer_by_id(cls, customer_id):
        return cls.customers.get(customer_id)


class OrderService:
    orders = {}
    order_counter = 1

    @classmethod
    def place_order(cls, customer, products):
        order_id = cls.order_counter
        order = et.Order(order_id, customer, products)
        cls.orders[order_id] = order
        customer.orders.append(order)
        cls.order_counter += 1

        # Update product stock
        for product, quantity in products.items():
            product.stock_quantity -= quantity

        return order

    @classmethod
    def update_order_status(cls, order_id, status):
        if order_id in cls.orders:
            cls.orders[order_id].status = status

    @classmethod
    def get_all_orders(cls):
        return cls.orders.values()
