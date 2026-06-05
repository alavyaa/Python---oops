'''
filter()
Syntax:
filter(function, collection)


'''
a = [2, 4, 3, 5, 7, 9, 8]
b = filter(lambda x: x % 2 != 0, a)
print(list(b))

a = [2, 4, 3, 5, 7, 9, 8]
b = map(lambda x: x % 2 != 0, a)
print(list(b))


#1. filter number greater than 45
l = [100, 45, 35, 65, 66, 20, 19]
b = filter(lambda x: x > 45, l)
print(list(b))

#2. filter the number which are negative
s = [1, 2,  -5, 10, -11, -12]
b = filter(lambda x: x < 0, s)
print(list(b))

#3. filter the names which re storing "A"
c = ["Anmol", "Rahul", "Aditya", "Lokesh", "Ambani"]
b = filter(lambda x: x[0] == "A", c)
print(list(b))

#4. filter the strings greater than 5
f = ["Python", "Java", "AIML", "Cyber"]
b = filter(lambda x: len(x) > 5 , f)
print(list(b))

#5. filter the numbers which are divisible by 3 and 5 both
d = [23, 15, 67, 84, 25, 90]
b = filter(lambda x: x%3 == 0 and x %5 == 0 , d)
print(list(b))

#6. filter the name which are ending with "N"
b = filter(lambda x: x[-1] == "n", f)
print(list(b))

#7. filter the voting age feom a list
g = [23, 43, 56, 12, 6, 89]
b = filter(lambda x: x > 18, g)
print(list(b))

#8. filter the palindrome words from the list
h = ["racecar", 'python', 'radar', 'madam']
b = filter(lambda x: x[::-1] == x, h)
print(list(b))

#9. 