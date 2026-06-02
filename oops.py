'''
OOPS => Object Oriented Programming System  or Structure
Class => Blueprint of Object
Object => Instance of Class

Advantages of OOPS
1. Code Reusability => We can reuse the code by creating objects of the class.
2. Data Hiding => We can hide the data from the outside world by using access specifiers.
3. Modularity => The code is organized into classes and objects, making it easier to manage and maintain.
4. Flexibility => OOPS allows for easy modification and extension of the code without affecting the entire system.

OOPS is a way  of programming where we have to create class and object 

class  
it is a blueprint

Syntax:-
class ClassName:
    class body
    
object
it is a real world entity that is created from a class
it is an instance or example of a class

syntax:-
obj_name = ClassName(arguments) or obj_name = ClassName()
here arguments are ooptional  
it creates an object when we call the class,
the object address should be stored in variable

Types of class:
1. inbuilt class
2. user defined class

1. Inbuilt Class:- 
all the datatypes are inbuilt class because they are pre defined.

2. user defined class:-
the classes which are defined or created by the user are the user defined classes


Example:

class Creation:
    a = 10 
    b = 20
demo = Creation()
print(type(demo))

Output: <class '__main__.Creation'>

__main__   is representing that class is created by the user or we can sayy that it is a user defined class.

Memory Allocation:

main space    |    Method Area
------------------------------
in tldr

Whenever we want to access the values from the class or object we have to use a suntax.

For class :- ClassName.var
For Object :- obj_name.var

Example:

class Creation:
    a = 10 
    b = 20
demo1 = Creation()
demo2 = Creation()
print(Creation.a, Creation.b)     ~ by using class
print(demo1.a, demo1.b)           ~ by using object
print(demo2.a, demo2.b)

~ Actual Program
WAP for banking system 

class Bank:
    bname = "SBI"
    location = "Bangalore"
    Manager = "Aditya"

cus1 = Bank()
cus2 = Bank()

print(Bank.bname, Bank.location, Bank.Manager)
print(cus1.bname, cus1.location, cus1.Manager)
print(cus2.bname, cus2.location, cus2.Manager)

Bank.location = "Chandigarh"                            ~ modifying class var (will affect everyone)

print(Bank.bname, Bank.location, Bank.Manager)
print(cus1.bname, cus1.location, cus1.Manager)
print(cus2.bname, cus2.location, cus2.Manager)

cus1.location = "Jharkhand"                             ~  modifying object 1 var (will affect  object 1 only no one else)

print(Bank.bname, Bank.location, Bank.Manager)
print(cus1.bname, cus1.location, cus1.Manager)
print(cus2.bname, cus2.location, cus2.Manager)

cus2.location = "Mumbai"                                ~ modifying object 2 var (will affect object 2 only no one else)

print(Bank.bname, Bank.location, Bank.Manager)
print(cus1.bname, cus1.location, cus1.Manager)
print(cus2.bname, cus2.location, cus2.Manager)

Conclusion:

Modification done with respect to class will affect all the objects
Reason: Objects are instance/copy of the class

Modification done  with respect to object will not affect the class and other objects
Reason: class are not depending on objects 


States/  Property
The data or information stored inside a class or an object is known as property of the class/object.
OR
The variable or functionalities storing inside the class are called states.

There are two types of states:-
1. Generic State/ Class State/ Static State
2. Object State/ Specific State

~ these are the properties which will be common for every object.

1. Generic State
the properties which are common for all the objects are termed as generic state.

Example:
class School:
    sname = "CGC"
    loc = "Chandigarh"
    principal = "Aditya"
    time = "12:30 to 4:30"
st1 = School()
st2 = School()
print(School.sname, School.loc, School.principal, School.time)
print(st1.sname, st1.loc, st1.principal, st1.time)
print(st2.sname, st2.loc, st2.principal, st2.time)

2. Object state or Specific state
The properties which will we create outside the class after the class creation is called as specific or object state.

Example:

class School:
    sname = "DAV"
    loc = "Bangalore"
    principal = "Joseph Vijay"
    time = "9:00am to 12:00pm"
st1 = School()
st1.name = "Shaurya"
st1.id = 23
st1.age = 20
st1.bg = "AB+"

st2 = School()
st2.name = "Raj"
st2.id = 24
st2.age = 18
st2.bg = "O+"
print(st1.name, st1.id, st1.age, st1.bg, st1.sname, st1.loc, st1.principal, st1.time)
print(st2.name, st2.id, st2.age, st2.bg, st2.sname, st2.loc, st2.principal, st2.time)

Difference Betweek method and function.

Functions which we declare inside a class are known as methods.
If we declare the function is known as functions.

Function:
def add():
    print("Hi")
    
Method:
class Demo:
    def show():
        print("hi")
        
show() is a method.

Constructor/ __init__ / initialisation

Constructor is a special method .
It runs automatically when an object is created.
It is used to initialise the members of the object.
No need of calling the method, by default it will execute when we create an object.
self is the mandatory argument to pass for the __init__ method .
We can pass arguments in the object creation only if there is __init__ method present inside the class.
__init__ is the constructor method in python.

For __init__ method, passing self is mandatory to store the address of the object.

Syntax:
class Cname:
    Block of code
    def __init__(self, var1, var2, ....varn):
        self.var1 = var1
        self.var2 = var2
        self.......
        .
        .
        .
        self.varn = varn
    
obj_name = Cname(val1, val2, .....valn)


class School:
    sname = "Carmel"
    location = "Bangalore"
    principal = "Alavya"
    timing = "9:00 to 12:00"
    def __init__(self, name, id, age, bg):
        self.name = name
        self.id = id
        self.age = age
        self.bg = bg

st1 = School("Akanksha", 16, 24, "B+")
print(st1.name, st1.id, st1.age, st1.bg, st1.sname, st1.location, st1.principal, st1.timing)

st2 = School("Alavya", 17, 20, "AB+")
print(st2.name, st2.id, st2.age, st2.bg, st2.sname, st2.location, st2.principal, st2.timing)
  

~ wap to create a company having 3 class members and 1 object with 4 object member.

  class Company:
    cname = "Capgemini"
    location = "Bangalore"
    HR = "Aditya"
    def __init__(self, name, empid, age, department):
        self.name = name
        self.empid = empid
        self.age = age
        self.department = department

emp1 = Company("Akanksha", 16, 24, "Python Trainer")
print(emp1.name, emp1.empid, emp1.age, emp1.department, emp1.cname, emp1.location, emp1.HR)
 

~ class makeup properties brand shade price smudgeproof
class Makeup:
    def __init__(self, brand, shade, price, smudgeproof):
        self.brand = brand
        self.shade = shade
        self.price = price
        self.smudgeproof = smudgeproof

p1 = Makeup("Chnnel", "pink", 230, "no")
p2 = Makeup("Gucci", "red", 2400, "yes")
p3 = Makeup("Nyke", "black", 340, "no")
p4 = Makeup("Mars", "blue", 2300, "yes")
print(p1.brand, p1.shade, p1.price, p1.smudgeproof)
print(p2.brand, p2.shade, p2.price, p2.smudgeproof)
print(p3.brand, p3.shade, p3.price, p3.smudgeproof)
print(p4.brand, p4.shade, p4.price, p4.smudgeproof)

~ Wap to do right shift operation   o/p -> [2, 3, 4, 1]
l = [1, 2, 3, 4]
k = int(input("Enter number of rotation: "))
for i in range(k):
    l.append(l.pop(0))
print(l)


~ Wap ek chocolate shop hai usme alag alag price ki 4 chocolates hai 
tumhare and dosto ke paas alag alag paise haii like 17 19 22 and all 
to tumhe print karna hai ki tum kitni chocolate kharid sakte ho and kitne paise bache ya nahi bache everything 

~ s = "Alavya" half se ulta


METHODS
it has 3 types 
1. object method
2. class method
3. static method


1. object method
The method which is used to perform modification and some operations on the object member is known as object method
They are used to access or modify the object members
it is ompulsary to pass self to store the address of the object

Syntax:

class Cname:
    set of instructions
    def mname(self):                      ~ to access
        print(args)
    def mname(self, new):                 ~ to modify
        self.var = new

object = Cname(val1, val2, ....)
object.mname()    

Example:

class School:
    sname = "Cambridge"
    location = "Powayan"
    principal = "Shaurya"
    timing = "9:00 to 4:30"
    
    def __init__(self, name, stid, age, bg):
        self.name = name
        self.stid = stid
        self.age = age
        self.bg = bg
        
    def display(self):
        print(self.name, self.stid, self.age, self.bg)
        
    def ch_age(self, new):
        self.age = new

st1 = School("Alavya", 23, 20, "AB+")
st2 = School("Jalkiran", 24, 19, "A+")

st1.display()
st2.display()

st2.ch_age(18)
st2.display()


2. class method
It is used to access and modify the class members
We need to use "cls" as an argument to store the address of the class members.And it is compulsary to use 
@classmethod is the decorator to use 

Syntax:

class Cname:
    set of instructions
    @classmethod                                 ~ to access the class member
    def mname(cls, args):
        statements
    @classmethod                                 ~ to modify the class member
    def mname(cls, new):
        cls.var = new
object = Cname(val)
Cname.mname(val)

Example: 

class School:
    sname = "Cambridge"
    location = "Powayan"
    principal = "Shaurya"
    timing = "9:00 to 4:30"
    
    @classmethod
        
    def display(cls):
        print(cls.sname, cls.location, cls.principal, cls.timing)
    
    @classmethod    
    def ch_time(cls, new):
        cls.timing = new

st1 = School()
st2 = School()

st1.display()
st2.display()

st2.ch_time("9:00 to 1:00")
st2.display()


3. Static method
It neither belongs to class members nor belongs to objectt members
but it will act as a supportive method for both class and object.
decorator -> @staticmethod

Syntax:
class Cname:
    statements
    @staticmethod
    def mname(args):
        statements
object = Cname()


Example:

class Boring:
    name = "Rehman"
    role = "Student"
    @staticmethod
    def nonsense(a, b):
        print(a + b)

st1 = Boring()
Boring.nonsense(10, 20)
st1.nonsense(10, 20) 


class Boring:
    @staticmethod
    def nonsense(a, b):
        print(a + b)

st1 = Boring()
Boring.nonsense(10, 20)
st1.nonsense(10, 20)

Why is this static method?
1. it does not use object members
2. it does not use class members
3. it works independently

static method is a normal helper funtion inside a class


'''


