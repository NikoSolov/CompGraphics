from random import choice
# [0, [1,2,3,4,5,6,7,8,9] 2x, [st,ch,+2] 2x] 4x (colors), [+4, pick] 4x

for i in range(256):
 print(f'\033[48;5;{i}m {i}')

coloda=[]
def printout(st):
 colors={"R": 91, "G": 92, "Y":93, "B":94}
 print(f'\033[{colors[st[-1]]}m'+st[:-1]+'\033[37m')

for c in "RYGB":
 coloda.append("0"+c)
 for j in range(2):
  for i in range(1,10):
   coloda.append(str(i)+c)
  for i in ["stop", "rev","+2"]:
   coloda.append(i+c)

print(coloda)

for i in range(7):
 printout(choice(coloda))
 
