'''
Decorator


Syntax:
def <decorator_name> (function_name):
    def wrapper(*args, **kwargs):
        pre task
        function_name(*args, **kwargs):
            ost wrapper
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
1. Built-in
2. User-defined


'''