from fig import *

Pic=VecImage("pic", 70, 70, "white")
#########################################
class Arrow:
 w=6
 h=10
 color="black"

arrowR = Polygon(
 coords=[(Arrow.w/2,Arrow.h/2),
         (0,0),
         (Arrow.w, Arrow.h/2),
         (0,Arrow.h)],
#         color=Arrow.color, 
          swidth=0.5,
#         style="background:white"
         color="context-stroke"
 )
arrowL = Polygon(
 coords=[(0,Arrow.h/2),
         (Arrow.w,0),
         (Arrow.w/2, Arrow.h/2),
         (Arrow.w,Arrow.h)],
#         color=Arrow.color, 
          swidth=0.5,
#         style="background:white"
         color="context-stroke"
 )
Marker("arrowRight", Arrow.w,Arrow.h/2, 
       Arrow.w, Arrow.h,
       arrowR, svg=Pic)
Marker("arrowLeft", 0,Arrow.h/2, 
       Arrow.w, Arrow.h,
       arrowL, svg=Pic)
###########################################
class main:
 x=25
 y=50
 r=60
 r1=r*(3)**(1/2)/3
 centre=(x+r/2, y-r*(3)**(1/2)/6)
 swidth=0.2
 dash=(5,4)
Q1=1
Q4=-0.58

k=600

Culon = lambda Q1,Q2,r: -k*Q1*Q2/(r**2)
print(Culon(Q1,Q1, main.r1))
# draw triangle
Tri=PLine(
 coords=[#Triangle
         (main.x,main.y), 
         (main.x+main.r, main.y), 
         (main.x+main.r/2, main.y-main.r*(3)**(1/2)/2),
         (main.x, main.y),
          # paral
         (main.x+main.r*Culon(Q1,Q1, main.r),main.y),
         (main.x+(main.r+main.r/2)*Culon(Q1,Q1, main.r),
          main.y-(main.r*(3)**(1/2)/2)*Culon(Q1,Q1,main.r)),
         (main.x+(main.r/2)*Culon(Q1,Q1, main.r),
          main.y-(main.r*(3)**(1/2)/2)*Culon(Q1,Q1,main.r)),
          (main.x, main.y)
         ],
 svg=Pic, swidth=main.swidth, dash=main.dash, scolor="black")

for i in Tri.coords[:3]:
 Line(i[0], i[1], *main.centre, 
      svg=Pic, swidth=main.swidth, dash=main.dash)
#####
# draw force Arrows:
# main -> rightdown
for i in range(3):
 Line(*Tri.coords[0], *Tri.coords[4+i],
      svg=Pic, swidth=0.4, arr=("", "arrowRight"))
#### ################
le=0.18
sw=0.3
vec=((main.centre[1]-main.y)*le, (-main.centre[0]+main.x)*le)

A=Line(*Tri.coords[0], vec[0]+Tri.coords[0][0],vec[1]+Tri.coords[0][1],
      svg=Pic, swidth=sw)
B=Line(*main.centre, vec[0]+main.centre[0],vec[1]+main.centre[1],
      svg=Pic, swidth=sw)
Line(*A.coords[1], *B.coords[1], 
     svg=Pic, swidth=sw, arr=("arrowLeft", "arrowRight"))




#draw electrons
rad=1.2
swid=0.4
k=0.9
for i in Tri.coords[:3]:
 Circle(*i, r=rad*2, svg=Pic, swidth=swid)
 Line(i[0]-rad*k, i[1], i[0]+rad*k, i[1], svg=Pic, swidth=swid)
 Line(i[0], i[1]-rad*k, i[0], i[1]+rad*k, svg=Pic, swidth=swid)
Circle(*main.centre, r=rad*2, svg=Pic, swidth=swid)
Line(main.centre[0]-rad*k, main.centre[1], 
     main.centre[0]+rad*k, main.centre[1], 
     svg=Pic, swidth=swid)
#########################
Pic.save()