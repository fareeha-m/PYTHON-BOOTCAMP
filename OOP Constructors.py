#Constructor for Object Oriented Programming in Python
# __init__

class Employee():
    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name= name
        self.bond = bond


    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of employee is{self.name}. Their salary is {self.salary}. Their bond is {self.bond}")

e1 = Employee(90000, "John", 2)
print(e1.get_info())

