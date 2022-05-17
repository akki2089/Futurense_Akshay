
sName = "Akshay Aswani. Trainee Data Engineer"

#TO CAPITALIZE FIRST LETTER OF A STRING
sName.capitalize()


# CONVERTS STRING TO LOWER CASE
sName.casefold()

# TO COUNT THE SPECIFIED VALUE
sName.count("a")

# Returns True or False depending on the condition
sName.endswith('i')


sName.startswith('A')


# Finds for a specified valued and returns the position (index) of it
sName.find('n')


sName.index('Trainee')


sName.isascii()

sName.isnumeric()


sName.isspace()



sName.replace('Trainee', 'Senior')

#Converts the string to Upper Case
sName.upper()


# Converts the first character of each word to upper case
sName.title()


# ############ Different Functions on List


l = [1,2,3,4,"Hello","World"]


# Adds an element at the end of list
l.append(12)



# Adds the element at the specified position
l.insert(2,4)


#Add the element (any iterables) to the end of the list
l.extend([987])


#Returns the number of elements with specified value
l.count(4)


l.pop()


#Removes the first ocurance of values
l.remove(2)


#Sort the list in asc order
l  = ["Fazeel","Abhi","jacob", "lmsrahul", "ashish","hadoopharinath"]
l.sort()

# Sort the list based on numbers
l1 = [("1,Fazeel"),("4,Abhi"),("3,jacob"), ("2,lmsrahul"), ("6,ashish"),("5,hadoopharinath")]
l1.sort()
l1


############## Different functions on Dictionaries

d = {'Key1': 'Val 1', 'Key2': 'Val2', 'Key3':'Val3'}


#Remove specified key-values pair
d.pop('Key2')


# Remove the key-value pair in LIFO order
d.popitem()


#Returns the values of key if key is present in dictionary, else None is returned
d.get('Key1')


#Multiple Assignments
a=1,2,3


a,b = 'abc',[12,45]


