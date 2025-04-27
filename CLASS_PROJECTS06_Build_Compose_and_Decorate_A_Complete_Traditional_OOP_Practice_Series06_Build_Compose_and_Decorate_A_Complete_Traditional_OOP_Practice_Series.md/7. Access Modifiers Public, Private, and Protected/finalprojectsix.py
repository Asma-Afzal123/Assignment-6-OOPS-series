class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary    # Protected variable
        self.__ssn = ssn         # Private variable

# Create an object
emp = Employee("Ali", 50000, "123-45-6789")

# Access public variable
print("Name:", emp.name)  # Works fine

# Access protected variable
print("Salary:", emp._salary)  # Works, but not recommended directly

# Access private variable
try:
    print("SSN:", emp.__ssn)  # This will cause an error
except AttributeError as e:
    print("Error:", e)
