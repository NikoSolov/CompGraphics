from urllib.request import urlopen
import re

def formatter(s,f):
 arr=[]
# f=f.split("|")
 for i in range(len(f)-1):
  a=s.find(f[i])
  b=s[a+len(f[i]):].find(f[i+1])+a+len(f[i])
  x=s[a+len(f[i]):b]
  arr.append(x)
  s=s[a+len(f[i])+len(x):]
# print(arr)
 return arr
 
#formatter(s,f)



# ----- mirea ------
f=open("MIREA_urls.txt", "r")
MIREA=["https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416831985200438"]
#for i in f:
# MIREA.append(i)
#f.close()
print("MIREA array created")
head=["<p class='namesListPlan'><strong>Условия поступления:</strong><br>","<br></p><div style='text-align: center'><p>Всего мест — ","</p><p><strong>Текущий проходной балл по общему конкурсу — ","</p></strong></div>"]
form=["<tr id='","'><td class='num'>","</td><td class='fio'>","</td><td class='accepted'>","</td><td class='original'>","</td><td class='campus'>","</td><td class='marks'>","</td><td class='sum'>","</td><td class='achievments'>","</td>"]

direc="MIREA/"

for url in MIREA:
 #print("on break"); break
 N=0
 name=""
 page=urlopen(url)
 buf=""
 flag=True
 for line in page:
  dec_line=line.decode("utf-8")
  if "<p class='namesListPlan'>" in dec_line:
   print("File created")
   a=formatter(dec_line, head)
   print(a[0])
   a[0]=a[0].split(" / ")[0]
   print("----------")
   name=a[0]
   try:
    N=int(a[1])
   except:
    offset="Всего мест — "
#    print(dec_line)
    posi=dec_line.find(offset)+len(offset)
    N=int(dec_line[posi:posi+dec_line[posi:].find("<")])
    print(N)
   if N==0:
    flag=False
    break
#   f.write(a[0]+"\n"+a[1]+"\n")
   buf+=name+"\n"+str(N)+"\n"
  if "</thead>" in dec_line:
   break

 i=1
 for line in page:
  if flag==False:
   break
  dec_line=line.decode("utf-8")
  if "</table>" in dec_line: break
  a=formatter(dec_line, form)
  page.readline()
  a[2]=a[2].replace("-","").replace(" ","")
  
  a[3]=a[3].replace("</td>","")

  if a[3]=="да" and a[4]=="да": a[3]="1"
  else: a[3]="0"
  if a[3]=="1":
   i+=1
#  f.write( a[2]+" "+str(int(a[-1])+int(a[-2]))+" "+a[3]+"\n")
  buf+=( a[2]+" "+str(int(a[-1])+int(a[-2]))+" "+a[3]+"\n")
  if i==N: name=str(int(a[-1])+int(a[-2]))+"_"+name; i+=1
  
 if flag!=False:
  f=open(direc+name+".txt", "w")  
  f.write(buf)
  f.close()

# --- MEI ---
MEI=["https://pk.mpei.ru/inform/list581bacc.html",
     "https://pk.mpei.ru/inform/list14bacc.html"]

#</style><div class="competitive-group">Прикладная математика и информатика МПОВМКС бюджет (Очная) </div><div class="title1">Конкурсные списки на зачислениe 9 августа 2022г. (бакалавриат и специалитет) <br>(данные о поданных согласиях на зачисление на 19:18 13.07.2022)<br>Количество вакантных мест: 60<br><br><a href="#terms" style="font-size:14px; font-weight:bold; color:red; text-decoration:none; border-bottom: 1px dashed red;">Обозначения и пояснения приведены в конце страницы »»</a><br><br><a href="/inform/list.html">&laquo;&laquo;Вернуться к списку конкурсных групп</a><br><br>
#Прикладная математика и информатика МПОВМКС бюджет (Очная) 60
#'</style><div class="competitive-group">', '</div><div class="title1">','<br>(данные о поданных согласиях на зачисление на ',')<br>Количество вакантных мест: 60<br><br><a href="#terms" style="font-size:14px; font-weight:bold; color:red; text-decoration:none; border-bottom: 1px dashed red;">Обозначения и пояснения приведены в конце страницы »»</a><br><br><a href="/inform/list.html">&laquo;&laquo;Вернуться к списку конкурсных групп</a><br><br>

