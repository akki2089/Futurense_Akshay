import time
import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter
import threading
from tkinter import *
from tkinter import filedialog
import os


def fun(open_file, x):
    with open(open_file + f"\{x}", "rb") as in_file:
        input_pdf = PdfFileReader(in_file)
        output_pdf = PdfFileWriter()
        output_pdf.appendPagesFromReader(input_pdf)
        output_pdf.encrypt(x[:-4])
        f = datetime.datetime.now().strftime("%y_%m_%d-%H_%M_%S")
        n = datetime.datetime.now().strftime("%H_%M_%S")
        z = x[:-4] + "_" + f + ".pdf"
        with open(open_file + "/" + x[:-4] + "_" + f + ".pdf", "wb") as out_file:
            output_pdf.write(out_file)
        print(time.ctime() + '\n')
        time.sleep(2)


root = Tk()
root.withdraw()
root.attributes('-topmost', True)
open_file = filedialog.askdirectory()
files = os.listdir(open_file)

thread_list = []

for f in files:
    thread_list.append(threading.Thread(target=fun, args=(open_file, f)))

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()