from datetime import datetime
import time
import os
import pyautogui
from tkinter import *
from tkinter import filedialog as fd


n = int(input())
for i in range (1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print('\n')

screen=pyautogui.screenshot()

r=Tk()
r.withdraw()

folder = fd.askdirectory()

ct = datetime.now()
print(ct)

ct1 = datetime.now().replace(microsecond=0)
print(ct1)
print(type(ct1))

aFormat = "%y_%m_%d_%H_%M_%S"
bFormat = "%y_%B_%d_%H_%M_%S"
cFormat = "%y_%b_%d_%H_%M_%S"
dFormat = "%y_%M_%d_%H_%M_%S"

new_time = datetime.strftime(ct1,cFormat)
print(new_time)

new_time1 = datetime.strftime(ct1,bFormat)
print(new_time1)

new_time2= datetime.strftime(ct1,aFormat)
print(new_time2)

new_time3= datetime.strftime(ct1,dFormat)
print(new_time2)

fi = 'hello'+new_time+'.png'

file = os.path.join(folder,fi)
screen.save(file)
