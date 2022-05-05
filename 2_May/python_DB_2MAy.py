import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (MainMenu, DBOperation, DML, DDL):
            frame = F(container, self)

            # initializing frame of that object from
            # MainMenu, DBOperation, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame MainMenu

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="MainMenu", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="DBOperation",
                             command=lambda: controller.show_frame(DBOperation))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        # button2 = ttk.Button(self, text="Page 2",
        #                      command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        # button2.grid(row=2, column=1, padx=10, pady=10)


# second window frame DBOperation
class DBOperation(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="DBOperation", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(MainMenu))

        # putting the button in its place
        # by using grid
        button1.grid(row=3, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="DDL",
                             command=lambda: controller.show_frame(DDL))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="DML",
                             command=lambda: controller.show_frame(DML))
        button3.grid(row=1, column=1, padx=10, pady=10)


# third window frame page2
class DML(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Commands of DML", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Select",
                             command=lambda: controller.show_frame(DBOperation))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Select",
                             command=lambda: controller.show_frame(DBOperation))

        # putting the button in its place by
        # using grid
        button3.grid(row=2, column=1, padx=10, pady=10)

        button4 = ttk.Button(self, text="Select",
                             command=lambda: controller.show_frame(DBOperation))

        # putting the button in its place by
        # using grid
        button4.grid(row=3, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button3 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(DBOperation))

        # putting the button in its place by
        # using grid
        button3.grid(row=4, column=1, padx=10, pady=10)


class DDL(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Commands of DDL", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Create",
                             command=lambda: controller.show_frame(DBOperation))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=4, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Alter",
                             command=lambda: controller.show_frame(DBOperation))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Drop",
                             command=lambda: controller.show_frame(DBOperation))

        # putting the button in its place by
        # using grid
        button3.grid(row=3, column=1, padx=10, pady=10)

        button4 = ttk.Button(self,text="Back",
                             command=lambda: controller.show_frame(DBOperation))
        button4.grid(row=4,column=1,padx=10,pady=10)


def display4():
    import tkinter as tk

    # Create a canvas

    T = Text(base, height=20, width=100)
    # Create label
    Fact = """1.create(SYNTAX)-create table table_name (colummn type)(?,?,?)"""
    b2 = Button(base, text="Exit",
                command=base.destroy)

    T.pack()
    b2.pack()

    # Insert The Fact.
    T.insert(tk.END, Fact)
    mainloop()


# Driver Code
app = tkinterApp()
app.mainloop()
