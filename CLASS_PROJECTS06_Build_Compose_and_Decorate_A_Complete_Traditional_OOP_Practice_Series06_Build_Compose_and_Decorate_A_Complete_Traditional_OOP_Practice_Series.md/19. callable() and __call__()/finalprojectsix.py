class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Factor set karte hain

    def __call__(self, num):
        return num * self.factor  # Input ko factor se multiply karte hain

# Example usage
multiplier = Multiplier(5)  # Factor 5 set kiya
print(callable(multiplier))  # Check if object is callable (True hoga)

# Calling the object like a function
result = multiplier(10)  # 10 ko multiply karega factor 5 se
print(result)  # Output: 50
