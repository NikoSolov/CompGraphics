from random import randint as rd
width,height, count=int(input("width: ")), int(input("height: ")), int(input("count: "))

fel=[]

def print_all(arr):
 print(" ","-"*(width*2+1), sep="")
 for i in arr:
  print(" ",*i, sep="|",end="|\n "+"-"*(width*2+1)+"\n")

for i in range(height):
 c=[]
 for j in range(width):
  c.append("#")
 fel.append(c)

#print(fel)
print_all(fel)

#----- generate minefield------
mines=[]
i=0
while i<count:
 n=rd(0,width*height-1)
 if n not in mines:
  mines.append(n)
  i+=1
print(mines)

field=[]
for y in range(height):
 c=[]
 for x in range(width):
  if height*y+x in mines:
   c.append("x")
  else:
   c.append(" ")
 field.append(c)
del mines

  
#print_all(field)
#print()

for y in range(height):
 for x in range(width):
  if field[y][x]!="x":
   c=0
   for i in range(-1,2):
    for j in range(-1,2):
     if (y+i>=0 and y+i<=height-1 and 
         x+j>=0 and x+j<=width-1 and
         field[y+i][x+j]=="x"):
      c+=1
      
   if c!=0:
    field[y][x]=c

print_all(field)
#-----------------------------------------

for i in range(1000):
 try:
  x,y,c=input("insert command: ").split()
  x,y=int(x),int(y)
  if x>=0 and x<=width and y>=0 and y<=height:
   fel[y][x]=field[y][x]
   print_all(fel)
  else:
   print("Wrong command!!!")

 except:
  print("Wrong command!!!")

#3 4 D - dig
#1x1 M - mark
#3x2 ? - idk 
