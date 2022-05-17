# import pandas
# my_input = [1,2,3,4,5]
# list_manipulation = my_input*2
# print(list_manipulation)
# my_dimension = pandas.DataFrame(my_input)
# print(my_dimension)
# print(type(my_dimension))


# import pandas
# my_imput = [[1,2,3],[4,5,6],[7,8,9]]
# my_dimension = pandas.DataFrame(my_imput)
# print(my_dimension)
# print(type(my_dimension))

# import pandas
# my_imput = [[1,2,3],[4,5,6],[7,8,9]]
# my_dimension = pandas.DataFrame(my_imput)
# print(my_dimension)
# print(type(my_dimension))
# sum_of_tuple = my_dimension.sum()
# print(sum_of_tuple)


# import pandas
# my_imput = [1,2,3],[4,5,6],[7,8,9]
# my_dimension = pandas.DataFrame(my_imput)
# print(my_dimension)
# print(type(my_dimension))

# pandas in Dictonaries

# import pandas
# my_input= {"names":["Dhoni","Kohli"],"teams":["CSK","RCB"]}
# my_dimension = pandas.DataFrame(my_input, index=["a","b"])
# print(my_dimension)


# Different Function of Pandad

# 1. Apply Sum
# By default it is column wise


# import pandas
# my_input = ((1,2,3,4),(5,6,7,8))
# my_dimension = pandas.DataFrame(my_input)
# print(my_dimension)
# sum_of_tuple = my_dimension.sum()
# print(sum_of_tuple)

# Apply Sum in Row wise
# Sum in ROw wise use axis keyword

# import pandas
# my_input = ((1,2,3,4),(5,6,7,8))
# my_dimension = pandas.DataFrame(my_input)
# print(my_dimension)
# sum_of_tuple = my_dimension.sum(axis=1)
# print(sum_of_tuple)

# 2. Head
#
# import pandas
# my_input = ((1,2,3,4),(5,6,7,8))
# my_dimension = pandas.DataFrame(my_input)
# print(my_dimension)
# print("----")
# my_head = my_dimension.head(1)
# print(my_head)


# name the rows and Column

# import pandas
# my_input = ((1,2,3,4),(5,6,7,8))
# my_dimension = pandas.DataFrame(my_input, index = ['a','b'], columns=["A","B","C","D"])
# print(my_dimension)

# 3. Describe

# import pandas
# my_input = ((1,2,3,4),(5,6,7,8))
# my_dimension = pandas.DataFrame(my_input)
# my_describe = my_dimension.describe()
# print(my_describe)

# 4. Memory_Usage

# import pandas
# my_input = ((1,2,3,4),(5,6,7,8))
# my_dimension = pandas.DataFrame(my_input)
# my_usage = my_dimension.memory_usage(deep=True)
# print(my_usage)

# 5. iloc and 6. loc

# import pandas
# my_input = ((1,2,3,4),(5,6,7,8))
# my_dimension = pandas.DataFrame(my_input, index = ['a','b'], columns=["A","B","C","D"])
# print(my_dimension)
# print("------")
# print(my_dimension.loc['a'])
# print(my_dimension.iloc[0,0])

# 7. To Csv

# import pandas
# my_input = ((1,2,3,4),(5,6,7,8))
# my_dimension = pandas.DataFrame(my_input, index = ['a','b'], columns=["A","B","C","D"])
# print(my_dimension)
# my_dimension.to_csv("akki.csv")

# 8. Group By
# import pandas
#
# my_input = ({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
#                    'points': [5, 7, 8, 9, 12, 6, 10, 4],
#                    'assists': [11, 8, 10, 6, 8, 5, 9, 12]})
#
# my_dimension = pandas.DataFrame(my_input)
# print(my_dimension)
# print("-------")
# group = my_dimension.groupby(by="team").points.mean()
# print(group)

import pandas as pd
df = pd.read_csv("student.csv")
print(df)
print("-----")
group = df.groupby(by="class").mark.mean()
print(group)
print("-----")
# group1 = df.groupby(["class","mark"])
# print(group1.first())

sort = df.sort_values(by="name",ascending=False)
print(sort)



# import pandas
#
# data = {"Score":[90,20,25,36],"Player":["A","B","C","D"]}
# df_data = pandas.DataFrame(data)
# mean_data = df_data.groupby(by="Player").mean()
# print(mean_data)


# import pandas
#
# my_input = ({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
#                    'points': [5, 7, 8, 9, 12, 6, 10, 4],
#                    'assists': [11, 8, 10, 6, 8, 5, 9, 12]})
#
# my_data = pandas.DataFrame(my_input)
# mean_data = my_data.groupby(["team"])["points"].mean()
# print(mean_data)
# sort = my_data.sort_values(by="points",inplace=True)
# print(sort)