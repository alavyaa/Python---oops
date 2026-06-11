'''
Exception Handling

Syntax:
try:
    statement block
except error_name:
    statement block


we only have one try block but we can create n number of except block 

we have 3 types of exception handling
1. Specific Exception Handling
2. Generic Exception Handling
3. Default Exception Handling
    1. Custom Exception handling
    2. User-Defined Exception handling

1. Specific Exception Handling
when we know the type of error we gonna face
for example:
try:
    a = int(input("Enter a value: "))
    b = int(input("Enter another value: "))
    print(a/b)
except ZeroDivisionError:
    print("Error hai bhai 0 pass nahi karna")
except ValueError:
    print("number daal bhai")    

2. Generic Exception Handling
Syntax:
try:
    statement block
except Exception:
    statement block

3. Default Exception Handling
Syntax:
try:
    statement block
except:
    statement block

Two types of default ex. handling
1. Custom Exception handling
Syntax:
raise <exception> ("message")

2. User-Defined Exception handling
class Error_name(Exception):
    pass
raise Error_name('message')

For Example:
class AgeError(Exception):
    pass
try:
    a = int(input("Enter your age: "))
    if a < 18:
        raise AgeError('Not Eligible')
    else:
        print("Eligible")
except AgeError as E:
    print(E)
    
final structure of Exception Handling
try:
    SB
except:
    SB
except:
    SB
finally:
    SB
    
finally is mandatory to use
finally will always execute


'''