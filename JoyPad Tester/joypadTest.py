import pygame as pg

pg.init()
pg.joystick.init()
joys = [pg.joystick.Joystick(i) for i in range(pg.joystick.get_count())]
print(joys)
size = (1280,768)
root=pg.display.set_mode(size)
clock = pg.time.Clock()
game=True

class sqr():
 def __init__(self,x,y,size,color=(255,0,0)) -> None:
  self.x=x
  self.y=y
  self.size=size
  self.color=color
 def draw(self, root):
  pg.draw.rect(root, self.color, (self.x, self.y, self.size, self.size))

S=sqr(50,50,50)
dx=0
dy=0

def sgn(x):
 if x>0: return 1
 if x<0: return -1
 return 0

speed = 10
while game:

 for event in pg.event.get():
  if event.type==pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESC):
   game=False
  if event.type == pg.JOYBUTTONDOWN:
   print("~",event)
  if event.type == pg.JOYAXISMOTION:
   print("#",event)
   if event.axis==0:
    dx=event.value**2*sgn(event.value)*speed
   if event.axis==1:
    dy=event.value**2*sgn(event.value)*speed
  if event.type == pg.JOYHATMOTION:
   print("!",event)
 
 root.fill((0,0,0))
# joys[0].rumble(0,1,10)
 S.draw(root)
 S.x+=dx
 S.y+=dy


 pg.display.update()
 clock.tick(60)


pg.quit()