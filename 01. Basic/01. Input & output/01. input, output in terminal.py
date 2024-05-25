# .......................................................................................................................................................................
# ..........................................................| Printing on terminal |.....................................................................................
# .......................................................................................................................................................................



#.......................Print Hello World............................................
print ("Hello world")

print("Prince Sabu")

num = 25
print (num)

princeAge = 26


# before displaying a int with words, convert it to string. 
print("Prince age is " + str(princeAge)) 


# .............................. input ..............................................

getNumber = input("Enter number: ")
# Get number is a 'str'

print(getNumber)
print(type(getNumber)) # it is a str

# Before doing any operation, it should be convert it into 'int'

conNumber = int(getNumber)

print(conNumber)  
print(type(conNumber)) # it is a int
