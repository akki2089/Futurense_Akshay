from tkinter import *
from tkinter import filedialog
import os.path

save_path =
base = Tk()
# Create a canvas
base.geometry('250x250')



# Function for opening the file
def file_opener1():
    f1_list=[]
    f1=[]

    input1 = filedialog.askopenfile(initialdir="/")
    print(input1)
    with open(input1,"r") as file1:
          l1 = file1.readlines()
    for word in range(len(l1)):
        q=l1[word]
        f=q.split()
        f1_list.extend(f1)



def file_opener2():
   input2 = filedialog.askopenfile(initialdir="/")
   print(input2)
   for i in input2:
       print(i)
'''
def file_reader():
        input3 = filedialog.askopenfile(initialdir="/")
        print(input3)
    with open("file2.txt", "r") as file2:
        file2_content = file2.readlines()
'''



# Button label
x = Button(base, text ='Select a file1', command = lambda:file_opener1())
x.pack()
y = Button(base, text ='Select a file2', command = lambda:file_opener2())
y.pack()
'''
z = Button(base, text ='evalute', command = lambda:file_reader())
z.pack()'''
mainloop()

