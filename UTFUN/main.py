import codecs
fin=codecs.open("source.txt", "r","utf-8")
fout=codecs.open("result.txt", "w","utf-8")

sub=False
sup=False

a=fin.read()
#       0    1    2    3     4    5     6     7     8    9   
sups=[8304, 185, 178, 179, 8308, 8309, 8310, 8311, 8312, 8313]

for i in a:
 if i=='_':
  print("_ found")
  sub=True
 elif i=="^":
  print("^ found")
  sup=True

 elif i in "0123456789":
  print(i)
  if sub==True:
   fout.write(chr(8320+int(i)))
   print(chr(8320+int(i)))
   sub=False
  elif sup==True:
   fout.write(chr(sups[int(i)]))
   print(chr(sups[int(i)]))
   sup=False
   print("===================")
  else:
   fout.write(i)
 else:
  fout.write(i)


fin.close()
fout.close()
