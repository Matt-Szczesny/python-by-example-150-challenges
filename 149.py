from tkinter import *

fields = {}

def get_number():
    clear_output()
    num = int(fields["num_entry"].get())

    for n in range(1,100):
        calc = num * n
        fields["out_entry"].insert(END, f"{num} x {n} = {calc}")

def clear_output():
    fields["out_entry"].delete(0, END)

def main():
    root = Tk()
    root.title("Times Table")
    root.geometry("470x280")

    layout = {"ipadx": 10, "ipady": 10}

    fields["num_field"] = Label(text="Enter a number: ")
    fields["num_field"].grid(row=0, column=0, **layout)

    fields['num_entry'] = Entry()
    fields["num_entry"].grid(row=0, column=1,padx=15)
    fields["num_entry"].focus()

    fields["out_entry"] = Listbox()
    fields["out_entry"].grid(row=1, column=1)

    fields["view"] = Button(text="View Times Table", width=13, command=get_number)
    fields["view"].grid(row=0, column=2)

    fields["view"] = Button(text="Clear", width=13, command=clear_output)
    fields["view"].grid(row=1, column=2, sticky=N)

    root.mainloop()

main()