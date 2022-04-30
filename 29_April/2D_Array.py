from array import *

t = [[11,12,3],[4,5,6],[7,8,9]]
print(t)

#print row and column wise
for r in t:
    for c in r:
        print(c,end=" ")
    print()

#inserting Value

t.insert(0,[2,3])
t.insert(1,[3,4])
print(t)

#delete value
del t[0]
del t[1]
print(t)

#update values
t[0] = [1,2,3]

for r in t:
    for c in r:
        print(c,end=" ")
    print()