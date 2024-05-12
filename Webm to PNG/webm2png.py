from PIL import Image
from os import listdir
print(listdir())

for i in listdir()[3:]:
 if ".webp" in i:
  print(i)
  im = Image.open(i)
  im.save("new/"+i[:-5]+".png", "png")