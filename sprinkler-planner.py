# Program to help design outdoor sprinkler coverage

from textwrap import fill
import tkinter as tk
from PIL import Image, ImageTk, ImageGrab
from tkinter import filedialog

#Open a file
def open_file():
    global image_container
    filepath = filedialog.askopenfilename(title="Open a file", filetypes=[("JPG Files", "*.jpg"), ("All Files", "*.*")])
    if not filepath:
        return
    global load #Prevent Python garbage collector from deleting the variable before it's shown in the window
    load = ImageTk.PhotoImage(Image.open(filepath))
    canvas_widget.create_image(10, 10, anchor="nw", image=load)
    root.title(f"Simple Editor - {filepath}")

#Save the current file as a new file
def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPG Files", "*.jpg"), ("All Files", "*.*")])
    if not filepath:
        return
    save_widget_as_image(canvas_widget, filepath)

def save_widget_as_image(widget, filename):
    ImageGrab.grab(bbox=(
        widget.winfo_rootx(),
        widget.winfo_rooty(),
        widget.winfo_rootx() + widget.winfo_width(),
        widget.winfo_rooty() + widget.winfo_height()
    )).save(filename)

#Clear the canvas and start fresh
def clear_canvas():
    canvas_widget.delete("all")

root = tk.Tk()
root.title("Sprinkler Test")

#Customize the root layout so we have 1 narrow column for the buttons and 1 large column for our canvas
root.rowconfigure(0, minsize=1000, weight=1)
root.columnconfigure(1, minsize=1000, weight=1)

#Create the widgets
frame_buttons = tk.Frame(root, relief=tk.RAISED, bd=2)
button_clear = tk.Button(frame_buttons, text="Clear", command=clear_canvas)
button_save = tk.Button(frame_buttons, text="Save As...", command=save_file)
button_open = tk.Button(frame_buttons, text="Open", command=open_file)
canvas_widget = tk.Canvas(root, cursor="dot")

#Attach the frame and canvas
frame_buttons.grid(row=0, column=0, sticky="ns")
canvas_widget.grid(row=0, column=1, sticky="nsew")

#Attach buttons to the frame
button_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
button_clear.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

#Test drawing
#Backyard borders
canvas_widget.create_line(125,375,625,375, fill="green", width=5)
canvas_widget.create_line(125,375,125,125, fill="green", width=5)
canvas_widget.create_line(125,125,825,125, fill="green", width=5)
canvas_widget.create_line(825,125,825,525, fill="green", width=5)
canvas_widget.create_line(625,375,625,525, fill="green", width=5)
canvas_widget.create_line(625,525,825,525, fill="green", width=5)

#Sprinkler coord since an ARC is the center of a rectangle with coordinates x0, y0, x1, y1 where x0 & y0 is the top left corner
sprinkler_one_coordinates   =0,0,250,250
sprinkler_two_coordinates   =0,125,250,375
sprinkler_three_coordinates =0,250,250,500
sprinkler_four_coordinates  =250,250,500,500
sprinkler_five_coordinates  =500,250,750,500
sprinkler_six_coordinates   =500,400,750,650
sprinkler_seven_coordinates =0
sprinkler_eight_coordinates =0
sprinkler_nine_coordinates  =0
sprinkler_ten_coordinates   =0
sprinkler_eleven_coordinates=0
sprinkler_twelve_coordinates=0

#Create the arcs
sprinkler_one_arc    = canvas_widget.create_arc(sprinkler_one_coordinates, start=270, extent=90, fill="cyan")
sprinkler_two_arc    = canvas_widget.create_arc(sprinkler_two_coordinates, start=270, extent=180, fill="cyan")
sprinkler_three_arc  = canvas_widget.create_arc(sprinkler_three_coordinates, start=0, extent=90, fill="cyan")
sprinkler_four_arc   = canvas_widget.create_arc(sprinkler_four_coordinates, start=0, extent=180, fill="cyan")
sprinkler_five_arc   = canvas_widget.create_arc(sprinkler_five_coordinates, start=270, extent=270, fill="cyan")
sprinkler_six_arc    = canvas_widget.create_arc(sprinkler_six_coordinates, start=0, extent=90, fill="cyan")

sprinkler_twelve_arc = canvas_widget.create_arc(sprinkler_twelve_coordinates, start=180, extent=180, fill="cyan")

root.mainloop()


