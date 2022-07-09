from tkinter import *
import pyautogui
from PIL import ImageTk, Image
# this is to make png nd jpeg images accessable in the python tkinter

root = Tk()
root.title("This is title")


'''#Creating a lable widget
mylabel1 = Label(root, text="Hello World!",fg="red")
mylabel2 = Label(root, text="Name is himxnshu",bg="red").pack()
mylabel1.pack() # shoving onto the screen
# lable 1 se pehle lable2 pack hua to phla lable1 nahi 2 hoga'''

'''def myclick():
    mylabel = Label(root,text="okay!").pack()

mybutton0 = Button(root, text="Submit",fg="red").pack() # here yoy can use hex color code also
mybutton1 = Button(root, text="SubmitD", state=DISABLED).pack()
mybutton4 = Button(root, text="xpadding",padx ='20',pady="20").pack()
mybutton5 = Button(root, text="Function Bulaao", command=myclick, bg="Yellow").pack()'''


# creating input fields
'''def mclick():
    mylabel = Label(root, text = "Helo "+ett.get()).pack()

ett = Entry(root,width='30',borderwidth="5")
ett.pack() # here also fg, bg
ett.insert(0, "Enter You Name : ") # by default will insert some text inside the entry
button = Button(root,text="....",command=mclick).pack()'''


'''# using icons, images and exit buttons

# method of using icons into the window
root.iconbitmap('C:/Users/dell/Downloads/icons8-beaming-face-with-smiling-eyes-96.ico')

# exit button 
button_quit = Button(root, text="Exit Program", command = root.quit)
button_quit.pack() # to put it into window

# using images (only two types of images is supported one is gif)
myimg = ImageTk.PhotoImage(Image.open('C:/Users/dell/Downloads/PicsArt_09-30-07.31.07.png'))
mylabel = Label(image = myimg)
mylabel.pack()'''

# BUILT A IMAGE VIEWER

# ADDING FRAMES TO OUR PROGRAM
frame = LabelFrame(root, text="Frame Title", padx=5, pady=5,)
frame.pack(padx=100, pady=100)

b = Button(frame, text="Don't click !!")
b.grid(row = 0, column = 0) # we can also do the grid inside the frame

b2= Button(frame, text="Don't click it!!")
b2.grid(row = 1, column = 1)

# radio buttons

r = IntVar()

Radiobutton(root, text="Option1", variable = r, value = 1).pack()
Radiobutton(root, text="Option2", variable = r, value = 2).pack()


root.mainloop()