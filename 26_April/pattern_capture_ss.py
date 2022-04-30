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
file = os.path.join(folder,'h.jpg')
screen.save(file)