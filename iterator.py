'''
Iterator
it is a process of traversing through sequence getting the value one by one 
the function is used to perform iteration 
for loop completely depends on iterator so that it has an inbuilt iterator
to perform iterator it consists of two methods
1. iter()
2. next()

iter()
it is a function which is used to make the control to get pointed to the initial node address
Syntax:
var = iter(iterables)

iterables: multi value data (list, tuple, range, dictionary, set, strings)

next()
it is a function which is used to get the values one by one
once you accessed all the objects inside the iterables that time it will throw StopIteration error
Syntax:
next(iterator())



'''
a = [1, 2, 30, 40]
it = iter(a)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


class Count:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

obj = Count(1, 45)

print(obj.__next__())
