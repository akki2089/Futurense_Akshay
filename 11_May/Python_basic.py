# var = 'dhoni'
# print(var[0])
# print(var[0:])
# print(var[0:4])
# print(var[2:0])
# print(var[-2:0])
# print(var[-2:-5])
# print(var[0:-3])
# print(var[::2])
# print(var[::-2])
# print(var[0:-3:-1])

# var = 'dhoni'
# print(var)

# var = "Kohli"
# print(var)

# var = "Dhoni",'msd'
# print(var)

# var = "Dhoni"'Csk'
# print(var)

# var = "Dhoni'c'sk"
# print(var)

# var = "dhoni  
# msd"
# print(var)


# var = """dhoni 
# msd"""
# print(var)


# var = """dhoni  /
# msd"""
# print(var)



# var = """dhoni  \
# msd"""
# print(var)


# var = "dhoni  /
# msd"
# print(var)

# var = "dhoni  \
# msd"
# print(var)

# var = list(input("enter the data"))
# print(var)
# print(type(var))

# var = list("dhoni")
# print(var)

# var = list(input("enter").split())
# print(var)
# print(type(var))

# name = "Dhoni"
# age = 33

# output = "my captain " +name+ " Plays even at the age of " +str(age)
# print(output)

# output = "my captain %s Plays even at the age of %d" %(name,age)
# print(output)

# output = "my captain {} Plays even at the age of {}" .format(name,age)
# print(output)

# output = f"my captain {name} Plays even at the age of {age}"
# print(output)

# name = "Dhoni plays for csk"
# for x in name:
#     print(x)

# name = "Dhoni plays for csk"
# #__iter__ (hold the state of the travelled letter)
# for x in name:
#     print(x, end=" ")
#     #__next__
    
# #__iter__
# #__next__
# #iter()
# #generator()

# name = "Dhoni"
# name1= "Kohli"
# for x,y in zip(name,name1):
#     print(x,y)

# name = "Dhoni"
# name1= "Kohli"
# output = iter(name,name1)
# print(output)

# name = ["Dhoni"]
# name1= ["Kohli"]
# output = iter(name,name1)
# print(output)

# name = ["Dhoni"]
# name1= ["Kohli"]
# output = list(iter(zip(name,name1)))
# print(output)

# name1= ["Kohli"]
# output = iter(name1)
# print(output)

# var = "Dhoni is captain"
# for x in enumerate(var):
#     print(x)
    
# var = "Dhoni is captain"
# for x,y in enumerate(var):
#     print(x)
#     print(y)

# var = "Dhoni is captain"
# for x ,_ in enumerate(var):
#     print(x)


# var = "Dhoni is captain"
# for x , y in enumerate(var):
#     if x%2 == 0:
#         print("SUCCESS")


# var = "Dhoni is captain"
# for x,y in enumerate(var):
#     if y == "i":
#         print("Success")
#     if y == "a":
#         print("Success")
        
# var = "Dhoni is captain"
# for x,y in enumerate(var):
#     if y == "i" or y == "a":
#         print("Success")

# for x in range(10):
#     print(x)

# print('---')
# for x1 in range(2,10):
#     print(x1)
    
# print('---')
# for x2 in range(2,10,-1):
#     print(x2)
    
# output = 0
# for x3 in range(10,1,-1):
#     # output = output-1
#     output -= 1
# print(output)

# difference between range and xrange

# import numpy as np
# a = np.random.rand(5,2)
# print(a)

# import numpy as np
# a = np.random.rand(2,2)
# print(a)

import numpy as np
a = np.random.randint(3,size=10)
print(a)