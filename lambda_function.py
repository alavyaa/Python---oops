'''
lambda function:
it is a function which is anonymous in nature it is a function without name which is used to declare in 1 line
we have to make use of lambda keyword to create a lambda function
we can pass arguments according to the requirements

an anonymous function which helps in creating single line function

Syntax:
lambda argument : expression

b = lambda a : a**2 
print(b(10))
print((lambda a : a**3)(10))

b = lambda a ,b: a*b 
print(b(10, 20))
print((lambda a : a**3)(10))

~ wap to check weather the number is greater or not
if  the number is greater print(hi) else print (bye)
by using lembda function
b = lambda a,b : "Hi" if a > b else "Bye" 
print(b(10, 20))
'''
