# Program to help design outdoor sprinkler coverage

import tkinter as tk
import tkinter.ttk as ttk

from setuptools import Command

def handle_click():
    print("The Button was pressed")

def main():
    window = tk.Tk()
    window.title("Address Entry Form")

    entryLabels = [ "First Name:",
                    "Last Name:",
                    "Address Line 1:",
                    "Address Line 2:",
                    "City:",
                    "State/Province:",
                    "Postal Code",
                    "Country"
                    ]

    # Create new frame to contain the Label and Entry widgets
    frame_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frame_form.pack()

    for index, label in enumerate(entryLabels):
        lbl = tk.Label(master=frame_form, text=label)
        ent = tk.Entry(master=frame_form, width=50)
        lbl.grid(row=index, column=0, sticky="e")
        ent.grid(row=index, column=1)
        
    frameButtons = tk.Frame()
    frameButtons.pack(fill=tk.X, ipadx=5, ipady=5)

    buttonSubmit = tk.Button(master=frameButtons, text="Submit", command=handle_click)
    buttonSubmit.pack(side=tk.RIGHT, ipadx=10)
 

    buttonClear = tk.Button(master=frameButtons, text="Clear")
    buttonClear.pack(side=tk.RIGHT, ipadx=10)

    window.mainloop()


if __name__ == "__main__":
    main()
