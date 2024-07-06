import os
from time import sleep
width,height=os.get_terminal_size()
heart=[
 "00010001000",
 "00222022200",
 "03333333330",
 "04444444440",
 "00555555500",
 "00066666000",
 "00007770000",
 "00000100000"    
]
pic_height, pic_width=len(heart), len(heart[0])

#print("\033[2m Hello \033[0m")
#print("\033[3m worrld \033[0m") 
x=50
y=10

def set_pos(x,y):
 print(f"\033[{y};{x}H", end="", flush=True)
def draw_pixel(i):
 print(f'\033[{40+i%8}m \033[40m', end="", flush=True)

def draw_pic(array,x,y,color):
 for i in array:
  set_pos(x,y)
  dx=x
  for j in i:
   if j=="0": set_pos(dx,y)
   else: draw_pixel(color)
   dx+=1
  y+=1

def draw_pic_rgb(array,x,y):
 for i in array:
  set_pos(x,y)
  for j in i:
   draw_pixel(int(j))
  y+=1


os.system("cls")
game=True
x,y=10,10
xstep,ystep=1,1
while game:
 draw_pic(heart, (width-pic_width)//2, (height-pic_height)//2, 4)
 draw_pic(heart, x,y,0)
 if x+xstep+pic_width>width: xstep=-1
 elif x+xstep<0: xstep=1
 if y+ystep+pic_height>height: ystep=-1
 elif y+ystep<0: ystep=1

 
 x+=xstep
 y+=ystep
 draw_pic(heart, x,y,2)
 sleep(0.1)

#print('\033[41m \033[40m', end="")
