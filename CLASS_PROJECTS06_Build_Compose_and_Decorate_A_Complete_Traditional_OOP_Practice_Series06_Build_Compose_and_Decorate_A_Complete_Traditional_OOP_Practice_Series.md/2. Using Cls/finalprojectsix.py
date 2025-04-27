class Counter:
    count = 0  # class variable to keep track of objects

    def __init__(self):
        Counter.count += 1  # increment count whenever a new object is created

    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.count)

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.show_count()
