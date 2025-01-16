import tkinter as tk
from PIL import Image, ImageEnhance, ImageTk
import os
from tkinter import filedialog, ttk

window = tk.Tk()
window.geometry("800x800")

frame = ttk.Frame(window, width=800, height=800)
frame.pack()

canvas = tk.Canvas(frame, width=600, height=600)
canvas.configure(bg="gray")
canvas.pack()

var = tk.DoubleVar()

file_path = filedialog.askopenfilename()
im = Image.open(file_path)
enhancer = ImageEnhance.Brightness(im)

dir = os.path.dirname(im.filename)
filename = os.path.basename(im.filename)

resized = im.resize((600, int(600*(im.height/im.width))))
tk_i = ImageTk.PhotoImage(resized)
img = canvas.create_image(300, 300, image=tk_i)

latest_image = img
def set_image_brightness(v: float):
    global latest_image

    #informal var names, i know. Its just a quick code markup
    enhanced_im = enhancer.enhance(1+var.get()/100)
    latest_image = enhanced_im
    resized = enhanced_im.resize((600, int(600*(im.height/im.width))))
    tk_im = ImageTk.PhotoImage(resized)
    new_img = canvas.create_image(300, 300, image=tk_im)
    canvas.itemconfig(img, image=new_img)
slider = ttk.Scale(
    frame,
    from_=-100,
    to=200,
    orient='horizontal',
    variable=var,
    length=100
)
slider.bind("<ButtonRelease-1>", set_image_brightness)
slider.configure(length=400)
slider.pack(side=tk.BOTTOM)

def save():
    latest_image.save(filedialog.asksaveasfilename(
        initialfile=filename,
        initialdir=dir,
        filetypes=[("all","*")],
        title=filename, 
        confirmoverwrite=True), 
        "png"
        )
save_button = ttk.Button(
    frame,
    text="save",
    command=save
)
save_button.pack(side=tk.BOTTOM)

window.mainloop()
