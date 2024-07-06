import pygame as pg
pg.init()
width, height=1024,768
root=pg.display.set_mode((width,height))
clock=pg.time.Clock()
game=True
class obj():
 x=500
 y=500

class vec():
 arr=[]
 def __init__(self, dx,dy):
  self.dx=dx
  self.dy=dy
  vec.arr.append(self)

vec(300,0)
vec(0,100)
while game:
 for event in pg.event.get():
  if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE):
   game=False
 root.fill((0,0,0))
 pg.draw.circle(root, (255,255,255), (obj.x, obj.y), 10)
 for i in vec.arr:
  pg.draw.line(root, (255,0,0), (obj.x, obj.y), (obj.x+i.dx, obj.y+i.dy))
 for i in vec.arr:
  obj.x+=i.dx/100
  obj.y+=i.dy/100
 vec.arr[1].dy-=10

 pg.display.update()
 clock.tick(60)
pg.quit()





 