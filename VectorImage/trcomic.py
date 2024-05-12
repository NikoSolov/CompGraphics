
from fig import *
from PIL import Image
im = Image.open('comic.png')
print(im.size) # (width,height) tuple

Pic=VecImage(name = "comic", 
             width = im.size[0],
             height = im.size[1],
             bgcolor="white")

RastImage(path='comic.png', svg=Pic)

class Box:
    x=1010 
    y=140

#Line(Box.x, 0, Box.x, im.size[1],svg=Pic)
#Line(0,Box.y,im.size[0], Box.y,svg=Pic)

TextBox("Is there \nany good \nphoto editing \ntools?", 
        anchor="middle", color="#334676",
        x=480, y=120, fsize=30, svg=Pic, vspace=0)

TextBox("Why not \ntry Fofor? \nThat's \npretty \ngood! ", 
        anchor="middle", color="#334676",
        x=1010, y=140, fsize=30, svg=Pic, vspace=0)

TextBox("Why not \ntry Fofor? \nThat's \npretty \ngood! ", 
        anchor="middle", color="#334676",
        x=Box.x, y=Box.y, fsize=30, svg=Pic, vspace=0)

#It must be
#expensive
#to use

Pic.save()