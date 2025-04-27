# Engine class
class Engine:
    def start(self):
        print("Engine started!")

# Car class
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car ke andar Engine ka object

    def start_car(self):
        self.engine.start()  # Car ke zariye Engine ka method call karna

# Example usage
engine1 = Engine()
car1 = Car(engine1)

car1.start_car()
