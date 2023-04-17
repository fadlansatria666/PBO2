# Nama  : Fadlan Satria Triswanto
# Kelas : D3
# NIM   : 210510001

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):

        super().display_info()
        print("Department:", self.department)


class Engineer(Employee):

    def __init__(self, name, salary, skill):
        super().__init__(name, salary)
        self.skill = skill

    def display_info(self):
        super().display_info()
        print("Skill:", self.skill)


employee1 = Employee("Son", 5000)
manager1 = Manager("Chanwook", 7000, "Marketing")
engineer1 = Engineer("Rommy", 6000, "Python")


employee1.display_info()  
manager1.display_info()  
engineer1.display_info()  