import pygame as pg
pg.init()
width=1280
height=760
frame=300
radius=(frame//4)

pol=[[[(frame//2, 0), (0, frame//2), (frame//2, frame), (frame, frame//2)],(255,0,0)],
     [[(0,0),(frame//2,0), (frame//2,frame//2), (0,frame//2)],(255,255,0)],
     [[(0,0),(frame, frame), (0,frame)], (255,184,92)],
     [[(0,0),(frame, frame), (0,frame)], (255,255,255)],
     [[(0,0), (frame,0),(frame//2, frame//2), (frame, frame), (0,frame)], (152,184,66)],
     [[(0,0), (frame,0),(frame//2, frame//2), (0,frame//2)], (0,0,66)],
     [[(0,0), (frame,0),(frame, frame//2), (0,frame//2)], (0,80,0)],
     [[(0,frame//2), (frame//2,frame//2),(frame, 0), (frame//2,0)], (0,80,0)]#,



    #  [[]],
    #  [[(0,0), (frame,0),(frame, frame//2), (0,frame//2)], (61,0,61)],
    #  [[(0,0), (frame,0),(frame, frame//2), (0,frame//2)], (61,0,61)],
    #  [[(0,0), (frame,0),(frame, frame//2), (0,frame//2)], (255,255,255)]
     ]


cards=[]

for i in pol:
    a=pg.Surface((frame, frame), pg.SRCALPHA)
    pg.draw.polygon(a, i[1], i[0])
    pg.draw.rect(a, (128,128,128), (0,0,frame,frame), width=1)
    cards.append(a)


pg.draw.circle(cards[-1], pol[-1][1],(frame//2,frame//2), frame//2)
pg.draw.circle(cards[-1], (0,0,0,0),(frame//2,frame//2), radius)
pg.draw.circle(cards[-2], pol[-2][1],(frame//2,frame//2), radius)
pg.draw.circle(cards[-3], (0,0,0,0),(frame//2,frame//2), radius)

a=pg.Surface((frame, frame), pg.SRCALPHA)
pg.draw.circle(a, (0,0,66),(frame//2,frame//2), frame//2)
pg.draw.rect(a, (0,0,0,0), (0,frame//2,frame,frame//2))
pg.draw.rect(a, (128,128,128), (0,0,frame,frame), width=1)
cards.append(a)


root=pg.display.set_mode((width,height))
clock=pg.time.Clock()
game=True
i=0
n=0
while game:
 for event in pg.event.get():
  if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE):
   game=False
 root.fill((i*4,i*4,i*4))

 i+=1
 if i>30: n+=1; i=0
 if n>len(cards)-1: n=0
#  print(i)  
 root.blit(cards[n], (0,0))
# root.blit(a, (0,0))

 pg.display.update()
 clock.tick(60)
