from random import randint as rd
from itertools import permutations as pd
a=int(input("insert count of digits in value "))
d=list(pd("123456789", a)) # generate object of variations
print(d)
d=d[rd(0,len(d)-1)] # get only one of all
print(d)
n=""
for i in d:
 n+=i

#n=str(rd(10**(a-1), (10**a)-1))
#print(n)
game=True
q=1
while game:
 if q>30: print("Right answer:",n); break
 print("Attempt",q)
 m=str(input("insert value to check: "))
 if len(m)==a:
  x,y=0,0
  for i in range(a):
   if m[i] in n:
    if m[i]!=n[i]:
     x+=1
    else:
     y+=1
  if x==0 and y==a:
   print("YOU WIN")
   game=False
  else:
   print("digits in wrong pos:",x,"\ndigits in right pos:", y,"\n")
  q+=1
 else:
  print("Please insert the value with right count of digits!!!\n")
