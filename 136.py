from tkinter import *

def add():
    name   = fields["name_entry"].get()
    gender = dropdown_value.get()

    if name and gender != "Select":
        fields["list"].insert(END, "%s, %s" %(name, gender))
        fields["name_entry"].delete(0, END)
        dropdown_value.set("Select")

root = Tk()
root.geometry("500x350")
root.title("Dropdown and Listbox")

fields = {}
dropdown_value = StringVar()
dropdown_value.set("Select")

first = Frame()
first.pack(fill=X)

fields["name_label"] = Label(first, text="Enter name")
fields["name_label"].pack(fill=X, expand=True, side=LEFT, padx=5, pady=5)

fields["name_entry"] = Entry(first)
fields["name_entry"].pack(fill=X, expand=True, side=RIGHT, padx=5, pady=5)

second = Frame()
second.pack(fill=X)

fields["dropdown_label"] = Label(second, text="Select gender")
fields["dropdown_label"].pack(fill=X, expand=True, side=LEFT, padx=5, pady=5)

fields["dropdown"] = OptionMenu(second, dropdown_value, *["Male","Female"])
fields["dropdown"].pack(fill=X, expand=True, side=LEFT, padx=5, pady=5)

# Populating Listbox with data using Variable
data = StringVar(value=("Andrew, Male", "Cristine, Female"))

fields["list"] = Listbox(root, listvariable=data)
fields["list"].pack(fill=X, padx=10, pady=10, ipadx=5, ipady=5)

fields["btn"] = Button(text="Add new entry", command=add)
fields["btn"].pack(fill=X)

root.mainloop()