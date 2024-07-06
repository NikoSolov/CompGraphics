import os
from time import sleep
s="hello, world!!!\n"

#def print_char(x,y,char):

HEADER='\033[93m'

def print_at(x,y, text):
 print("\033["+str(y)+";"+str(x)+"H"+text, flush=True)

os.system("cls")
size=list(os.get_terminal_size())
#size=[55,22]
#print(size, size[0], size[1])
#print_at(2,2,"#")
#print_line(5,5,17,19)
game=True

x=2
y=2
xstep=1
ystep=1

while game:
# os.system("clear")
 print_at(x,y,"#")
 size=list(os.get_terminal_size())
 if y>size[1]-2 or y<2:
  ystep*=-1
 if x>=size[0] or x<2:
  xstep*=-1
 x+=xstep
 y+=ystep
 sleep(1/165)

