from os import get_terminal_size as term_size
from os import system
from random import randint as rd
from random import choice as ch
from time import sleep as delay

win=term_size()
draw=lambda c: print(f"\033[{c}m \033[40m", end="", flush=True)
coord=lambda x,y: print(f"\033[{y};{x}H", end="", flush=True)
clear=lambda: system("cls")
def cursor_hide(bl):
 if bl: print("\033[?25l", end="", flush=True)
 else:  print("\033[?25h", end="", flush=True)

class dot():
 arr=[]
 def __init__(self, x,y,c):
  self.x=x
  self.y=y
  self.d_x=ch([rd(1,3), -rd(1,3)])*0.1
  self.d_y=ch([rd(1,3), -rd(1,3)])*0.1
  self.c=c
  dot.arr.append(self)
 def draw():
  for obj in dot.arr:
   coord(int(obj.x), int(obj.y))
   draw(obj.c)
   obj.x+=obj.d_x
   obj.y+=obj.d_y
   if obj.x<2 or obj.x>win.columns: obj.d_x*=-1
   if obj.y<2 or obj.y>win.lines: obj.d_y*=-1

for i in range(5):
 dot(rd(0,win.columns-1), rd(0,win.lines-1), ch([rd(41,47), rd(100, 107)]))
clear()

print(win)
print(dot.arr[0].y)
while 1:
 dot.draw()
 delay(0.01)
