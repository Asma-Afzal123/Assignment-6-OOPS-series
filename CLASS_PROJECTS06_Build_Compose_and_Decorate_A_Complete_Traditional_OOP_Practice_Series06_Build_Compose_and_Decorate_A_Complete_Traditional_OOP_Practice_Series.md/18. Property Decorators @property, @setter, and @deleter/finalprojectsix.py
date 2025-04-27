class Product:
    def __init__(self, price):
        self._price = price  # Private attribute _price

    @property
    def price(self):
        return self._price  # Price ko read karte waqt yeh method call hoga

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value  # Price ko update karte waqt yeh method call hoga

    @price.deleter
    def price(self):
        print("Deleting the price!")
        del self._price  # Price ko delete karte waqt yeh method call hoga

# Example usage
product = Product(100)
print(product.price)  # @property use hoga (getter)

product.price = 150  # @price.setter use hoga (setter)
print(product.price)

product.price = -50  # Negative price set karte waqt @setter warning dega

del product.price  # @price.deleter use hoga (deleter)
