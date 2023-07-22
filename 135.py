import tkinter as tk

def update(value):
    root["bg"] = value.lower()
    # root["bg"] = color.get().lower()

root = tk.Tk()
root.geometry("300x300")
root.title("Colors box")

color = tk.StringVar()
color.set("Select color")

options = [
    "Blue",
    "Red",
    "Green",
    "Black",
    "Yellow"
]

box = tk.OptionMenu(root, color, *options, command=update)
box.pack(anchor="ne", padx=5, pady=5)

root.mainloop()