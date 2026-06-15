'''
generator
=========
yields a sequence of values, one at a time, instead of computing them all at once and sending them back. 
This is useful when you want to iterate over a large dataset or an infinite sequence without consuming a lot of memory.
yield keyword is used in this.

Generator is a function used to generate some sequence of elements or values using the yield
keyword. If any user-defined function consists of at least one yield keyword, it is called a generator
function.
Generator function returns the address of an output collection. To get the values, type casting (list,
tuple, set) is required.

return
• Keyword used to return control from
the function. Control will NOT come
back.
• Used in user-defined functions.
• Type casting is NOT required.
yield
• Keyword used to pause function
execution, store the value, and
resume for further execution.
• Used in generator functions.
• Type casting IS required (list, tuple,
set).

Example: Basic Generator
def sam():
    print('hello')
    yield 1
    print('hi')
    yield 2
    print('bye')
    yield 3
print(list(sam()))
# Output: hello hi bye [1,2,3]
'''
 