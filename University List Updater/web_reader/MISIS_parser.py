# MISIS
from bs4 import BeautifulSoup as bs
import requests
urls=[
  #ИБО
 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-450302',
  #ИНМиН
 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-030302',
 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-110304',
 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-220301',
 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-280300',
  #ИТКН
 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-010304',
 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-090300',
  #ЭкоТех
 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-150302',
 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-220302',
  #МГИ
 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-130302',
 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=SPEC-BUDJ-O-210500',
  #ЭУПП
 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-380300']


direc="MISIS/"
for url in urls:
 
 page=bs(requests.get(url).text, "html.parser")

 direction=page.find("direction").text
 place=page.find("contest").text
 date=page.find("date").text
 print(date, direction, place, sep=" | ")
 al=direction+'\n'+place+'\n'
 table=page.find("tbody")
 pos=1
 score=0
 for i in table.find_all("tr"):
  buf=[]
  for n in i.find_all("td"):
   buf.append(n.text)

  if buf[-3]=="ОКМ;" and buf[2]!='':
   al+=buf[2].replace(" ", "").replace("-", "")+' '+buf[4]+' '
   if buf[-5]=='+' and buf[-4]=='+':
    al+='1\n'
   else:
    al+='0\n'
   if pos==int(place):
    score=buf[4]
   pos+=1
  # print(pos, buf[4])
 f=open(direc+str(score)+"_"+direction+".txt","w")
 f.write(al)
 f.close()
 print("---")
