# pos = "C0" - 0
# C C# D D# E F F# G G# A A# B
# 0 1  2 3  4 5 6  7 8  9 10 11

a=[12*4+4, 12*3+11, 12*3+7, 12*3+2, 12*2+9, 12*2+4]
guitar=[]
chords=[[0,4,7], [0,3,7], [-7,4,0]]

for i in a:
 c=[]
 for j in range(5):
  c.append(i+j)
 guitar.append(c)

for i in guitar:
 print(*i)

pos= 9+12*3
c=[]
for i in chords[2]:
 c.append(pos+i)

print(c)

for string in guitar:
 for note in string:
  if note in c:
   print("#", end="")
  else: print("-",end="")
 print() 
