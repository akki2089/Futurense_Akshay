import os
import sqlite3
from tkinter import filedialog as fd
from PyPDF2 import PdfFileWriter, PdfFileReader
from datetime import datetime
import mysql.connector

folder=fd.askdirectory()
#print(folder)
files=os.listdir(folder)
#print(files)

#read the pdf files one  by one
for file in files:
        if(file.endswith(".pdf")):
            #if pdf is already encrypted ignore
            # if not do
            #read the pdf
            name = os.path.join(folder, file)
            with open(name,'rb') as f:
                out = PdfFileWriter()
                input = PdfFileReader(f)
                num = input.numPages
                for idx in range(num):
                    # Get the page at index idx
                    page = input.getPage(idx)
                    # Add it to the output file
                    out.addPage(page)
                    password = file[:-4]
                    out.encrypt(password)
                    #create dynamic nature in saving your file
                    curr=datetime.now().replace(microsecond=0)
                    format="%y_%b_%d_%H_%M_%S"
                    new_format= datetime.strftime(curr,format)
                    file_n = file[:-4] + new_format + ".pdf"
                    # save it with timestamp
                    filename = os.path.join(folder, file_n)

                    with open(filename, "wb") as k:
                        out.write(k)
                    #write the content like name,size,password in database

                    db = mysql.connector.connect(host='localhost',
                                         database='training',
                                         user='root',
                                         password='akki')

                    cursor = db.cursor()
                    cursor.execute("CREATE DATABASE datacamp")
                    cursor.execute("CREATE TABLE files (filename VARCHAR(255), flz integer,pwd VARCHAR(255))")
                    query = "INSERT INTO files (filename,filesize,pwd) VALUES (%s, %s)"
                    values = ("x", 8, 'sal')
                    cursor.execute(query, values)
                    query = "SELECT * FROM users"

                    cursor.execute(query)

                    ## fetching all records from the 'cursor' object
                    records = cursor.fetchall()

                    ## Showing the data
                    for record in records:
                        print(record)







