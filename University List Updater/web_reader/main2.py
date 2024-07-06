from urllib.request import urlopen


urls=['https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416774837808438',
   'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417222681472310',
   'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416831985200438',
   'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417235799158070',
   'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1714956156281072950']

all_table=[]

for q in urls:
 tablet=[]
 page = urlopen(q)
 i=0
 for line in page:
  if i==21:
#   print(line.decode("utf-8"))
   break
  i+=1
 text=page.read().decode("utf-8")
#</thead> </table>
 table=text[text.rfind("</thead>")+len("</thead>"): text.find("</table>")]
 table=table.split("\n")

 for i in range(1,len(table),2):
#  print(table[i])
  #line="<tr id='1737065049733731991'><td class='num'>1</td><td class='fio'>163-063-896-67</td><td class='accepted'>нет</td><td class='original'>нет</td><td class='campus'>требуется</td><td class='marks'>100 98 96 </td><td class='sum'>294</td><td class='achievments'>10</td>"
  line=table[i]
  form=["<tr id='","'><td class='num'>","</td><td class='fio'>","</td><td class='accepted'>","</td><td class='original'>","</td><td class='campus'>","</td><td class='marks'>"," </td><td class='sum'>","</td><td class='achievments'>","</td>"]
  ids=list(map(line.rfind, form))
#  print(ids)
  acra=[]
  for z in range(1,len(form)-1):
   acc=line[ids[z]+len(form[z]):ids[z+1]]
   acc=acc.replace("</td>","")
   acra.append(acc)
#   print(acc, end="\t")
  tablet.append(acra)  
# print()
 all_table.append(tablet)

for i in all_table:
 for j in i:
  print(*j,sep="\t\t")
 print("\n---------")
print("Done")
