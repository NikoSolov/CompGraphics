from math import sin, cos
from PIL import Image


class VecImage:
 def __init__(self, name,width, height, bgcolor):
  self.name = name
  self.width = width
  self.height = height
  self.bgcolor = bgcolor
  self.file = open(name+'.svg', "w")
  self.file.write(f"""<svg xmlns="http://www.w3.org/2000/svg" 
              width="{self.width}" height="{self.height}"  
              style="background:{self.bgcolor}">\n""")
  self.inits = []
  self.objects = []
 def save(self):
  # init
  self.file.write("<defs>\n")
  for i in self.inits:
   self.file.write(i.result())
  self.file.write("</defs>\n")
  # draw
  for obj in self.objects:
   self.file.write(obj.result())
  # close
  self.file.write('</svg>\n')
  self.file.close()
 
class Marker:
 def __init__(self, id, refX, refY, width, height, obj, svg=None):
  self.id = id
  self.refX = refX
  self.refY = refY
  self.width = width
  self.height = height
  self.obj = obj
  if svg!=None:
   svg.inits.append(self)
 def result(self):
  return f"""
     <marker id="{self.id}" 
     markerWidth="{self.width}" markerHeight="{self.height}" 
     refX="{self.refX}" refY="{self.refY}" 
     orient="auto">\n
     {self.obj.result()}\n
     </marker>\n
  """

class Sqr:
 def __init__(self,x,y,width,height, svg=None,color="black", scolor="white", swidth=1, dash=(0,0)):
  self.x = x
  self.y = y
  self.width = width
  self.height = height
  self.color = color
  self.scolor = scolor
  self.swidth = swidth
  self.dash = dash
  if svg!=None:
   svg.objects.append(self)
 def result(self):
  return f"""<rect 
    width="{self.width}" height="{self.height}" 
    x="{self.x}" y="{self.y}" 
    fill="{self.color}"
    stroke-linecap="round"
    stroke="{self.scolor}" stroke-width="{self.swidth}"
    stroke-dasharray="{self.dash[0]},{self.dash[1]}" 
    />\n"""

class Line:
 def __init__(self,  x1, y1, x2, y2, svg=None,scolor="black", swidth=1, dash=(0,0), arr=("", "")):
  self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
  self.coords = [(x1,y1),(x2,y2)]
  self.length = ((self.x1-self.x2)**2+(self.y1-self.y2)**2)**(1/2)
  self.X = abs(self.x1-self.x2)
  self.Y = abs(self.y1-self.y2)
  self.scolor = scolor
  self.swidth = swidth
  self.dash = dash
  self.arr = arr
  if svg!=None:
   svg.objects.append(self)

 def result(self):
  return f"""<line 
    x1="{self.x1}" y1="{self.y1}" 
    x2="{self.x2}" y2="{self.y2}" 
    stroke="{self.scolor}" 
    stroke-dasharray="{self.dash[0]},{self.dash[1]}"
    stroke-width="{self.swidth}"
    stroke-linecap="round"
    marker-start="url(#{self.arr[0]})"
    marker-end="url(#{self.arr[1]})"
    />\n""" 
  

class Circle:
 def __init__(self, x,y,r,  svg=None,color="white", scolor="black", swidth=1, dash=(0,0)):
  self.x = x
  self.y = y
  self.r = r

  self.color = color
  self.scolor = scolor
  self.swidth = swidth
  self.dash = dash
  if svg!=None:
   svg.objects.append(self)
 def result(self):
  return f"""
    <circle
    cx="{self.x}" cy="{self.y}"
    r="{self.r}"
    fill="{self.color}"
    stroke-linecap="round"
    stroke="{self.scolor}" stroke-width="{self.swidth}"
    stroke-dasharray="{self.dash[0]},{self.dash[1]}" 
    />\n"""

class Polygon:
 def __init__(self,coords,  svg=None, color="white", scolor="black", swidth=1, dash=(0,0), style=""):
  self.coords = coords
  self.color = color
  self.scolor = scolor
  self.swidth = swidth
  self.dash = dash
  self.style=style
  if svg!=None:
   svg.objects.append(self)

 def result(self):
  st=""
  for i in self.coords:
   st+=f"{i[0]},{i[1]} "

  return f"""
    <polygon 
    points="{st}"
    fill="{self.color}"
    stroke-linecap="round"
    stroke="{self.scolor}" stroke-width="{self.swidth}"
    stroke-dasharray="{self.dash[0]},{self.dash[1]}"
    style="{self.style}" 
    />\n"""

class PLine():
 def __init__(self, coords, svg=None, color="None", scolor="black", swidth=1, dash=(0,0), marker=("None", "None","None")):
  self.coords = coords
  self.color = color
  self.scolor = scolor
  self.swidth = swidth
  self.dash = dash
  self.marker = marker
  if svg!=None:
   svg.objects.append(self)

 def result(self):
   st=""
   for i in self.coords:
    st+=f"{i[0]},{i[1]} "
   return f"""
    <polyline 
    points="{st}"
    fill="{self.color}"
    stroke-linecap="round"
    stroke="{self.scolor}" stroke-width="{self.swidth}"
    stroke-dasharray="{self.dash[0]},{self.dash[1]}"
    marker-start="url(#{self.marker[0]})"
    marker-mid="url(#{self.marker[1]})"
    marker-end="url(#{self.marker[2]})" 
    />\n"""
 
class RastImage():
 def __init__(self, path="",svg=None):
  im = Image.open(path)
  self.width = im.size[0]
  self.height = im.size[1]
  if svg!=None:
   svg.objects.append(self)
 def result(self):
  return f'''
  <image 
  href="{self.path}" 
  width="{self.width}" height="{self.height}" 
  />\n'''