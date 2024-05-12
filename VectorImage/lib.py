import pygame as pg
class Window:
 width = 1280
 height = 1024
 size = (width, height)
class Surf:
 width = 100
 height = 100

Surf = pg.Surface((Surf.width, Surf.height))
# color values
w = (255,255,255)
# for dot object doesn't need class. It is just tuple.

class BLine():
 def __init__(self, *pos):
  if pos[-1] == pos[0]:
   print("closed")
   self.state = "closed"
   self.pos = pos[:-1]
  else:
   print("opened")
   self.state = "opened"
   self.pos = pos
 def draw (self, root):
  for i in range(len(self.pos)-1):
   pg.draw.line(root, w, self.pos[i], self.pos[i+1])
  if self.state == "closed":
   pg.draw.line(root, w, self.pos[0], self.pos[-1])


A=(10,10)
B=(20,20)
C=(30,30)

r = BLine(A,B,C)
t = BLine(C,A,B,C)