head=['</style><div class="competitive-group">','</div><div class="title1">Конкурсные списки на зачислениe 9 августа 2022г. (бакалавриат и специалитет) <br>(данные о поданных согласиях на зачисление на',')<br>Количество вакантных мест: ','<br><br><a href="#terms" style="font-size:14px; font-weight:bold; color:red; text-decoration:none; border-bottom: 1px dashed red;">Обозначения и пояснения приведены в конце страницы »»</a><br><br><a href="/inform/list.html">&laquo;&laquo;Вернуться к списку конкурсных групп</a><br><br>']
#head=["<p class='namesListPlan'><strong>Условия поступления:</strong><br>","<br></p><div style='text-align: center'><p>Всего мест — ","</p><p><strong>Текущий проходной балл по общему конкурсу — ","</p></strong></div>"]
st='<tr class="accepted" id="p99783"><td>294</td><td>286</td><td>88</td><td>&nbsp;</td><td>98</td><td>&nbsp;</td><td>100</td><td>8</td><td id="s18448647821">СНИЛС: 18448647821</td><td>б/о</td><td>не подано</td><td></td></tr>'
#294 286 88 98 100 18448647821 б/о не подано
#form=['<tr class="','" id="','"><td>','</td><td>','</td><td>','</td><td>','</td><td>','</td><td>',';</td><td>','</td><td>','</td><td id="','">СНИЛС: ','</td><td>','</td><td>','</td><td></td></tr>']
#form=["<tr id='","'><td class='num'>","</td><td class='fio'>","</td><td class='accepted'>","</td><td class='original'>","</td><td class='campus'>","</td><td class='marks'>","</td><td class='sum'>","</td><td class='achievments'>","</td>"]
form=['<tr class="','" id="','"><td>','</td><td>','</td><td>','</td><td>','</td><td>','</td><td>','</td><td>','</td><td>','</td><td id="','">СНИЛС: ','</td><td>','</td><td>','</td><td>','</td></tr>']
off='				<td class="parName" width="30%" rowspan=2>СНИЛС или Рег.номер</td><td class="parName" width="3%" rowspan=2>Общ.</td><td class="parName" width="5%" rowspan=2>Согласие</td><td class="parName" width="10%" rowspan=2>Примечание</td></tr><tr style="background-color:#F0F0FF"><td class="parName">Мат.</td><td class="parName">Инж.мат.</td><td class="parName">Инф.</td><td class="parName">ИТ Проф.</td><td class="parName">Рус.</td></tr>'
off2='				<td class="parName" width="30%" rowspan=2>СНИЛС или Рег.номер</td><td class="parName" width="3%" rowspan=2>Общ.</td><td class="parName" width="5%" rowspan=2>Согласие</td><td class="parName" width="10%" rowspan=2>Примечание</td></tr><tr style="background-color:#F0F0FF"><td class="parName">Мат.</td><td class="parName">Инж.мат.</td><td class="parName">Инф.</td><td class="parName">Физ.</td><td class="parName">ИТ Проф.</td><td class="parName">Рус.</td></tr>'

N=0
direc="MEI/"
name=""
for url in MEI:
 break
 buf=""
# break; print("on break") 
 page=urlopen(url)
 for line in page:
  dec_line=line.decode("utf-8")
  if '</style><div class="competitive-group">' in dec_line:
   print("File created")
   a=formatter(dec_line, head)
   print(a[0])
   print("----------------")
   name=a[0]
   N=int(a[2])
   #print(N)
   #f.write(a[0]+"\n"+a[2]+"\n")
   buf+=(a[0]+"\n"+a[2]+"\n")
  if off in dec_line:
   dec_line=dec_line[len(off):].replace(' style="color:gray;"',"")
   break

  if off2 in dec_line:
   dec_line=dec_line[len(off2):].replace(' style="color:gray;"',"")
   break
# page.readline()
 i=1
 a=formatter(dec_line.replace(' style="color:gray;"',""), form)
 dec={"не подано":'0', "подано":'1'}
 try:
