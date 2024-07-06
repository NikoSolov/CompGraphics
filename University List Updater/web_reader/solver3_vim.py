from os import listdir
#"Baumanka/TXT/",

#direcs=["MISIS/", "MIREA/", "MEI/"]

direcs=["MIREA/"]

al=[]
for path in direcs:
 sorted_files=listdir(path)[::-1]
# print("~~~~~~~~~~",path)
 for file in sorted_files:
#  print(file)
  f=open(path+file, encoding="cp1256")
  print(path+file)
  name=f.readline()
  N=int(f.readline())
  main={"code":file+" "+path, "place":N, "score":file[:3]}
  buf=[]
#  print(name)
#  print("Кол-во мест:",N)
  for line in f:
   q=line.split()
   q[1]=int(q[1])
   if len(q)>2: q[2]=int(q[2]); buf.append({"id":q[0], "score":q[1],"agree":q[2]})
   else: buf.append({"id":q[0], "score":0,"agree":q[1]})

#  print("Кол-во заявлений:",len(buf))
  main.update({"people" : buf})
  al.append(main)

def find_me(arr,snils):
 i=1
 for man in arr:
  if man["id"]==snils:
   return i
  i+=1
 return -1

param=0

for der in al:
 break
 N=find_me(der["people"], "17487324404")
 if N!=-1:
  print(der["code"])
  print("Your place now:",N, "/", len(der["people"]), "for", der["place"], "Score:",der["score"])
  pos=N
  for i in der["people"][:N]:
   man=i
  # print(man["id"], man["score"])
   for direc in al:
    if (find_me(direc["people"],man["id"])!=-1 and
        find_me(direc["people"],man["id"])<direc["place"]-param and
        direc["code"]!=der["code"]):
  #   if direc["code"].split()[-1]=="MISIS/":
   #  print("Founded in", direc["code"])
     pos-=1
     break
  print("Potential place:", pos)
print("=====================================")

 #18202748355
for der in al:
 N=find_me(der["people"], "17487324404")
 if N!=-1:
  print(der["code"])
  score=der["people"][N]["score"]
  pos=1
  count=0
  for man in der["people"]:
   if man["agree"]==1:
    count+=1
  

  for man in der["people"][:N-1][::-1]:
   if man["agree"]==1:
    #print(man["id"], pos) 
    pos+=1
#   else:
     #break
  print("Potential agree place:",pos,"from", count, "for", der["place"])
  print("-"*40)

input()


 


  
  







#def delete(snils):
# for der in al:
#  i=0
#  while i<len(der["people"]):
#   if der["people"][i]["id"]==snils:
#    del der["people"][i]
#   i+=1


#print("====== delete all agreed ======")
#for der in al: # перебор направлений
# print(der["code"], der["place"], len(der["people"]))
# for man in der["people"]: # перебор людей
#  if man["agree"]==1:
#   der["place"]-=1
#   print(man["id"], "founded")
#   snils=man["id"]
#   delete(snils)
# print(der["place"], len(der["people"]))
