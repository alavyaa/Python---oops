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

There are are two types of states:-
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
    
 

'''
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



