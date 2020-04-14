# Steganography
Hide/Find message in image 

Wikipedia : Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video

In this tiny project, i deicded ti make a GUI application, where you can hide a message in an image, and you can look it up again in the future.

Algorithm:
each image is built from alot of pixels, each pixel containt 24 bits (RBG).
the idea is to transform the message to binary, and store the whole binary message in the pixels, in order to keep the photo as similar as the oroginal,i just change the last two bitsfrom each pixel.

how to run:
1. run terminal

2. clone the project

3. cd to the directory

4. type 
```
python3 GUI.py
```
