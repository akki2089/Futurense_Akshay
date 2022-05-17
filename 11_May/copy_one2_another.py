import shutil
from tkinter import filedialog as fd
import os

source_path = fd.askdirectory()
file_name = input("enter the filename with extension")
source_file_path = os.path.join(source_path,file_name)
dest_path = fd.askdirectory()
shutil.copy(source_file_path, dest_path)
print("completed")