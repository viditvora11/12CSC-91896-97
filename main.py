from tkinter import *

from PIL import Image, ImageTk



class Home:
    def __init__(self, parent):

        self.img_file = Image.open("lost.png")
        self.img_file = self.img_file.resize((130,70))
        self.img_file = ImageTk.PhotoImage(self.img_file)

        self.b1 = Button(parent,image=self.img_file, border = 0, highlightthickness=0, command = self.lost)
        self.b1.place(x=0,y=255)

        self.img_file1 = Image.open("exit.png")
        self.img_file1 = self.img_file1.resize((110,60))
        self.img_file1 = ImageTk.PhotoImage(self.img_file1)

        self.b2 = Button(parent,image=self.img_file1, border = 0, highlightthickness=0, command = self.exit)
        self.b2.place(x=220,y=539)

        self.img_file2 = Image.open("found.png")
        self.img_file2 = self.img_file2.resize((170,74))
        self.img_file2 = ImageTk.PhotoImage(self.img_file2)

        self.b3 = Button(parent,image=self.img_file2, border = 0, highlightthickness=0)
        self.b3.place(x=430,y=255)
      
    def exit(self):
      window.destroy()
  
    def lost(self):
      self.b1.destroy()
      self.b2.destroy()
      self.b3.destroy()
      Lost(window)
      

class Lost:
    def __init__(self, parent):
      
        bg_image2 = Image.open("back2.png") 
        bg_image2 = bg_image2.resize((600,600),Image.ANTIALIAS)
        bg_image2 = ImageTk.PhotoImage(bg_image2) 
        image_label.configure(image = bg_image2) 
        image_label.image=bg_image2

        self.img_file2 = Image.open("found.png")
        self.img_file2 = self.img_file2.resize((170,74))
        self.img_file2 = ImageTk.PhotoImage(self.img_file2)


       
      
if __name__== "__main__": 
    window = Tk()
    window.title("Lost and Found MRGS")
    window.geometry("600x600")
    bg_image = Image.open("back.png")
    bg_image = bg_image.resize((600,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = Home(window)

    window.mainloop()