#Manipulating String in Python
import random
#Printing String
astring = "Hello World"
print(astring)

#Cutting string
print(astring[2:5])

print(astring[2:7:2])

print(astring[::-1])

#Cutting string by letter and printing them
for i in range(len(astring)):
    print("The letter at %d index position is %c" %(i, astring[i]))

#Adding letters of string to list
astring_list = []

for i in range(len(astring)):
    astring_list.append(astring[i])

print(astring_list)

#Random Generation
random.shuffle(astring_list)

ran_string = ''.join(astring_list)

print(ran_string)