

# Create new dictionary
phonebook = {"Jake" : 9995556666,
             "Jannet" : 6543219874,
             "Ross" : 6842369875}
#print dictioanry
print(phonebook)

#deleting number
phonebook.pop("Jake")

#print dictionary into string
for name, number in phonebook.items():
    print("%s's number is %s." % (name, number))

#getting input for new entry
new_name = input("Enter a person's name: ")
new_number = input("Enter %s's number: " % (new_name))

#Removes - from number entry
new_number = new_number.replace("-","")

#converts to int for normalization
new_number = int(new_number)

#adds new name and number to dictionary
phonebook[new_name] = new_number

print(phonebook)