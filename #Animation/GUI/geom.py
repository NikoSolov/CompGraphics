import pygame as pg
from math import sin, cos
from random import randint as rd
from random import random
pg.init()
width, height=1024,768
root=pg.display.set_mode((width, height))
clock=pg.time.Clock()
game=True

fade=pg.Surface((width,height), pg.SRCALPHA)
fade.fill((0,0,0))
fade.set_alpha(1)
i=0
x_off=width//2
y_off=height//2
x_amp=100
while game:
 for event in pg.event.get():
  if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE):
   game=False
 #root.fill((0,0,0))
 #root.blit(fade, (0,0))

 i+=0.01
 x=x_off+sin(i*50)*sin(i*2)*100
 y=y_off+sin(i/2)*300
 pg.draw.circle(root, (0,255,0), (x,y), radius=3)
 x_amp+=1

 x,y=rd(height//3,width//3*2), rd(height//3,height//3*2)
 a,b=rd(1,width//4), rd(1,height//4)
 d=random()
 pg.draw.polygon(root, (rd(0,255), rd(0,255), rd(0,255)), [(x,y),(x+a,y+b), (x-b*d, y+a*d)])


 pg.display.update()
# clock.tick(60)
pg.quit()

