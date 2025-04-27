# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of Person
        self.subject = subject

# Example usage
teacher1 = Teacher("Mr. Smith", "Mathematics")
print(f"Name: {teacher1.name}")
print(f"Subject: {teacher1.subject}")
