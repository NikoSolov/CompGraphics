import os
from time import sleep as delay
from math import sin, radians
#=============================================
setPos=lambda x,y: print("\033["+str(y)+";"+str(x)+"H", end="")
out=lambda string: print(string, end="")
clear=lambda: print("\033[2J", end="")
clear2=lambda: os.system("cls")
#=============================================
class win():
 def __init__(self,x,y,width,height):
  self.x=x
  self.y=y
  self.width=width
  self.height=height

size=list(os.get_terminal_size())
wind=win(10,10,20,10)

game=True
t=0
while game:
 clear2()
 for i in range(wind.height):
  setPos(int(sin(radians((i+t)*30))*5)+wind.x, wind.y+i)
  if i==0 or i==wind.height-1:
   out("#"+"="*(wind.width-2)+"#")
  else:
   out("|"+" "*(wind.width-2)+"|")
 t+=1
 print(flush=True)
 delay(0.05) 


