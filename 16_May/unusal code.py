# class one:
#     def __init__(self,name):
#         self.name = name
#     def onefun(self):
#         print(self.name)
        
# class two:
#     def __init__(self,age):
#         self.age = age
#         self.test = one("Dhoni")
#         self.test.onefun()
#     def twofun(self):
#         print(self.age)
        
# t = two(23)
# t.twofun()

# class one:
#     def __init__(self,name):
#         self.name = name
#     def onefun(self):
#         print(self.name)

# class two:
#     def __init__(self,age,fobj):
#         self.age = age
#         self.name = fobj
#         fobj.onefun()
#     def twofun(self):
#         print(self.age)
        
# fobj = one("Kohli")
# t = two(23,fobj)
# t.twofun()


# class A:
#     def fun(self):
#         print("A")

# class B(A):
#     def fun(self):
#         print("B")
        
# class C(A):
#     def fun(self)
#     print("C")

# class D(C,B):
#     pass
# d = D()
# d.fun()


# class A:
#     def fun(self):
#         print("A")

# class B(A):
#     def fun(self):
#         print("B")
        
# class C(A):
#     def fun(self)
#     print("C")

# class D(C,B):
#     # pass
#     def fun(self):
#         print("D")

# d = D()
# d.fun()


#MRO -> Method Resolution Order
#Near by search


############ Pandas ##############

# import pandas as pd
# df = pd.DataFrame({
#     'name':['alice','bob','charlie'],
#     'date_of_birth':['10/25/2005','10/29/2022','01/12/1998']
# })

# print(df)
# df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])
# print(df)

######################################################

# import pandas as pd
# df = pd.DataFrame({
#     'name':['alice','bob','charlie'],
#     'date_of_birth':['10/25/2005','10/29/2022','01/12/1998']
# })

# print(df)
# df['date_of_birth'] = pd.to_datetime(df['date_of_birth'],format='%d/%m/%y')
# print(df)

#######################################################

# from datetime import datetime
# import pandas as pd
# df = pd.DataFrame({
#     'name':['alice','bob','charlie'],
#     'date_of_birth':[12,43,22,34]
# })
# df["timestamp_col"] = pd.Timestamp(datetime.now())
# df["formatted_col"] = df["timestamp_col"].map(lambda ts: ts.strftime('%d-%m-%y'))

# print(df)


######################################
# import pandas as pd
# from datetime import date

# df = pd.DataFrame({
#     'name':['alice','bob','charlie'],
#     'date_of_birth':['10/25/2005','10/29/2022','01/01/2001']
# })

# # convert to type datetime
# df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])

# df[df['date_of_birth'] < pd.Timestamp(date(2002,1,1))]

# print(df)
# output = df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])
# print(output)

############################################

# import pandas as pd
# from datetime import date

# date_from = pd.Timestamp(date(2003,1,1))
# date_to = pd.Timestamp(date(2006,1,1))

# #### df is not defined

# df = df[
#     {df['date_of_birth'] > date_from } &
#         {df['date_of_birt'] <date_to}]


