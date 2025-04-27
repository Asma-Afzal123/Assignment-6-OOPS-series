class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):        # public method
        print(self.brand, "is starting...")

# Example usage
car1 = Car("Toyota")

# Accessing public variable and method from outside the class
print("Car Brand:", car1.brand)
car1.start()
