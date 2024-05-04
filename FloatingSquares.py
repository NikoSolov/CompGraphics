import pygame
from random import randint, choice, uniform
pygame.init()
width, height=512,512
game=True
clock=pygame.time.Clock()
class obj():
    list=[]
    def __init__(self, x,y, color, xstep, ystep):
        self.x=x
        self.y=y
        self.color=color
        obj.list.append(self)
        self.xstep=xstep
        self.ystep=ystep
    def coords():
        for i in obj.list:
            print(i.x, i.y)
    def lines(root):
        global width, height
        for i in obj.list:
            pygame.draw.rect(root, i.color,(i.x, i.y,10,10))
            i.x+=i.xstep
            i.y+=i.ystep
            if i.x<0 or i.x>width-10: i.xstep*=-1
            if i.y<0 or i.y>height-10: i.ystep*=-1
for i in range(200):
    color=(randint(0,255),randint(0,255),randint(0,255))
    obj(randint(0,width-10),randint(0,height-10),color,uniform(-2,2),uniform(-2,2))

surf=pygame.Surface((width, height), pygame.SRCALPHA)
surf.fill((0,0,0))
surf.set_alpha(10)

root=pygame.display.set_mode((width, height))
while game:
    for event in pygame.event.get():
        if (event.type==pygame.QUIT) or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE): game=False
    root.blit(surf, (0,0))
    obj.lines(root)
    pygame.display.update()
    clock.tick(60)
pygame.quit()