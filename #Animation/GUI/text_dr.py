import pygame as pg
pg.init()
root=pg.display.set_mode((1024,768))
surf=pg.Surface((1024,768),pg.SRCALPHA)

game=True
clock=pg.time.Clock()

def print_sym(a,x,y):
 draw=False
 coord=(0,0)
 for i in a:
  if i==0: draw=False
  elif i==1: draw=True
  else: 
   if draw==True:
    pg.draw.aaline(root, (0,255,0,10),
                 (x+coord[0]*font_width, y+coord[1]*font_height),
                 (x+i[0]*font_width, y+i[1]*font_height),0)
   coord=i


font_width=100
font_height=100

sym=[[0,(0,1),1,(.5,0),(1,1),0,(0.25,0.5),1,(0.75,.5)], # A
     [0,(1,0),1,(0,0),(0,1),(1,1),(1,0.5),(0,0.5)]]

while game:
 for event in pg.event.get():
  if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE):
   game=False
 root.fill((0,0,0))
# surf.fill((0,0,0,255))
# font_height+=1
 print_sym(sym[1],5,5)
 print_sym(sym[0],10,10)

# root.blit(surf, (0,0))
 pg.display.update()
 clock.tick(60)
pg.quit()
