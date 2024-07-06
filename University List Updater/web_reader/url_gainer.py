from bs4 import BeautifulSoup as bs

page=bs(open("MIREA_urls.html", encoding="utf-8"), "html.parser")
table=page.body.find("div", class_="rates").table.find_all("tbody")

f=open("MIREA_urls.txt","w")
for i in table:
 try:
  acc=i.find("tr", class_="rowCommon").find("td", class_="competitionListing").a
  print(acc["href"])
  f.write(acc["href"]+"\n")
 except:
  pass
f.close()
