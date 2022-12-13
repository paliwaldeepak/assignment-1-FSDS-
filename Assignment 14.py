#!/usr/bin/env python
# coding: utf-8

# 1. What does RGBA stand for?

# #ans:- RGBA stand for Red-Green-Blue-Alpha

# 2. From the Pillow module, how do you get the RGBA value of any images?

# In[4]:


#ans:- 
from PIL import Image
img = Image.open("deep.png")
rgba = img.convert("RGBA")
datas = rgba.getdata()


# 3. What is a box tuple, and how does it work?

# #ans:- A tuple is a collection of python objects that are separated by commas which are ordered and immutable. Tuples are sequences, just like lists. The differences between tuples and lists are, that tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

# 4. Use your image and load in notebook then, How can you find out the width and height of an Image object?

# In[6]:


#ans:- 
# import required module
from PIL import Image

# get image
file = "deep.png"
img = Image.open(file)

# get width and height
width = img.width
height = img.height

# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)


# 5. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?

# #ans:- Set the cropping area with box=(left, upper, right, lower).
# 
# The top left coordinates correspond to (x, y) = (left, upper), and the bottom right coordinates correspond to (x, y) = (right, lower). The area to be cropped is left <= x <right and upper <= y <lower, and the pixels of x = right andy = lower are not included.

# 6. After making changes to an Image object, how could you save it as an image file?

# #ans:-To save images, we can use the PIL. save() function

# 7. What module contains Pillow’s shape-drawing code?

# #ans:-The Pillow module provides the open() and show() function to read and display the image respectively.

# 8. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?

# #ans:- Generate Pencil Sketch from Photo in Python
