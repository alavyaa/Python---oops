'''
File Handling
It is the  process of writing the data into the file or reading the data from the file
File is a container which is used to store the data 
Based on the file extension it is possible to identify the type of data stored in a file
before handling any files getting accessibility is necessary
in python open() function is used to get the accessiblity of a file
for that we have to follow one syntax:
var = open("Path/file_name", "mode")
 OR
with open("Path/file_name", "mode") as var
in the mode of operation writing the data into the file or reading from the file for that 
we have to use modes 

mode of operation 
classified into 3 types
1. Write  -> write(), writelines(), "w+"
2. Read   
3. Append

write mode
write mode is used to write the content into the file
if file is not present then write mode will create the file
if file exists then the content will override
in write mode we have 2 functions
1. write()
it is used for create a single line
Syntax: 
var_name.write("message/ string")

2. writelines()
it is used for writing multiple lines in the file
Syntax:
var_name.writelines([iterables])


read mode
it is used to read the data from the file
in this case if file does not exist then controller will throw error
in read mode we have 3 types of operation
1. read()
it is a function which is used to read the content which is present inside the file
argument is not mandatory
it only acceps integer argument
it will read only that numbers of characters

2. readline()
it is a function which is used to read a particular line from the file and it is possible to read line by line data

3. readlines()
in this function it will read all lines from a file and return a list of string
 
 
append mode
this mode is almost similar to write mode
but  if file already exist then controller will add the new data to the existing file
without performing overriding
in append we have two types of function
1. write()
2. writelines()

Syntax:
var = open("path/ file_name", "a")
in append we have two operations

tell()




'''

f = open("Sample.txt", "a")
# print(f.read(10))     # first 10 character
# print(f.read(10))     # next 10 character
# print(f.readline())
# print(f.readline())
# print(f.readlines(15))
# a = f.readlines()
# print(a[2])
# f.write("hemloo")
print(f.tell())
f.seek(34)
print(f.tell())
f.close()