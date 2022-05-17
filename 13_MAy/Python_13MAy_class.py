# class My_class:
    
#     def fun():
#         print("Welcome to Python")
        
#     def two():
#         print("Welcome 2 oops")

# My_class.fun()
# My_class.two()


# class My_class:
    
#     def fun():
#         print("Welcome to Python")
        
#     def two():
#         print("Welcome 2 oops")
        
# my = My_class
# my.fun()
# my.two()



# class My_Server(object):        # every class inherits object
    
#     def __init__(self,ip,pwd):
        
#         self.ip = ip
#         self.pwd = pwd
    
#     def server_login(self):
#         print("Welcome to Python",self.ip)
        
#     def hostname(self):
#         print("Welcome 2 oops",self.ip,self.pwd)
        
# my = My_Server("2.2.2.2","123")
# my.server_login()
# my.hostname()

# My_Server() is called constructor
# my is now become instance object reference
#when we create constructor , we will have one hidden object created inside the constructor
# __init__ by nature is called attribute or magic methods or dunder methods
# __init__ will be created automatically when class constructor got created
# __init__ as funcionality we call as instance + imitializer =---> instantitator
# __new__


# class My_Server(object):        # every class inherits object
    
#     """__author__Mohan s
#     ___data__ May 13 2022
#     Class Name: My_Server"""
    
#     def __init__(self,ip,pwd):
        
#         self.ip = ip
#         self.pwd = pwd
    
#     def server_login(self):
#         print("Welcome to Python",self.ip,country)
        
#     def hostname(self):
#         print("Welcome 2 oops",self.ip,self.pwd)
        
# my = My_Server("2.2.2.2","123")
# my.server_login("India")
# my.hostname()
# print(my.__doc__)


# class My_Server(object):        # every class inherits object
    
#     """__author__Mohan s
#     ___data__ May 13 2022
#     Class Name: My_Server"""
    
#     def __init__(self,ip,pwd):
        
#         self.ip = ip
#         self.pwd = pwd
    
#     def server_login(self):
#         print("Welcome to Python",self.ip,country)
        
#     def hostname(self):
#         print("Welcome 2 oops",self.ip,self.pwd)
    
#     @staticmethod
#     def routing(asdf):
#         print(asdf)
        
# my = My_Server("2.2.2.2","123")
# my.server_login("India")
# my.hostname()
# my.routing("http://testing.com")
# print(my.__doc__)

# class My_Server(object):        # every class inherits object
    
#     def __init__(self,ip,pwd):
        
#         self.ip = ip
#         self.pwd = pwd
    
#     def server_login(self,country):
#         print("Welcome to Python",self.ip)
        
#     def hostname(self):
#         print("Welcome 2 oops",self.ip,self.pwd)
        
# my = My_Server("2.2.2.2","123")
# my.server_login("india")
# my.hostname()


# var = 100
# def fun():
#     global var
#     var = 10
#     print(var)
    
# print(var)
# fun()
# print(var)



# # Scoping
# var = 100 # Global

# def fun():
#     #var = 100 #enclosed
#     def new():
#         #var = 10 #local Scope
#         print(var)
        
#     new()
    
# fun()


# counter = 0
# def fun():
#     global counter
#     counter += 1
#     print("hello",counter)
    
#     if counter == 100:
#         return
#     fun()
# fun()

# counter = 0
# def fun():
#     global counter
#     counter += 1
#     print("hello",counter)
    
#     if counter < 100:
#         fun()
# fun()


# class My_Server(object):        # every class inherits object
    
#     def __init__(self,ip,pwd):
        
#         self.ip = ip
#         self.pwd = pwd
    
#     def server_login(self,country):
#         print("Welcome to Python",self.ip,country)
        
#     def server_login(self):
#         print("Welcome 2 oops",self.ip,self.pwd)
        
# my = My_Server("2.2.2.2","123")
# my.server_login("india")


# class My_Server(object):        
    
#     def __init__(self,ip,pwd):
        
#         self.ip = ip
#         self.pwd = pwd
    
#     def server_login(self):
#         print("Welcome to Python",self.ip)

# class Second_class(My_Server):      #inheritance
        
#     def Login(self):
#         print("Welcome 2 oops",self.ip,self.pwd)
        
# my = Second_class("2.2.2.2","123")
# my.server_login()
# my.Login()


# 2nd.

# class My_Server(object):        
    
#     def server_login(self):
#         print("Welcome to Python",self.ip)

# class Second_class(My_Server):      #inheritance
    
#     def __init__(self,ip,pwd):
        
#         self.ip = ip
#         self.pwd = pwd
        
#     def Login(self):
#         print("Welcome 2 oops",self.ip,self.pwd)
        
# my = Second_class("2.2.2.2","123")
# my.server_login()
# my.Login()


# #3rd

# class My_Server(object):        
    
#     def __init__(self,ip,pwd):
        
#         self.ip = ip
#         self.pwd = pwd
    
#     def server_login(self):
#         print("Welcome to Python",self.ip)

# class Second_class(My_Server):      #inheritance
    
#     def __init__(self,ip,pwd):
        
#         self.ip = ip
#         self.pwd = pwd
        
#     def Login(self):
#         print("Welcome 2 oops",self.ip,self.pwd)
        
# my = Second_class("2.2.2.2","123")
# my.server_login()
# my.Login()



# class My_Server(object):        
    
#     def __init__(self,ip,pwd,country):
        
#         self.ip = ip
#         self.pwd = pwd
#         self.country = country
    
#     def server_login(self):
#         print("Welcome to Python",self.ip,self.country)

# class Second_class(My_Server):      #inheritance
    
#     def __init__(self,ip,pwd):
        
#         self.ip = ip
#         self.pwd = pwd
#         My_Server.__init__(self,self.ip,self.pwd,"india")
        
#     def Login(self):
#         print("Welcome 2 oops",self.ip,self.pwd)
        
# my = Second_class("2.2.2.2","123")
# my.server_login()
# my.Login()


# class My_Server(object):        
    
#     def __init__(self,ip,pwd,country):
        
#         self.ip = ip
#         self.pwd = pwd
#         self.country = country
    
#     def server_login(self):
#         print("Welcome to Python",self.ip,self.country)

# class Second_class(My_Server):      #inheritance
    
#     def __init__(self,ip,pwd):
        
#         self.ip = ip
#         self.pwd = pwd
#         # My_Server.__init__(self,self.ip,self.pwd,"india")
#         super().__init__(self.ip,self.pwd,"india")
        
#     def Login(self):
#         print("Welcome 2 oops",self.ip,self.pwd)
        
# my = Second_class("2.2.2.2","123")
# my.server_login()
# my.Login()



### Composition and aggregation

class My_Server:        
    
    def server_login(self):
        print("Welcome to Python",self.ip)

class Second_class(My_Server):      #inheritance
    
    def __init__(self,ip,pwd):
        
        self.ip = ip
        self.pwd = pwd
        # # My_Server.__init__(self,self.ip,self.pwd,"india")
        # super().__init__(self.ip,self.pwd,"india")
        
    def Login(self):
        print("Welcome 2 oops",self.ip,self.pwd)
        
my = Second_class("2.2.2.2","123")
my.server_login()
my.Login()