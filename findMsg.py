from PIL import Image

im = Image.open('lastproduct.jpg', 'r')
width, height = im.size
pixel_values = list(im.getdata())
strb = ""
for item in pixel_values: #getting last two bits of each pixel and combining them together
    f, s, t = item
    bint = bin(t) #transors last color G to binary
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
chars = []
end = "a"
for item in pixels: # transforming each byte to char and putting them together to get our new String
        if len(end) == 3:
            end = end[1:]
        n = int(item, 2)
        end += chr(n)
        string +=chr(n)
        if end == "END":
            print("yessssssssss")
            break
string = string[:-3]
print(string)



