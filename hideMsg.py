from PIL import Image


im = Image.open('C:/Users/Rafeek/Desktop/pics/dog.png', 'r')
width, height = im.size
pixel_values = list(im.getdata()) #getting all the pixels
newpix = []
counter = 0
string = "hi my name is rafiq" #the message i wanna hide

end = "ENDD" #how to know where the message ends
string = string + end
print(string)
binstr = ""
for i in string: #transforming my message into binary
    binstr+=('{:08b}'.format(ord(i)))


for item in pixel_values:#splitting my the msg binary into two bits, and storing them into the last two bits of each pixel
    f,s,t=item
    bint = bin(t)[2:] #remove 0b from beggining
    newt = ""
    for i in range(0, len(bint) - 2):
        newt += bint[i]
    if counter+2<len(binstr):
        newt += binstr[counter]
        counter += 1
        newt += binstr[counter]
        counter += 1
        t = int(newt, 2)
    newpix.append((f,s,t)) #then appending our new pixel (only t changes because t has the last 2 bits
counter = 0
im1= Image.new('RGB', (width, height)) #creating new image with new pixels
im1.putdata(newpix)
print(list(im1.getdata()))
im1.save('test.png')
