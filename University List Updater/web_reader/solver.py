from os import listdir


direc="MIREA"


files = listdir(direc)
files.reverse()
print(files)
MIREA=[]

for i in files:
 f=open(direc+"/"+i, encoding='utf-8')
 a=[]
 a.append(f.readline())
 N,M=list(map(int,f.readline().split()))
 #print(N,M)
 a.append(N)
# break
 for line in f:
  b=int(line.split()[1])
  a.append(b)
 MIREA.append(a)

for i in range(len(MIREA)):
 print("-------------")
 print(MIREA[i][0],"pos", MIREA[i].index(17487324404), "in",MIREA[i][1])
 print(MIREA[i])
 a=MIREA[i].index(17487324404)
 n=a
 for j in range(a,1,-1):
  for q in MIREA:
  # print("~",q[0])
   if (MIREA[i]!=q) and (MIREA[i][j] in q) and q.index(MIREA[i][j])-1<q[1]:
  #  print("found", MIREA[i][j],"in",q[0], "pos:",q.index(MIREA[i][j])-1, 'in',q[1])
  #  print("temp_res",n)
    n-=1
 print("abs:", a, "solved:", n, "in",  MIREA[i][1])
 #break
 
