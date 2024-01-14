#Import Required Modules
import time
from PIL import Image

#Generate number based on time
current_time = int(time.time())
generated_number = (current_time % 100) + 50

#If number is even increase by 10
if generated_number % 2 == 0:
    generated_number += 10

print("Number Generated Based on time = " + str(generated_number))

#Open image, store dimensions and load pixel map  
img = Image.open("Assignment 2\chapter1.jpg")
width, height = img.size
pixels = img.load()

redkey = 0
#Iterate over all pixels in the image
for x in range(width):
    for y in range(height):
        #get rbg values of pixel, add generated number to pixels
        r,g,b = img.getpixel((x,y))
        pixels[x,y] = (r+generated_number, g+generated_number, b+generated_number)
        #get new rgb values, store r value
        r,g,b = img.getpixel((x,y))
        redkey += r

print("Total value of all redpixels in new image = " + str(redkey))
#Save new image
img.save("Assignment 2\chapter1out.png")

