import PyPDF2
import wget 
from os import listdir
direc="Baumanka/"
# 2
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
off="5. Поступающие на места в рамках КЦП по общему конкурсу ( "
for i in urls:
 break
 file=wget.download(i[0], out=direc+"PDF")
 print(file)

list_files=listdir(direc+"PDF")
print(list_files)
for i in range(len(list_files)):
 dec_txt=""
 #break
 score=""
 pdffileobj=open(direc+"PDF/"+list_files[i],'rb') 
 pdfreader=PyPDF2.PdfFileReader(pdffileobj)

 x=pdfreader.numPages
 print(list_files[i],x)
 dec_txt+=list_files[i][:-4]+"\n"
 text=[]
 for j in range(urls[i][1], x):
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
   a[1]=a[1].replace("-","").replace("Да","")
   dec_txt+=(a[1]+" "+a[4]+" "+a[-1]+"\n")
   if pos==N:
    score=str(a[4])
   pos+=1
#  print("~",line)
 
 file1=open(direc+"TXT/"+score+"_"+list_files[i][:-4]+".txt","w")
 file1.writelines(dec_txt)
 file1.close()
 print("Done")
