# 1
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

obj = Animal()
obj2 = Dog()
obj.eat()
obj2.bark()


# 2
class Employee:
    employee_name = "Alavya"
    salary = 43323456
class Developer(Employee):
    programming_lang = "Python"
    
obj = Developer()
print(obj.employee_name, obj.programming_lang, obj.salary)


# 3
class Resume10th:
    def __init__(self, name, age, school10, percentage10):
        self.name = name
        self.age = age
        self.school10 = school10
        self.percentage10 = percentage10

    def display_10th(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("10th School:", self.school10)
        print("10th Percentage:", self.percentage10)
class Resume12th(Resume10th):
    def __init__(self, name, age, school10, percentage10,
                 school12, percentage12):
        super().__init__(name, age, school10, percentage10)
        self.school12 = school12
        self.percentage12 = percentage12

    def display_12th(self):
        self.display_10th()
        print("12th School:", self.school12)
        print("12th Percentage:", self.percentage12)
class ResumeDegree(Resume12th):
    def __init__(self, name, age, school10, percentage10,
                 school12, percentage12,
                 degree_college, degree_percentage):
        super().__init__(name, age, school10, percentage10,
                         school12, percentage12)
        self.degree_college = degree_college
        self.degree_percentage = degree_percentage

    def display_degree(self):
        self.display_12th()
        print("College:", self.degree_college)
        print("Degree Percentage:", self.degree_percentage)
student12 = Resume12th(
    "Shini", 20,
    "ABC Public School", 92,
    "XYZ Senior Secondary School", 88
)

student12.display_12th()

print("\n" + "=" * 40 + "\n")

studentDegree = ResumeDegree(
    "Alavya", 21,
    "ABC Public School", 95,
    "XYZ Senior Secondary School", 90,
    "Chandigarh University", 85
)

studentDegree.display_degree()




sum1 = 0
sum2 = 0
sum3 = 0
for i in range(1, 26):
    sum1 += i
for i in range(26, 51):
    sum2 += i
for i in range(51, 76):
    sum3 += i
print(sum1, sum2, sum3)
