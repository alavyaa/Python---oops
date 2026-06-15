'''
Decorator
Decorators are functions used to add extra features to an existing function. They are useful when we
have common pre-task and post-task operations to perform.

Syntax:
def <decorator_name> (function_name):
    def wrapper(*args, **kwargs):
        pre task
        function_name(*args, **kwargs):
        post wrapper
    return wrapper
    
@<decorator_name>
def main():
    print("Task")
main()

Example:
def hih(alu):
    def wrapper():
        print('This is the start of decorator.')
        alu()
        print('This is the end of decorator')
    return wrapper
@hih                                                 ~ first tareeka which we use always
def greet():
    print("Good Morning")
    
x = hih(greet)                                       ~ second tareeka which is internally being done
x()

Two types 
1. Inbuilt
2. User-defined

Inbuilt Decorators
These are decorators whose tasks are already predefined by the developers
Examples
• @classmethod
• @staticmethod
• @property
• @abstractmethod

User Defined Decorators
These are decorators that get created based on the user requirement

Syntax
def decorator_name(func):
 def inner(*args, **kwargs):
 # pre-task
 func(*args, **kwargs)
 # post-task
 return inner
@decorator_name
def func_name(args):
 # SB (Statement Block)
func_name(values)





'''