from tkinter import *

from PIL import Image, ImageTk

lost = []


class Start:
    def __init__(self, parent):
        self.quiz_frame =Frame(parent)
        self.quiz_frame.pack() 

if __name__== "__main__": 
    window = Tk()
    window.title("Lost and Found MRGS")
    window.geometry("700x600")
    bg_image = Image.open("back.png")
    bg_image = bg_image.resize((700,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = Start(window)

    window.mainloop()