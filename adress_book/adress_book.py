from tkinter import * 
from tkinter.filedialog import * 
from tkinter import messagebox
import os 

#fonctions 
my_address_book = {}

def open_file():
    global my_address_book
    reset()
    open_file = askopenfile(mode = "r")
    if open_file is not None:
        my_address_book = eval(open_file.read())
        for key in my_address_book.keys():
            listbox.insert(END, key)
        title.config(text = os.path.basename(open_file.name))
    else:
        messagebox.showwarning("WARNING", "No address book selected")

def save_file():
    global my_address_book
    save_file = asksaveasfile(defaultextension = ".txt")
    if save_file:
        print(my_address_book, file = save_file)
        reset()
    else:
        messagebox.showwarning("WARNING", "Adress book not saved")

def reset():
    global my_address_book
    clear_all()
    listbox.delete(0, END)
    my_address_book.clear()

def clear_all():
    name_entry.delete(0, END)
    address_entry.delete(0, END)
    mobile_entry.delete(0, END)
    email_entry.delete(0, END)
    birthday_entry.delete(0, END)

def update():
    key = name_entry.get()
    if key == "":
        messagebox.showwarning("ERROR", "Name is required")
    else:
        if key not in my_address_book.keys():
            listbox.insert(END, key)
        my_address_book[key] = (address_entry.get(), mobile_entry.get(), email_entry.get(), birthday_entry.get())
        clear_all()

def edit():
    clear_all()
    index = listbox.curselection()
    if index:
        #auto fill 
        name_entry.insert(0, listbox.get(index))
        details = my_address_book[name_entry.get()]
        address_entry.insert(0, details[0])
        mobile_entry.insert(1, details[1])
        email_entry.insert(2, details[2])
        birthday_entry.insert(3, details[3])
    else:
        messagebox.showwarning("Error", "Please select a name from the list")

def delete():
    index = listbox.curselection()
    if index:
        listbox.delete(index)
        del my_address_book[listbox.get(index)]
        clear_all()
    else:
        messagebox.showwarning("Error", "No selection made")

def display(event):
    new_window = Toplevel(window)
    index = listbox.curselection()
    contact = ""
    if index:
        key = listbox.get(index)
        contact = "NAME     : " + key + "\n\n"

        details = my_address_book[key]
        contact += "ADDRESS  : " + details[0] + "\n"
        contact += "MOBILE   : " + details[1] + "\n"
        contact += "EMAIL    : " + details[2] + "\n"
        contact += "BIRTHDAY : " + details[3] + "\n"
    else: 
        messagebox.showwarning("ERROR", "Nothing to display")
    
    label = Label(new_window)
    label.pack()
    label.config(text = contact)

window = Tk()
window.title("Adress Book")
window.geometry("500x500")

#entry + listbox
listbox = Listbox(window, width = 26, height = 20)
listbox.bind("<<ListboxSelect>>", display)
name_entry = Entry(window, width = 15)
address_entry = Entry(window, width = 15)
mobile_entry = Entry(window, width = 15)
email_entry = Entry(window, width = 15)
birthday_entry = Entry(window, width = 15)

listbox.grid(row = 2, column = 1, rowspan = 5, columnspan = 2, pady = 10, padx = 10)
name_entry.grid(row = 2, column = 4)
address_entry.grid(row = 3, column = 4)
mobile_entry.grid(row = 4, column = 4)
email_entry.grid(row = 5, column = 4)
birthday_entry.grid(row = 6, column = 4)

#labels
title = Label(window, text = "My address book:", font = ("times", 20))
title.grid(row = 1, column = 1)
name_label = Label(window, text = "Name:", font = ("times", 20)).grid(row = 2, column = 3)
adress_label = Label(window, text = "Address:", font = ("times", 20)).grid(row = 3, column = 3)
mobile_label = Label(window, text = "Mobile:", font = ("times", 20)).grid(row = 4, column = 3)
email_label = Label(window, text = "Email:", font = ("times", 20)).grid(row = 5, column = 3)
birthday_label = Label(window, text = "Birthday:", font = ("times", 20)).grid(row = 6, column = 3)

#buttons
edit_button = Button(window, text = "Edit", font = ("times", 17), command = edit).grid(row = 7, column = 1, pady = 10)
delete_button = Button(window, text = "Delete", font = ("times", 17), command = delete).grid(row = 7, column = 2)
open_button = Button(window, text = "Open", font = ("times", 17), command = open_file).grid(row = 1, column = 3)
update_button = Button(window, text = "Update/Add", font = ("times", 17), command = update).grid(row = 7, column = 4)
save_button = Button(window, text = "Save", font = ("times", 17), width = 23, command = save_file).grid(row = 8, column = 1, columnspan = 2)

window.mainloop()