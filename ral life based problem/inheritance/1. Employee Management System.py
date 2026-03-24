class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")


class Intern(Employee):
    def __init__(self, name, emp_id, salary, duration):
        super().__init__(name, emp_id, salary)
        self.duration = duration

    def display_details(self):
        super().display_details()
        print(f"Internship Duration: {self.duration}")


# 🔎 Example usage
m = Manager("Alice", 101, 90000, "HR")
d = Developer("Bob", 102, 80000, "Python")
i = Intern("Charlie", 103, 20000, "6 months")

print("Manager Details:")
m.display_details()
print("\nDeveloper Details:")
d.display_details()
print("\nIntern Details:")
i.display_details()