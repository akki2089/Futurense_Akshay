# var = {"name":"dhoni"}
# print(var)
# print(type(var))

# var = {"name":"dhoni","name":"kohli"}
# print(var)
# print(type(var))

'''in dictionry '''
# var = {"name":"dhoni"}
# var1 = {"age":33}
# print(var+var1)

# var = {"name":"dhoni"}
# var1 = {"age":33}
# output = {**var,**var1}
# print(output)

# var = {"name":"dhoni"}
# var1 = {"age":33}
# var.update(var1)
# print(var)

'''any inmutable character can be accepted in dictionary'''
# var={"name":"dhoni",True:"Kohli",3:"raina",5.9:"ashwin",("a","b"):"Kartik",(1,2):"Akshay"}
# print(var)
# print(type(var))

# var={1:"dohni",True:"Virat",1.0:"Rohit"}
# print(var[1])

# var={"name":"dohni"}
# print(dir(var))

# var = {"name":"dohni"}
# var["coutntry"] = "india"
# print(var)

# var = {"name":"dohni"}
# var["name"] = "Kohli"
# print(var)



# var = {"name":"dhoni","age":33,"team":"csk","born_year":1980}
# print(var.items())
# sort_dic = dict(sorted(var.items()))
# print(sort_dic)



# var = {"name":"dhoni","age":33,"team":"csk","born_year":1980}
# keys = []
#
# for x in var.keys():
#     keys.append(x)
# print(keys)
#
# sorted_keys = sorted(keys)
# print(sorted_keys)
#
# sorted_dict = {}
# for x in sorted_keys:
#     value = var[x]
#     sorted_dict[x] = value
# print(sorted_dict)


# var = {"name":"dhoni","age":33,"team":"csk","born_year":1980}
# sorted_dict ={x:var[x] for x in sorted ([x for x in var.keys()])}
# print(sorted_dict)

# var = ["dhoni","ashwin","sachin","akshay"]
# var.sort()
# print(var)

# var = ["dhoni","ashwin","sachin","akshay","cat","running","ab"]
# print(sorted(var))
# output = sorted(var,reverse=True)
# print(output)


# import json
# var = '{"name":"dhoni","age":"ashwin"}'
# print(var)
# print(type(var))
#
# res = json.loads(var)
# print(res)
# print(type(res))
#
# var_string = json.dumps(res)
# print(var_string)
# print(type(var_string))

# var = ["a","b","c"]
# var.pop()
# print(var)
#
# var = {"name":"dhoni","age":"ashwin"}
# var.popitem()
# print(var)
#
# var = {"name":"dhoni","age":"ashwin"}
# var.pop("name")
# print(var)

