# Employee class
class Employee:
    def __init__(self, name):
        self.name = name

# Department class
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: just a reference to Employee

    def show_details(self):
        print(f"Department: {self.department_name}")
        print(f"Employee: {self.employee.name}")

# Example usage
emp1 = Employee("Alice")  
dept1 = Department("HR", emp1)  

dept1.show_details()
