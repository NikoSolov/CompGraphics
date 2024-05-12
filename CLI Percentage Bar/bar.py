import os
from time import sleep
value=102
for i in range(value+1):
 print('\r', end="")
 width=os.get_terminal_size()[0]
 for x in range(width-5):
  if x==0 or x==width-6: print("|",end="")
  elif x>width//2-1 and x<width//2+1:
   if int(i/value*100)<10: print(" ",end="")
   print(" ", int(i/value*100),"% ",sep="",end="")
  else:
   if x<i/value*(width-3): print("#",end="")
   else: print(" ",end="")  
  print(end="", flush=True)
 sleep(0.01)
print("\nDone")