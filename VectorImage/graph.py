from fig import *

Pic=VecImage("graph", 100,100,"gray")

centre=(40,40)
R=10
a=(20,20)
r=4

Circle(*centre, R, svg=Pic, swidth=0.1)

Circle(*centre, R, svg=Pic, swidth=0.1)

Pic.save()