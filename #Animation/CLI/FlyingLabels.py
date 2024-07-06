import os 
from time import sleep as delay
from random import choice as ch
term=os.get_terminal_size()

#print(win.lines)
os.system("clear")
out=lambda s: print(s, end="", flush=True)
coord=lambda x,y: out(f"\033[{y};{x}H")


class win:
 arr=[]
 def __init__(self, xoff, yoff, xlen, ylen, text="hi"):
  self.xoff=xoff
  self.yoff=yoff
  self.xlen=xlen
  self.ylen=ylen  

  self.d_xoff=self.d_yoff=self.d_xlen=self.d_ylen=0
  self.xstep=ch([-1,-2,1,2])
  self.ystep=ch([-1,-2,1,2])
  self.text=text
#  self.d_text=""

  self.wrap=False
  win.arr.append(self)

 def draw():
  for obj in win.arr:
   for y in range(obj.d_ylen):
    coord(obj.d_xoff, obj.d_yoff+y)
    out(" "*obj.d_xlen)
   
   for y in range(obj.ylen):
    coord(obj.xoff, obj.yoff+y)
    if y==0 or y==obj.ylen-1:
     for x in range(obj.xlen):
      if ((y==0 and x==0) or (y==obj.ylen-1 and x==obj.xlen-1) or
          (y==0 and x==obj.xlen-1) or (y==obj.ylen-1 and x==0)): out("#")
      else: out("=")
    else:
     out("|"+(obj.xlen-2)*" "+"|")
   obj.d_xoff=obj.xoff; obj.d_yoff=obj.yoff; obj.d_xlen=obj.xlen; obj.d_ylen=obj.ylen
   if obj.wrap==False:
    for i in range(len(obj.text)):
     coord(obj.xoff+i%(obj.xlen-2)+1, obj.yoff+1)
     out(obj.text[i]) 

 def update(term):
  for obj in win.arr:
   if obj.xoff<2 or obj.xoff+obj.xlen>term.columns: obj.xstep*=-1
   if obj.yoff<2 or obj.yoff+obj.ylen>term.lines: obj.ystep*=-1
   obj.xoff+=obj.xstep
   obj.yoff+=obj.ystep
   
   


win(5,5,len("hi")+2,3,"hi")
win(5, 8, 2+len("Whats up!!!"),3, "Whats up!!!")
win(10, 10, 2+len("GET OFF OF ME!!!"), 3, "GET OFF OF ME!!!!")

game=True


d_term=os.get_terminal_size()
text="GET OFF OF ME!!!!!"
while game:
 term=os.get_terminal_size()
 if term!=d_term: os.system("clear"); d_term=term
 win.draw()
 win.update(term) 

# win.arr[1].xoff+=d_x
# if win.arr[1].xoff+win.arr[1].xlen>term.columns or win.arr[1].xoff<2: d_x*=-1
# win.arr[2].yoff+=d_y
# if win.arr[2].yoff+win.arr[2].ylen>term.lines or win.arr[2].yoff<2: d_y*=-1

# win.arr[2].text=text[:win.arr[2].yoff%len(text)]
# coord(2+i,2)
# out(text[i])
 delay(0.05)
