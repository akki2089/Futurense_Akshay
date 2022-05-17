
# import sqlite3

# connection = sqlite3.connect("python.db")
# query = """create table Student ("name" text, "age" int)"""
# execution = connection.execute(query)
# connection.commit()
# connection.close()

# def My_DB_Execution():
#     connection = sqlite3.connect("python.db")
#     query = """create table Student1 ("name" text, "age" int)"""
#     execution = connection.execute(query)
#     connection.commit()
#     connection.close()
    
# My_DB_Execution()
# import sqlite3
# def My_DB_Execution(table_name,db="testing.db"):  # function with default argument
#     connection = sqlite3.connect("python.db")
#     query = f"""create table {table_name} ("name" text, "age" int)"""
#     execution = connection.execute(query)
#     connection.commit()
#     connection.close()
# My_DB_Execution("sports1","python.db")


# import sqlite3
# def My_DB_Execution(db,table_name="sports"):  # function with default argument
#     connection = sqlite3.connect(db)
#     query = f"""select * from {table_name}"""
#     execution = connection.execute(query)
#     connection.commit()
#     connection.close()
# My_DB_Execution("python.db")


# import sqlite3
# def My_DB_Execution(*colmn_name,table_name="sports",db="testing.db"):  # function with default argument
#     connection = sqlite3.connect("python.db")
#     query = f"""create table {table_name} ("name" text, "age" int)"""
#     execution = connection.execute(query)
#     connection.commit()
#     connection.close()
# My_DB_Execution("team","country")


################## Exception Handling

# var = 10/0
# print(var)

# try:
#     var = "a"+10
#     print(var)
# except:
#     print("Sorry")


# try:
#     var = 10/0
#     print(var)
# except TypeError as ex:
#     print(ex)
# except ZeroDivisionError as ex:
#     print(ex)
# except:
#     print("Sorry")

# try:
#     var = "a"+10
#     print(var)
# except (TypeError, ZeroDivisionError) as ex:
#     print(ex)
# except:
#     print("Sorry")

# try:
#     var = 10/0
#     print(var)
# except Exception as ex:
#     print(ex)

###################### finaly and else block in exception

# try:
#     var = 10/2
#     print(var)
# except Exception as ex:
#     print(ex)
# else:
#     print("Else")
# finally:
#     print("Welcome")



####################### exception and finally with database


# import sqlite3
# try:
#     connection = sqlite3.connect("akki.db")
#     query = """create table AKKKKKK ("name" text, "age" int)"""
#     execution = connection.execute(query)
    
# except Exception as ex:
#     print(ex)
# finally:
#     connection.commit()
#     connection.close()
#     print("DB Create")

# import sqlite3
# try:
#     connection = ""
#     connection = sqlite3.connect(db)
#     query = """create table AKKKKKK ("name" text, "age" int)"""
#     execution = connection.execute(query)
    
# except Exception as ex:
#     print(ex)
# finally:
#     if connection != "":
#         connection.commit()
#         connection.close()
#     print("DB Create")


#### index error

# try:
#     var = 10
#     if var > 5:
#         raise IndexError
# except IndexError:
#     print("Sorry")


# try:
#     var = 10
#     if var > 5:
#         raise IndexError("This is my exception")
# except IndexError as ex:
#     print(ex)
    

# try:
#     var = 10
#     if var > 5:
#         raise MyError
# except MyError:
#     print("Sorry")



####### user Defined Exception

# class MyError(Exception):
#     pass
# try:
#     var = 10
#     if var > 5:
#         raise MyError
# except MyError:
#     print("Sorry")


# class MyError(Exception):
#     my_meaning = "user defined exception"
# try:
#     var = 10
#     if var > 5:
#         raise MyError
# except MyError as ex:
#     print(ex.my_meaning)

