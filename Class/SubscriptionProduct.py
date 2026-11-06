from Class.Product import Product

class SubscriptionProduct(Product):

    def __init__(self, product_id, name, price, stock, type, size):
        super().__init__(product_id, name, price, stock, type, size)
        self.__size = size

    def get_fulfillment_info(self):
        return f"Product is a subscription service."

    def display_information(self):
        return super().display_information()