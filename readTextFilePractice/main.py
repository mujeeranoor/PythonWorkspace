file = open("abc.txt", "r")
print(file.read())

###################################

file = open("abc.txt", "r")
print(file.read(5))

#############################

file = open("abc.txt", "r")
print(file.readline())

#############################

file = open("abc.txt", "r")
print(file.readline())
print(file.readline())

file.close() #we should always close 
# a file after we are done reading 
# or doing some changes in it.