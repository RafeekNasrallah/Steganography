import time
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image
from tkinter import messagebox


name = ""



def findMsg(path):
    if len(path) == 0:
        messagebox.showinfo("no Photo", "Please choose a photo")
        return
    print("im in")
    im = Image.open(path, 'r')
    pixel_values = list(im.getdata())
    strb = ""
    for item in pixel_values: #getting last two bits of each pixel and combining them together
        f, s, t = item
        bint = bin(t)
        if len(bint) < 3:
            strb += '0'
            strb += '0'
        else:
            if len(bint) == 3:
                strb += '1'
                strb += '0'
            else:
                strb += bint[len(bint) - 2]
                strb += bint[len(bint) - 1]
    big = len(strb)
    counter = 0
    pixels = []
    byte = ""
    while counter < big:#storing all the bits in a list of bytes (each 8 bits together)
        for i in range(counter, counter + 8):
            byte += strb[i]
        counter += 8
        pixels.append(byte)
        byte = ""
    string = ""
    end = "a"
    for item in pixels: # transforming each byte to char and putting them together to get our new String
        if len(end) == 3:
            end = end[1:]
        n = int(item, 2)
        end += chr(n)
        string +=chr(n)
        if end == "END":
            break
    string = string[:-3]
    print(string)
    label = canvas1.create_text(200,350,fill="black",font="Times 11 italic bold",
                        text=string)




def hideMsg(path):

    msg = entry1.get()
    print(msg)
    if len(path) == 0:
        messagebox.showinfo("no Photo", "Please choose a photo")
        return
    im = Image.open(path, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())  # getting all the pixels
    newpix = []
    counter = 0
    string = msg  # the message i wanna hide
    end = "ENDD"  # how to know where the message ends
    string = string + end
    print(string)
    binstr = ""
    if (len(msg)*8)/2 > len(pixel_values):
        messagebox.showinfo("Too long", "Your message is too long, please choose the photo and another text.")
        return
    for i in string:  # transforming my message into binary
        binstr += ('{:08b}'.format(ord(i)))
    for item in pixel_values:  # splitting my the msg binary into two bits, and storing them into the last two bits of each pixel
        f, s, t = item
        bint = bin(t)[2:]  # remove 0b from beggining
        newt = ""
        for i in range(0, len(bint) - 2):
            newt += bint[i]
        if counter + 2 < len(binstr):
            newt += binstr[counter]
            counter += 1
            newt += binstr[counter]
            counter += 1
            t = int(newt, 2)
        newpix.append((f, s, t))  # then appending our new pixel (only t changes because t has the last 2 bits
    counter = 0
    im1 = Image.new('RGB', (width, height))  # creating new image with new pixels
    im1.putdata(newpix)
    print(list(im1.getdata()))
    last = 0
    for counter, value in enumerate(path):
        if value == '/':
            last = counter
    cut = len(path)-last
    path = path[:-cut]
    path = path + "/lastproduct.png"
    print(path)
    im1.save(path,'PNG')



def browse_button():
    global folder_path
    global name
    filename = askopenfilename()
    folder_path.set(filename)
    name = filename
    ending = name[-4:]
    if ending != ".png" and ending != ".jpg":
        name = ""
        messagebox.showinfo("Title", "Please insert an png or jpg image only!")

root = tk.Tk()
root.geometry("500x500")
folder_path = StringVar()
canvas1 = tk.Canvas(root, width = 500, height = 500)
canvas1.pack()
lbl1 = Label(master=root,textvariable=folder_path)
button2 = Button(text="Browse", command=browse_button)
canvas1.create_window(200, 30, window=button2)
canvas1.create_line(0, 50, 500, 50)
canvas1.create_text(200,70,fill="black",font="Times 20 italic bold",
                        text="Hide message")
#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
canvas1.create_text(70,140,fill="black",font="Times 10 italic bold",
                        text="Type your message")
entry1 = tk.Entry (root,width="50")

canvas1.create_window(280, 140, window=entry1)
button1 = tk.Button(text='hide', command=lambda: hideMsg(name))
canvas1.create_window(200, 180, window=button1)
canvas1.create_line(0, 200, 500, 200)
canvas1.create_text(200,230,fill="black",font="Times 20 italic bold",
                        text="Find message")
button3 = tk.Button(text='Find', command=lambda: findMsg(name))
canvas1.create_window(200, 285, window=button3)
mainloop()
