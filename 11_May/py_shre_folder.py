from flask import send_file, send_from_directory, abort
from flask import Flask
from tkinter import filedialog as fd
import os


folder=fd.askdirectory()
file_name = input("enter the file_name with extension to be shared")
global source_path
source_path = os.path.join(folder,file_name)
app = Flask(__name__)
# The absolute path of the directory containing PDF files for users to download
app.config["CLIENT_PDF"] = source_path


@app.route("/")
def get_image():

    try:
        return send_from_directory(app.config["CLIENT_PDF"], filename=source_path, as_attachment=True)
    except FileNotFoundError:
        abort(404)
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
app.run(host='0.0.0.0', port=80)