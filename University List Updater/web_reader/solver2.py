from os import listdir

direc="MIREA"
files = listdir(direc)

def find(snils):
 for i in range(len(people)):
  if people[i]["SNILS"]==snils:
   return i 
   
people=[]
list_people=[]
for i in files:
 f=open(direc+"/"+i)
 N=f.readline()
 f.readline()
 for i in f:
  r=i.split()
  if r[1] not in list_people:
   a={"SNILS": r[1], "Score": r[4],
      "VUS":{"MIREA":{"Code":N[:8],"Agreed": r[2], "Origin": r[3]}]}}
   people.append(a)
   list_people.append(r[1])
  else:
   people[find(r[1])]["VUS"]["MIREA"].append({"Code":N[:8],"Agreed": r[2], "Origin": r[3]})

direc="MEI"
files = listdir(direc)


print(people[0])
print(len(people)) 

for i in people:
 if i["SNILS"]=="17487324404":
  print(i["Score"])
  break

#print(people)
