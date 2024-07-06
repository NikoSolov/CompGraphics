
s='<tr class="accepted" id="p99783"><td>294</td><td>286</td><td>88</td><td>&nbsp;</td><td>98</td><td>&nbsp;</td><td>100</td><td>8</td><td id="s18448647821">СНИЛС: 18448647821</td><td>б/о</td><td>не подано</td><td></td></tr>'
f='<tr class="accepted" id="|"><td>|</td><td>|</td><td>|</td><td>&nbsp;</td><td>|</td><td>&nbsp;</td><td>|</td><td>|</td><td id="|">СНИЛС: |</td><td>|</td><td>|</td><td></td></tr>'
#<td>294</td><td>286</td><td>88</td><td>&nbsp;</td><td>98</td><td>&nbsp;</td><td>100</td><td>8</td><td id="s18448647821">СНИЛС: 18448647821</td><td>б/о</td><td>не подано</td><td></td></tr>'


def formatter(s,f):
 arr=[]
 f=f.split("|")
 for i in range(len(f)-1):
  a=s.find(f[i])
  b=s[a+len(f[i]):].find(f[i+1])+a+len(f[i])
  x=s[a+len(f[i]):b]
  arr.append(x)
  s=s[a+len(f[i])+len(x):]
 print(arr)
 return arr
 
formatter(s,f)
