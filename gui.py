from tkinter import *
from backend import Database

database=Database("bookList.db")

class Window(object):

    def __init__(self,window):

        self.window = window

        self.window.wm_title("BookStore Database")

        label1=Label(window, text="Title")
        label1.grid(row=0, column=0)

        label2=Label(window, text="Author")
        label2.grid(row=0, column=2)

        label3=Label(window, text="Year")
        label3.grid(row=1, column=0)

        label4=Label(window, text="ISBN")
        label4.grid(row=1, column=2)

        self.title_text=StringVar()
        self.entry1=Entry(window, textvariable=self.title_text)
        self.entry1.grid(row=0, column=1)

        self.author_text=StringVar()
        self.entry2=Entry(window, textvariable=self.author_text)
        self.entry2.grid(row=0, column=3)

        self.year_text=StringVar()
        self.entry3=Entry(window, textvariable=self.year_text)
        self.entry3.grid(row=1, column=1)

        self.isbn_text=StringVar()
        self.entry4=Entry(window, textvariable=self.isbn_text)
        self.entry4.grid(row=1, column=3)

        self.list1=Listbox(window, height=10, width=52)
        self.list1.grid(row=3, column=0, rowspan=7, columnspan=4)

        scrollBar=Scrollbar(window)
        scrollBar.grid(row=3, column=4, rowspan=6)

        self.list1.configure(yscrollcommand=scrollBar.set)
        scrollBar.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        button1=Button(window, text="View All", width=12, command=self.view_command)
        button1.grid(row=3, column=5)

        button1=Button(window, text="Search", width=12, command=self.search_command)
        button1.grid(row=4, column=5)

        button1=Button(window, text="Add Entry", width=12, command=self.add_command)
        button1.grid(row=5, column=5)

        button1=Button(window, text="Update Entry", width=12, command=self.update_command)
        button1.grid(row=6, column=5)

        button1=Button(window, text="Delete Entry", width=12, command=self.delete_command)
        button1.grid(row=7, column=5)

        button1=Button(window, text="Close App", width=12, command=window.destroy)
        button1.grid(row=8, column=5)

    def get_selected_row(self, event):
        try:
            index=self.list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)
            self.entry1.delete(0, END)
            self.entry1.insert(END, self.selected_tuple[1])
            self.entry2.delete(0, END)
            self.entry2.insert(END, self.selected_tuple[2])
            self.entry3.delete(0, END)
            self.entry3.insert(END, self.selected_tuple[3])
            self.entry4.delete(0, END)
            self.entry4.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def update_command(self):
        database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())

    def delete_command(self):
        database.delete(self.selected_tuple[0])

window=Tk()
Window(window)
window.mainloop()
