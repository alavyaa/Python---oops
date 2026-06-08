'''
in write mode we havee 2 methods
write()
writelines()
Syntax: 
f.writelines(iterables/collections)


'''

f = open("Sample.txt", "w")

f.writelines(["Hello World\n", "2. MY bestfriend is the best gadha\n", "3. he is the best annoyer\n", "4. he is the best monkey\n"])

f.close()

#f.writelines()