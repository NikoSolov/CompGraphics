# MIREA
from bs4 import BeautifulSoup as bs
import requests

f=open("MIREA_urls.txt", "r")
MIREA=[]
for i in f:
 MIREA.append(i)
f.close()
print("MIREA array created")
#urls=["dochtml.html"]

#<p class="lastUpdate" style="text-align: center;">Список по состоянию на 25 июля 20:25</p>
direc="MIREA/"
for url in MIREA:
 page=bs(requests.get(url).text, "html.parser")
 
# page=bs(open(url, encoding='utf-8'), "html.parser")
 print("page loaded")
 date=page.find("p", class_="lastUpdate").text
 direction=page.body.h1.text.split('\n')[1].replace("\t","")
 place=page.body.find("div", class_="names").div.p.text.split()[-1]
 print(date, direction, place, sep=" | ")
 
 al=direction+'\n'+place+'\n'
 table=page.body.find("div", class_="names").find("table", class_="namesTable").contents

 #print("===========================")
# print(len(list(table)), type(table))
 #pos=1
 score=0
# print(table[3:10:2])
 #print("===========================")
 for i in table[3::2]:
  buf=[]
  if i!='\n':
   for j in i.contents:
  #  print(j.text)
    buf.append(j.text)
  # print(buf)
  # print('----------')

   if len(buf)>1:
    al+=buf[1].replace("-", "")+' '+buf[-2]+' '
    if buf[3]=='да' and buf[4]=='да':
     al+='1\n'
    else:
     al+='0\n'
#    print(buf[0], place)
    if int(buf[0])==int(place):
     score=buf[-2]
# break 
 f=open(direc+str(score)+"_"+direction+".txt","w")
 f.write(al)
 f.close()
 print("---")
