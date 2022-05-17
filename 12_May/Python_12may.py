# print(type(var))

# var = list()
# print(type(var))

# var = ["Dhoni","Kohli"]
# var[1] = "Rohit"
# print(var)

# var = ["Dhoni"]
# var1 = ["Kohli"]
# print(var + var1)

# var = ["Dhoni","Kohli"]
# var1 = "Rohit"
# print(var)

# var = ["Dhoni","Kohli"]
# var.insert(5,"Rohit")
# print(var)

# var = ["Dhoni" , "Kohli"]
# var.append("Rohit")
# print(var)

# var = ["Dhoni" , "Kohli"]
# var.append("rohit","kohli")
# print(var)

# var = ["Dhoni" , "Kohli"]
# var.append


# var = ["dhoni","kohli",7,6]
# var.extend(("rohit","kohli"))
# print(var)

# var = ["Dhoni","Kohli"]
# var.extend("India")
# print(var)

# var = ["Dhoni","Kohli","5","9","12","ashwin"]
# var.sort(reverse=True)
# print(var)

# # var = ["dhoni","kohli","5","9","12","ashwin"]
# # print(var.sorted(reverse=True))

# var = ["dhoni","Kholi","5","9","Ashwin","12","Akshay","aswani"]
# output = sorted(var,reverse=False,key=len)
# print(output)




# var = ["ashwin","cat","basket","aisle",5,2,7,8]
# # output = [2,5,7,8,"niwhsa","tac","teksab","elsia"]
# output = sorted(range(len(var)),key=lambda k :var[k],reverse=True)
# for i in output:
#     print('{0:^50}|{1:7}|'.format(var[i]))

# var = ()
# print(type(var))

# var = ("Dhoni")
# print(type(var))



import sys

# var = ("Dhoni","Kohli")
# print(var)
# print(type(var))
# print(sys.getsizeof(var))

# var = ["Dhoni","Kohli"]
# print(var)
# print(type(var))
# print(sys.getsizeof(var))

# var = {}
# print(type(var))

# var = {"name":"Dhoni","age":33}
# print(var)
# print(type(var))

# hashing or hash Table
# O(1)
# key value pair
# key should be unique
# JSON

# var = {"name":"Dhoni","age":33,"age":[44,22]}
# var["age"][1] = 66
# print(var)
# print(type(var))

'''
libraries
pprint()
colorma()
'''

# print(dir(var))

# var = {"name, surname":"dhoni","name, surname":"Akshay,Akki"}
# var1 = {"age":33}
# var.update(var1)
# print(var)

# var = [1,"a",2,"b",3,"c"]
# var_iter = iter(var)
# print(var_iter)
# var_zip = dict(zip(var_iter,var_iter))
# print(var_zip)

# #output = {1:"a".2:"b",3:"c"}

var = [4,5,6].pop()
var +=50
print(var)

var = [4,5,6]
print(var.pop())
print(var)