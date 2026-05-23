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



'''

class Bank:
    bname = "SBI"
    location = "Bangalore"
    Manager = "Aditya"

cus1 = Bank()
cus2 = Bank()

print(Bank.bname, Bank.location, Bank.Manager)
print(cus1.bname, cus1.location, cus1.Manager)
print(cus2.bname, cus2.location, cus2.Manager)

Bank.location = "Chandigarh"         

print(Bank.bname, Bank.location, Bank.Manager)
print(cus1.bname, cus1.location, cus1.Manager)
print(cus2.bname, cus2.location, cus2.Manager)

cus1.location = "Jharkhand"

print(Bank.bname, Bank.location, Bank.Manager)
print(cus1.bname, cus1.location, cus1.Manager)
print(cus2.bname, cus2.location, cus2.Manager)

cus2.location = "Mumbai"

print(Bank.bname, Bank.location, Bank.Manager)
print(cus1.bname, cus1.location, cus1.Manager)
print(cus2.bname, cus2.location, cus2.Manager)

