# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older!"):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError()  # Agar age < 18 ho to exception raise hota hai
    else:
        print("Age is valid!")  # Agar age valid hai to message

# Example usage with try-except
try:
    age = int(input("Enter your age: "))  # User se age lene ka tareeqa
    check_age(age)  # Age ko check karo
except InvalidAgeError as e:
    print(f"Error: {e}")  # Agar exception raise ho to isko handle karenge
