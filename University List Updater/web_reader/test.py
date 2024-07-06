line="<tr id='1737065049733731991'><td class='num'>1</td><td class='fio'>163-063-896-67</td><td class='accepted'>нет</td><td class='original'>нет</td><td class='campus'>требуется</td><td class='marks'>100 98 96 </td><td class='sum'>294</td><td class='achievments'>10</td>"

a=["<tr id='","'><td class='num'>","</td><td class='fio'>","</td><td class='accepted'>","</td><td class='original'>","</td><td class='campus'>","</td><td class='marks'>"," </td><td class='sum'>","</td><td class='achievments'>","</td>"]

b=list(map(line.rfind, a))
print(b)

for i in range(1,len(a)-1):
 print(line[b[i]+len(a[i]):b[i+1]])
#for i in range(len(a)-1):
 
