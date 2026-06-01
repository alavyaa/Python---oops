# class Student:
#     name = "aaru"
#     roll = 200
#     branch = "abd"
# obj = Student()
# print(Student.name, obj.roll)

# class A:
#     a = 10
#     b = 20
# obj = A()
# obj.a = 101
# obj.b = 104
# obj.c = 1444
# print(obj.a, obj.c)

# class Company:
#     ceo = 'Alavya'
#     branch = 'Bangalore'
#     project = 'App'
#     project_type = 'Development'
#     email = 'abc@email.com'
#     def __init__ (self, salary, number, position):
#         self.salary = salary
#         self.number = number
#         self.position = position
# emp1 = Company(23000, 2343567808, "leader")
# emp2 = Company(239090, 6677689464, "Developer")
# emp3 = Company(54000, 567687987, "Hacker")
# emp1.project = 'website'
# emp2.project = 'webapp'
# emp1.email = 'emp1@email.com'
# emp2.email = 'emp2@email.com'
# emp3.email = 'emp3@email.com'
# print(emp1.branch, emp1.ceo, emp1.email, emp1.project, emp1.project_type, emp1.salary, emp1.number, emp1.position)
# print(emp2.branch, emp2.ceo, emp2.email, emp2.project, emp2.project_type, emp2.salary, emp2.number, emp2.position)
# print(emp3.branch, emp3.ceo, emp3.email, emp3.project, emp3.project_type, emp3.salary, emp3.number, emp3.position)

class A:
    a= 10
    def __init__(self):
        print(self.a)
obj= A()