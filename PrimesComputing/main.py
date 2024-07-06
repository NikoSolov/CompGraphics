n=2

while n<1000000:
 flag=True
 for i in range(2,n):
  if n%i==0: flag=False; break
 if flag: print(n)
 n+=1
  