#  f.write(a[11].replace('">Рег.номер: ',"")+" "+a[2]+" "+dec[a[13]]+"\n")
  buf+=(a[11].replace('">Рег.номер: ',"")+" "+a[2]+" "+dec[a[13]]+"\n")
 except:
  print(a)
 i+=1
 for line in page:
  dec_line=line.decode("utf-8")
  if "</table>" in dec_line: break
  a=formatter(dec_line.replace(' style="color:gray;"',""), form)
  
  if i==N: name=a[2]+"_"+name

  i+=1
  try:
   buf+=(a[11].replace('">Рег.номер: ',"")+" "+a[2]+" "+dec[a[13]]+"\n")
  except:
   print(a)
 f=open(direc+name+".txt", "w")
 print(direc+name)
 f.write(buf)
 f.close()

quit()
import PyPDF2
import wget
from os import listdir, remove
direc="Baumanka/"

urls=[["https://priem.bmstu.ru/lists/upload/enrollees/first/moscow-1/01.03.02.pdf",3],
      ["https://priem.bmstu.ru/lists/upload/enrollees/first/moscow-1/01.03.03.pdf",1],
      ["https://priem.bmstu.ru/lists/upload/enrollees/first/moscow-1/01.03.04.pdf",1],
      ["https://priem.bmstu.ru/lists/upload/enrollees/first/moscow-1/02.03.01.pdf",1],
      ["https://priem.bmstu.ru/lists/upload/enrollees/first/moscow-1/09.03.01.pdf",5],
      ["https://priem.bmstu.ru/lists/upload/enrollees/first/moscow-1/09.03.02.pdf",2],
      ["https://priem.bmstu.ru/lists/upload/enrollees/first/moscow-1/09.03.03.pdf",3],
      ["https://priem.bmstu.ru/lists/upload/enrollees/first/moscow-1/09.03.04.pdf",4],
      ["https://priem.bmstu.ru/lists/upload/enrollees/first/moscow-1/10.05.01.pdf",1],
      ["https://priem.bmstu.ru/lists/upload/enrollees/first/moscow-1/10.05.03.pdf",1],
      ["https://priem.bmstu.ru/lists/upload/enrollees/first/moscow-1/10.05.05.pdf",1]]
off="2. Поступающие на места в рамках КЦП по общему конкурсу ( "

list_files=listdir(direc+"PDF")
for i in list_files:
 remove(direc+"PDF/"+i)
#print("Files removed")
for i in urls:
 break
 file=wget.download(i[0], out=direc+"PDF")
 print(file)
#print("Files downloaded")

list_files=listdir(direc+"PDF")
for i in range(len(list_files)):
 dec_txt=""
 break
 score=""
 pdffileobj=open(direc+"PDF/"+list_files[i],'rb') 
 pdfreader=PyPDF2.PdfFileReader(pdffileobj)

 x=pdfreader.numPages
 print(list_files[i],x)
 dec_txt+=list_files[i][:-4]+"\n"
 text=[] #urls[i][1]
 for j in range(1, x):
  pageobj=pdfreader.getPage(j)
  text+=pageobj.extractText().split('\n')
 print("text has been extracted")
 flag=False
 flag2=False
 pos=1
 for line in text:
  if off in line:
   N=int(line[len(off):].split()[0])
#   print(a)
   #5. Поступающие на места в рамках КЦП по общему конкурсу ( 20 мест, оставшихся от контрольных цифр
   dec_txt+=str(N)+"\n"
   flag=True
  a=line.replace("(?)","").replace("*","").split()
  
  try:
   a[0]=int(a[0])
   flag2=True
  except:
   flag2=False
#   pass
  
  if flag==True and flag2==True and len(a)>2:
  # print(a)
   if len(a)>12:
    a.pop()
    
   if a[-1]=="Да" and a[-2]=="Да": a[-1]='1'
   else: a[-1]="0"
   a[1]+=a[2]
   a[1]=a[1].replace("-","").replace("Да","").replace("Нет","")
   dec_txt+=(a[1]+" "+a[4]+" "+a[-1]+"\n")
   if pos==N:
    score=str(a[4])
   pos+=1
#  print("~",line)
 
 file1=open(direc+"TXT/"+score+"_"+list_files[i][:-4]+".txt","w")
 file1.writelines(dec_txt)
 file1.close()
 print("Done")