'''
MOCK INTERVIEW QUESTION PRACTICE

~ wap to find the sum of all the integers in a list
[10, 20 30, "Hello", None]
l = [10, 20, 30, "Hello", None]
sum = 0
for i in l:
    if type(i) is int:
        sum = sum + i
print(sum)

~ sum until user enters zero
sum = 0
i = 0
while i >= 0:
    num = int(input("Enter number: "))
    if num != 0:
        sum = sum + num
    else:
        print(sum)


~ wap to find second largest from a given list
[10, 20, 25, 30, 35, 40]
l = [10, 20, 25, 30, 35, 40]
first = 0
second = 0
for i in l:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print("Second largest:", second)

~ wap to check weater a number is prime or not
num = int(input("Enter a number: "))
is_prime = False

if num > 1:
    is_prime = True
    for i in range(2, (num//2+1)):                               ~ we can also use range(2, num) but it will take more time to execute because it will check for all the numbers from 2 to num-1
        if num % i == 0:
            is_prime = False
            break


print("Is prime:", is_prime)


~ remove duplicates from list without using inbuilt functions or typecasting
l = [2,2,1,1,3,3,5,5,6,6]
l = input("Enter list: ")
out = []
for i in l:
    if i not in out:
        out.append(i)
print(out)


~ wap to get following output
input (12, 3.4, "hello", 2+3j, "python", 'bye', False)
output {"hello":5, 'python':6,  'bye':3}
t = (12, 3.4, "hello", 2+3j, "python", 'bye', False)
out = {}
for i in t:
    if type(i) is str:
        out[i] = len(i)   
print(out)
 
 
~ wap input  = 'abcabacbcbc'
output = a3b4c4
 s = 'abcabacbcbc'
out = ""
for i in s:
    if i not in out:
        count = 0
        for j in s:
            if i == j:
                count = count + 1
        out = out + i + str(count)
print(out)
 

~ take two coordinate i.e x and y and check in which points the data points are present 

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
if x > 0 and y > 0 :
    print("Coordinates are in First Quadrant")
elif x < 0 and y < 0 :
    print("Coordinates are in Third Quadrant")
elif x < 0 and y > 0 :
    print("Coordinates are in Second Quadrant")
elif x > 0 and y < 0 :
    print("Coordinates are in Fourth Quadrant")
else:
    print("Coordinates are on the axis or origin")
    

~ Wap to check the given character is uppercase , lowercase or digit or special character 

BY CONDITIONS

ch = input("Enter the character : ")
if ch >= "a" and ch <= "z" :
    print("The character is an lower case alphabet")
elif ch >= "A" and ch <= "Z" :
    print("The character is an upper case alphabet")
elif ch >= "0" and ch <= "9":
    print("The character is a digit")
else:
    print("The character is a special character")   
    
BY INBUILT FUNCTION 

ch = input("Enter the character : ")
if ch.isupper:
    print("The character is an upper case alphabet")
elif ch.islower:
    print("The character is an lower case alphabet")
elif ch.isdigit:
    print("The character is a digit")
else:
    print("The character is a special character")
    
    
~ i/p = ['pro.html', 'google.com', 'pro1.txt']
o/p = {'html' : 'pro', 'com' : 'google', 'txt' : 'pro1'}
l = ['pro.html', 'google.com', 'pro1.txt']
d = {}
for i in l:
    key = i.split('.')[-1]
    value = i.split('.')[0]
    d[key] = value

print(d)

~ wap to find the string values from a tuple using package

s = (10, "hello", 3.4, "python", 2+3j, 'bye', False)
out = []
def find_string(*t):
    for i in t:
        if type(i) is str:
            out.append(i)
    return out
print(find_string(*s))


~ wap to print all the values from a tuple using package

s = (10, "hello", 3.4, "python", 2+3j, 'bye', False)
def find_string(*t):
    for i in t:
        print(i)
find_string(*s)


~ combination Packing
def pack(*a, **b):
    print(type(a))
    print(a)
    print(type(b))
pack(12, 3, a = 1, b = 2)
pack(10, 20, 30)
pack(a = 1, b = 2, c = 3)
pack()

~ unpacking 
def unpack(v1, v2, v3, v4):
    print(v1, v2, v3, v4)
unpack(*"abcd")
unpack(*[10, 20, 30, 40])
unpack(*(1, 2, 3, 4))
unpack(*{12, 27, 56, 78})
unpack(*{"a" : 10, "b" : 20, "c" : 30, "d" : 40})
unpack(*{"a" : 10, "b" : 20, "c" : 30, "d" : 40}.values())
unpack(*{"a" : 10, "b" : 20, "c" : 30, "d" : 40}.items())
unpack(*range(1,5))

Pillars of OOPS
1. Inheritance                               Example: Parents, Child
2. Encapsulation
3. Abstraction                               Example: ATM, Car
4. Polymorphism                              Example: Mobile Phone


1. Inheritance
it is a process of inheriting or invoking the properties or attributes of parent class to child class is known as inheritance

How to create inheritance class

syntax:
class <class_name>:
    Attributes/ methods
class <child_class>(<class_name>):

Example:
class Animal:                                     ~ Parent Class  / Base class
    a = 'snake'
    b = 'dog'

class Birds(Animal):                              ~ Child Class   / Derived class
    c = 'Penguin'

f = Animal()
g = Birds() 

print(f.a, f.b, g.a, g.b, g.c)

always create your object by using your child class
 
 
~ create one inheritance class where class name is A which is parent class and there is one second class child class  
  in class A there is a method show which prints hello in class B there is a method named display which print Hello world 
class A:
    def show(self):
        print("Hello")

class B(A):
    def display(self):
        print("Hello World")

g = B() 
g.show()
g.display()


* if your function is using print dont use print if it is using return you have to use print

Types Of Inheritance
1. Single Level Inheritance
2. Multi Level Inheritance
3. Multiple Inheritance
4. Hierarichal Inheritance 
5. Hybrid Inheritance


1. Single Level Inheritance
one parent class and one child class
the child class can inherit all the properties of parent class

Syntax:
class <class_name>:
    Attributes/ methods
class <child_class>(<class_name>):
    Attributs/ methods

~ create a parent class employee attributes employee name and salary then make a child class developer attributs programming languange 
  and project and display method jab usko call karenge to sari details aayengi 
class Employee:
    name = "Alavya"
    salary = 2389045
class Developer(Employee):
    programming_language = "Python"
    project = "AIML"
    def display(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Programming Language: ", self.programming_language)
        print("Project: ", self.project)

emp1 = Developer()
emp1.display()


2. Multi Level Inheritance
It is a phenomenon of driving properties from parent class or from one class to another class by considering more than one level
in this case the last derived class will be having all the properties of its parent class
it can easily access all the attributes of all the parent class

Syntax:
class C1:
    a / m
class C2(C1):
    a / m
and so on...

~ create a parent class BAnk with a constructor branch name , manager name, next class atm constructor hoga print branch name manager name
and account number class atm2 (atm)  

this question cant be done easily so we use constructor chaining 
we need to use super()
class Bank:
    def __init__(self):
        self.branch_name = 'Powayan'
        self.manager_name = 'Alavya'
class ATM(Bank):
    def __init__(self):
        super().__init__()
        self.account_number = 345687263789
        self.ifsc_code = '123AFY78923'
class ATM2(ATM):
    def __init__(self):
        super().__init__()
        print(self.branch_name)
        print(self.manager_name)
        print(self.account_number)
        print(self.ifsc_code)
        
cust1 = ATM2()









'''




        
