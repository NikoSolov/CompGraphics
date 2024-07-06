from random import randint, getrandbits
import pygame
from math import sin, cos, radians, pi
pygame.init()
game=True
width=1024
height=768
root=pygame.display.set_mode((width, height), pygame.HWSURFACE)#, pygame.FULLSCREEN )
#root=pygame.Surface((width,height))
clock=pygame.time.Clock()
n=pygame.Surface((10000,10000), pygame.HWSURFACE)

class Coords():
    inst=[]
#    mode=""
    def __init__(self, x,y, color, xstep, ystep):
        self.x=x
        self.y=y
        self.color=color
        self.xstep=xstep
        self.ystep=ystep
        self.xstate=0
        self.ystate=0
        self.get=False
        self.radius=1
        self.counter=0
        Coords.inst.append(self)
    def standby_mode(self,root):
        pass
        
    def lines(self, root):
        global width, height
        pygame.draw.rect(root, self.color,(self.x,self.y,5,5))
        if self.x<0 or self.x>width:self.xstep*=-1
        if self.y<0 or self.y>height:self.ystep*=-1
        self.x+=self.xstep
        self.y+=self.ystep
        
    def whirlpool(self, root):
        pygame.draw.rect(root, self.color,(self.x,self.y,5,5))
        self.x=self.x+(cos(radians(self.y)))*1+cos(3*radians(self.y))/0.5#+cos(5*radians(self.y))/5+cos(7*radians(self.y))/7
        self.y=self.y+(sin(radians(self.x)))*1+sin(3*radians(self.x))/0.5
        #+sin(5*radians(self.x))/5+sin(7*radians(self.x))/7
        
    def whirlpool2(self, root):
        pygame.draw.rect(root, self.color,(self.x,self.y,5,5))
        self.x=self.x+(cos(radians(self.y)))
        self.y=self.y+(sin(radians(self.x)))
    def draw(root, mode=0):
        if mode==0: [instance.lines(root) for instance in Coords.inst]
        elif mode==1: [instance.whirlpool(root) for instance in Coords.inst]
        elif mode==2: [instance.whirlpool2(root) for instance in Coords.inst]        
        
for i in range(1000):
    a=Coords(randint(0,width),randint(0,height), (randint(0,255),randint(0,255),randint(0,255),255), randint(1,4), randint(-4,-1))
#print("DONE!!!")

s = pygame.Surface((width,height), pygame.SRCALPHA)
s.set_alpha(5)               
s.fill((0,0,0))           

c=0
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: game=False
    root.blit(s, (0,0))
    key=pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]: game=False
    if key[pygame.K_z]:
        Coords(randint(0,width),randint(0,height), (randint(0,255),randint(0,255),randint(0,255),255), randint(1,4), randint(-4,-1))
        print(len(Coords.inst))
    if key[pygame.K_x]:
        if len(Coords.inst)>0:
            del Coords.inst[len(Coords.inst)-1]
        print(len(Coords.inst))
    if key[pygame.K_c]: Coords.inst=[]
    if key[pygame.K_v]:
        for i in range(1000):
            Coords(randint(0,width),randint(0,height), (randint(0,255),randint(0,255),randint(0,255),255), randint(1,4), randint(-4,-1))
#        while len(Coords.inst)>0:
#            del Coords.inst[0]

    Coords.draw(root,2)
    
#    for i in range(0,1000,90):
#        pygame.draw.line(root,(255,255,255),(i,0), (i,height))
#        pygame.draw.line(root,(255,255,255),(0,i), (width,i))
#    if c>0:
#        c=0
#        
#    c+=1

    pygame.display.update()
    clock.tick(60)
    #print(len(Coords.inst), clock.get_fps())
pygame.quit()
print(len(Coords.inst))
