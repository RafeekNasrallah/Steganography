# Steganography
Hide/Find message in image 

Wikipedia : Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video

In this tiny project, i deicded to make a GUI application, where you can hide a message in an image, and you can look it up again in the future.

Algorithm:
each image is built from alot of pixels, pixels in png are 32 bits and in jpg are 24.
in this project i will be working with png images only.
the idea is to transform the message to binary, and store the whole binary message in the pixels, in order to keep the photo as similar as the original,i just change the last two bits from each pixel.

how to run:
1. run terminal

2. clone the project

3. cd to the directory

4. type 
```
python3 GUI.py
```

How to use:
after running the program:
Hiding the Message:

1. choose an image with the button browse.
2. write the message you want to hide.
3. Click Hide! button

then the program will generate a new image called lastproduct.png in the same directory as your original image.

Find the Message:
1. choose an image with the button browse (usually its called lastproduct,png unless you changed its name)
2. press Find! button

you will see the message under the button
