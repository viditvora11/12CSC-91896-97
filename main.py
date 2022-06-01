from tkinter import *

from PIL import Image, ImageTk



class Home:
    def __init__(self, parent):

        self.img_file = Image.open("lost.png")
        self.img_file = self.img_file.resize((130,70))
        self.img_file = ImageTk.PhotoImage(self.img_file)

        self.b1 = Button(parent,image=self.img_file, border = 0, highlightthickness=0, command = self.lost)
        self.b1.place(x=59,y=255)

        self.img_file1 = Image.open("exit.png")
        self.img_file1 = self.img_file1.resize((110,60))
        self.img_file1 = ImageTk.PhotoImage(self.img_file1)

        self.b2 = Button(parent,image=self.img_file1, border = 0, highlightthickness=0, command = self.exit)
        self.b2.place(x=293,y=537)

    def exit(self):
      window.destroy()
  
    def lost(self):
      self.b1.destroy()
      self.b2.destroy()


  
      
        
      
if __name__== "__main__": 
    window = Tk()
    window.title("Lost and Found MRGS")
    window.geometry("700x600")
    bg_image = Image.open("back.png")
    bg_image = bg_image.resize((700,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = Home(window)

    window.mainloop()