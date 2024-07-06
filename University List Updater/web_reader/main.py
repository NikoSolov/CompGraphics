from urllib.request import urlopen

#https://pk.mpei.ru/inform/list581bacc.html
#https://pk.mpei.ru/inform/list14bacc.html
urls=['https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416774837808438',
   'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417591424757046',
   'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417222681472310',
   'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416831985200438',
   'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417235799158070',
   'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1714956156281072950']


for q in urls:
 page = urlopen(q)
 for i in page:
  n=i.decode("utf-8")
  if "<body>" in n:
   page.readline()
   n=page.readline().decode("utf-8")
   print(n[2:-6])
  if "Всего мест" in n:
   a=n[n.rfind("Всего мест"):-len("</p></strong></div>")-1]
   a=a.replace("</p><p><strong>", "\t")
   a=a.split("\t")
   print(a[0])
   # Снилс сюда
  if "174-873-244-04" in n:
   a="<tr id='1737240656254867095'><td class='num'>"
   print("Номер в списке:",n[len(a)+2:len(a)+5])
 print()

#input("Press any key to quit...")
