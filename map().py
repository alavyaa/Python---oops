'''
function map()
it is a function which is used to perform same set of operation for each and every value present inside the collection  
Syntax:

map(function, collection)

map(lambda x : x*x, a)

a = [10, 20, 30, 40, 50]
b = map(lambda x : x*x, a)
print(list(b))

a = ["Alavya", "Shaurya", "Vashu", "Aman"]
b = map((lambda x : x.upper()), a)
print(list(b))

'''
#1
a = [10, 20, 30, 40, 50] 
b = map(lambda x ,y : (x*x , y*y*y), a, a)
print(list(b))                                  

#2
b = map(lambda x : x + (x * 18 / 100), a)
print(list(b))


#3
c = ["Alavya", "Shaurya", "Vashu", "Aman"]
b = map(lambda x : x[-1], c)
print(list(b))

#4
a = [10, 20, 30, 40, 50, 60] 
b = map(lambda x : x/60, a)
print(list(b))

#5
d = [12, 34, 54, 53, 34, 23]
f = [12,56,23,34, 34,34,56]
b = map(lambda x, y, z : x+y+z, a, d, f)
print(list(b))

#6
d = [12, 34, 54, 53, 34, 23]
b = map(lambda x : "even" if x%2 == 0 else "odd", d)
print(list(b))

#7
c = ["Alavya", "Shaurya", "Vashu", "Aman"]
b = map(lambda x : len(x) , c)
print(list(b))

#8
s = [12213343, 2434234, 545353, 3443325]
b = map(lambda x : x - (x *10/100), s)
print(list(b))

#9
c = ["Alavya", "Shaurya", "Vashu", "Aman"]
b = map(lambda x : x[::-1], c)
print(list(b))

#10
m = [12, 34, 65, 98, 87]
b = map(lambda x : "A" if x > 90 and x < 100 else "B" if x > 80 and x < 90 else "C" if x > 70 and x < 80 else "Fail", m)
print(list(b))

#Challenge
v = ["Rahul", "Aman", "Priya", "Neha"]
h = [23, 76, 98, 12]
b = map(lambda x , y: (y + "-Pass") if x > 56 and x < 100 else (y +"-Fail"), h , v)
print(list(b))