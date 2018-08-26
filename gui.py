from tkinter import *
import backend

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

window=Tk()

window.wm_title("BookStore Database")

label1=Label(window, text="Title")
label1.grid(row=0, column=0)

label2=Label(window, text="Author")
label2.grid(row=0, column=2)

label3=Label(window, text="Year")
label3.grid(row=1, column=0)

label4=Label(window, text="ISBN")
label4.grid(row=1, column=2)

title_text=StringVar()
entry1=Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)

author_text=StringVar()
entry2=Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)

year_text=StringVar()
entry3=Entry(window, textvariable=year_text)
entry3.grid(row=1, column=1)

isbn_text=StringVar()
entry4=Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=3)

list1=Listbox(window, height=10, width=52)
list1.grid(row=3, column=0, rowspan=7, columnspan=4)

scrollBar=Scrollbar(window)
scrollBar.grid(row=3, column=4, rowspan=6)

list1.configure(yscrollcommand=scrollBar.set)
scrollBar.configure(command=list1.yview)

button1=Button(window, text="View All", width=12, command=view_command)
button1.grid(row=3, column=5)

button1=Button(window, text="Search", width=12, command=search_command)
button1.grid(row=4, column=5)

button1=Button(window, text="Add Entry", width=12, command=add_command)
button1.grid(row=5, column=5)

button1=Button(window, text="Update Entry", width=12)
button1.grid(row=6, column=5)

button1=Button(window, text="Delete Entry", width=12)
button1.grid(row=7, column=5)

button1=Button(window, text="Close App", width=12)
button1.grid(row=8, column=5)

window.mainloop()
