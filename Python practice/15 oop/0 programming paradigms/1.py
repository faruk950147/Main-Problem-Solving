class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print(self.name, self.age, self.salary)
    
if __name__ == "__main__":
    emp = Employee("Faruk", 21, 1000)
    print(getattr(emp, "name"))
    print(hasattr(emp, "age"))
    print(setattr(emp, "salary", 2000))
    print(delattr(emp, "salary"))
    emp.display()
    