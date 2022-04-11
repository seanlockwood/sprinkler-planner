# Program to help design outdoor sprinkler coverage

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog


#Open a file
def open_file():
    global image_container
    filepath = filedialog.askopenfilename(title="Open a file", filetypes=[("JPG Files", "*.jpg"), ("All Files", "*.*")])
    if not filepath:
        return
    global load
    load = ImageTk.PhotoImage(Image.open(filepath))
    canvas_widget.create_image(100, 80, anchor="nw", image=load)
    root.title(f"Simple Editor - {filepath}")

#Save the current file as a new file
def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPG Files", "*.jpg"), ("All Files", "*.*")])
    if not filepath:
        return
    return


root = tk.Tk()
root.title("Sprinkler Test")

#Customize the root layout so we have 1 narrow column for the buttons and 1 large column for our canvas
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

#Create the widgets
frame_buttons = tk.Frame(root, relief=tk.RAISED, bd=2)
button_clear = tk.Button(frame_buttons, text="Clear")
button_save = tk.Button(frame_buttons, text="Save As...")
button_open = tk.Button(frame_buttons, text="Open", command=open_file)
canvas_widget = tk.Canvas(root, cursor="dot")

#Attach the frame and canvas
frame_buttons.grid(row=0, column=0, sticky="ns")
canvas_widget.grid(row=0, column=1, sticky="nsew")

#Attach buttons to the frame
button_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
button_clear.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

root.mainloop()


