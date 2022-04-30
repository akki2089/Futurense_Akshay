from array import *
array1 = array("i",[10,20,30,40,50])

#traverse
for x in array1:
    print(x)

#insert
array1.insert(0,90)
print(array1)

#delete
array1.remove(90)
print(array1)

#searching
print(array1.index(40))

#update
array1[4] = 78
print(array1)
