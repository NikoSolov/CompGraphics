carMap={
  "A": ["H", 2,(0,0)],
  "O": ["V", 3,(5,0)],
  "P": ["V", 3,(0,1)],
  "B": ["V", 2,(0,4)],
  "X": ["H", 2,(1,2)],
  "Q": ["V", 3,(3,1)],
  "C": ["H", 2,(4,4)],
  "R": ["H", 3,(2,5)]
}

def interface(command):
 if command == "print":
  printMap = ""
  for y in range(6):
   for x in range(6):
    flag = False
    for name in carMap.keys():
     if flag == True : break

     for step in range(carMap[name][1]):
      if (x == carMap[name][2][0]+step*(carMap[name][0]=="H")
          and y == carMap[name][2][1]+step*(carMap[name][0]=="V")):
       printMap += name
       flag = True
       break
    if flag == False : printMap += "+"
   printMap += "\n"
  return printMap
  

def move(command):
 if (command[0] not in carMap.keys()):
  return "There is not car name like this"
 if (((command[1] == "L" or command[1] == "R") and carMap[command[0]] == "V") or
      (command[1] == "U" or command[1] == "P") and carMap[command[0]] == "H"):
  return "Car can't move that direction"
 flag=False
 car = carMap[command[0]]
 if (command[1] == "R" or command[1] == "D"): dstep=1
 if (command[1] == "L" or command[1] == "U"): dstep=-1


 for pos in range(car[1]):
  if ((car[2][0]+(dstep*command[2]+step)*(carMap[name][0]=="H") > 5) or
     (car[2][0]+(dstep*command[2]+step)*(carMap[name][0]=="H") < 0) or
     (car[2][1]+(dstep*command[2]+step)*(carMap[name][0]=="V") < 5) or
     (car[2][1]+(dstep*command[2]+step)*(carMap[name][0]=="V") < 5)):

   return "Cant go there"
print(carMap.keys())
 
while (True):
    print (interface(input("insert command: ")))