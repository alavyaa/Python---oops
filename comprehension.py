'''
Comprehension
The phenomenon of creating a new collection by using less number of instructions
It can be used for only mutable collection

There are 3 types of comprehension
1. List Comprehension
2. Set Comprihension
3. Dictionary Comprehension

1. List Comprehension
the phenomenon of creating a new list by using less number of instruction
to perform list comprehension we have 3 syntaxes

Syntax:

var = [var for var in collection or range]

var = [TSB if condition else FSB for var in collection]

var = [var1, var2 for var1 in collection for var2 in collection]
'''

c = [i for i in range(1, 201)]
print(c)

c = [i for i in range(1, 201) if i % 2 == 0]
print(c)

