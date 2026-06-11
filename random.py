'''
random

random.random()
always gives random values between  the range from 0.0 to 1.0
import random
print(random.random())

random.randint()
takes two arguments starting range and ending range value aur in dono ke beech se koi random value throw karta hai
import random
print(random.randint(a, b))
b > a always otherwise we get valueerror

random.choice()
it only accepts iterables
import random
print(random.choice(iterables))

random.shuffle()
shuffles the list
import random
a = [12, 34, 65, 23, 66, 776, 324, 756]
random.shuffle(a)
print (a)

random.sample()
import random
print(random.sample(iterable, k parameter))
jo bhi list pass ki usme se random k parameter elements and new list banayega 
and k parameter should be less than length of list
'''