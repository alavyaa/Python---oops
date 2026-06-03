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

# class A:
#     a= 10
#     def __init__(self):
#         print(self.a)
# obj= A()
# print(obj)
# print(A())

#~ create a class called employee requirements => usee init to initialise emp_name, emp_id, emp_sal,  create object method to display thee result

# class Employee:
#     def __init__(self, emp_name, emp_id, emp_sal):
#         self.emp_name = emp_name
#         self.emp_id = emp_id
#         self.emp_sal = emp_sal
#     def display(self):
#         print(self.emp_name, self.emp_id, self.emp_sal)
# emp1 = Employee("alavya", 23, 3900000000000000)
# emp2 = Employee("Abs", 34, 56)
# emp1.display()
# emp2.display()

#~ create a class called mobile requirements brand price using obj members, 2 different objects , display both object details separately
#add a class member called category = electronics

# class Mobile:
#     category = 'electronics'
#     def __init__ (self, brand, price):
#         self.brand = brand
#         self.price = price
#     def display (self):
#         print(self.brand)
#         print(self.category)
#         print(self.price)
        
# m1 = Mobile("Realme", 13000)
# m2 = Mobile("Oppo", 9000)
# m1.display()
# m2.display()

# class A:
#     def __init__(self):
#         print('Hi')
#     def __init__(self):
#         print('Hello')
# a = A()     
# output : Hello 
# cause it overwrites
    
    
# class A:
#     def display(self):
#         print("Hello")
#     def display(self, a):
#         print(a)
# a = A()
# a.display(10)

# it pverwrites if the names are same 

# make a online shopping application 
# create a class called shopping  Cart 
# requirements -> class members : platfrom name 
# constructor should initialize cust name , product list total amount
# object method = add method , remove product , update platform name , display

class ShoppingCart:
    platform_name = "Amazon"
    
    def __init__ (self, customer_name, product_list, total_amount):
        self.customer_name = customer_name
        self.product_list = product_list
        self.total_amount = total_amount
    
    def add(self):
        self.product_list.append(input("Enter the product name: "))
        self.price = int(input("Enter price of the product: "))
        self.total_amount += self.price
    
    @classmethod
    def update(cls):
        cls.platform_name = "Flipkart"
    
    def remove(self):
        self.product_name = input("Enter the product to be removed: ")
        if self.product_name in self.product_list:
            self.product_list.remove(self.product_name)
            self.pricee = int(input("Enter the price of the product to be removed: "))
            self.total_amount -= self.pricee
        else:
            print("Product not in list.")
    
    def display(self):
        print("Platform: ", ShoppingCart.platform_name)
        print("customer name : " , self.customer_name)
        print("Product List: ", self.product_list)
        print("Total Amount: ", self.total_amount)
        
cust1 = ShoppingCart("Alavya", ['apple', 'banana'], 89)
cust1.display()
cust1.add()
cust1.display()
cust1.remove()
cust1.display()
cust1.update()
cust1.display()

'''
to combine two sets we use union method
'''
