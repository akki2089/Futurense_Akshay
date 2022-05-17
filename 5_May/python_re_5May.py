import re

#when we need to search/Match the word which is at 1st Position
# var = "Dhoni is better than Kohli"
# data = re.match("Dhoni",var)
# print(data)
# print(data.group())
# print(data.span())
# print(data.start())
# print(data.end())

# If the search word is not placed at 1st position so we use search method
# var = "Dhoni is better than Kohli"
# data = re.search("than",var)
# print(data)
# print(data.group())
# print(data.span())
# print(data.start())
# print(data.end())


# # re.I is used for ignoring the case and search for word
# var = "Dhoni is better than Kohli"
# data = re.search("Than",var,re.I)
# print(data)
# print(data.group())
# print(data.span())
# print(data.start())
# print(data.end())


# var = """dhoni is better than Kohli
# dhoni they both play for India
# dhoni is senior"""
# data = re.match("dhoni",var)
# print(data)
# print(data.group())
# print(data.span())
# print(data.start())
# print(data.end())

# var = """dhoni is better than Kohli
# dhoni they both play for India
# dhoni is senior"""
# data = re.search("dhoni",var)
# print(data)
# print(data.group())
# print(data.span())
# print(data.start())
# print(data.end())

# var = """dhoni is better than Kohli
# dhoni they both play for India
# dhoni is senior"""
# data = re.search("dhoni",var,re.M)
# print(data)
# print(data.group())
# print(data.span())
# print(data.start())
# print(data.end())

# var = "<html><body><head></head>"
# data = re.search("<.*",var)
# print(data.group())

# var = "<html><body><head></head>"
# data = re.search("<.*?",var)
# print(data.group())

# var = """dhoni is better than Kohli"""
# data = re.search("(.*) is (.*)",var)
# print(data.group())
# print(data.group(1))
# print(data.group(2))


# # var = """dhoni is better than Kohli"""
# data = re.search("(.*) is (.*?) (.*)",var)
# print(data.group())
# print(data.group(1))
# print(data.group(2))
# print(data.group(3))

# var1 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
# data = re.findall("\d{3}",var1)
# print(data)
#
# var2 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
# data = re.findall("\d{1,3}",var2)
# print(data)
#
# var3 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
# data = re.findall("\D{1,3}",var3)
# print(data)
#
# var4 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
# data = re.findall("\w",var4)
# print(data)
#
# var5 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
# data = re.findall("\w*",var5)
# print(data)
#
# var6 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
# data = re.findall("\w+",var6)
# print(data)
#
# var7 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
# data = re.findall("\W*",var7)
# print(data)
# #
# var8 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
# data = re.findall("\s{1,3}",var8)
# print(data)
#
# var9 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
# data = re.findall("\W",var9)
# print(data)
#
# var = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
# data = re.findall("\S{1,4}",var)
# print(data)
import threading
import time

'''Multi Threading'''

# import time
# import threading
#
# def fun1():
#     print("One")
#     print(time.ctime())
#     time.sleep(2)
#
# def fun2():
#     print("two")
#     print(time.ctime())
#
# t1 = threading.Thread(target=fun1)
# t2 = threading.Thread(target=fun2)
#
# t1.start()
# t2.start()

'''Passing an argument using THreads'''

# import time
# import threading
#
# def fun1(name):
#     print(name)
#     print(time.ctime())
#     time.sleep(2)
#
# def fun2(name):
#     print(name)
#     print(time.ctime())
#
# t1 = threading.Thread(target=fun1,args=("Akshay",))
# t2 = threading.Thread(target=fun2, args=("Aswani",))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

'''Parallel Process'''

# def fun1(name,delay):
#     counter = 0
#     while counter <5:
#         print(name)
#         print(time.ctime())
#         time.sleep(delay)
#         counter +=1
#
# t1 = threading.Thread(target=fun1,args=("Akshay",2))
# t2 = threading.Thread(target=fun1,args=("Aswani",4))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()


