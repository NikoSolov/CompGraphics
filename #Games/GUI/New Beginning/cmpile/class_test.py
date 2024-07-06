from random import randint, getrandbits
import pygame
from math import sin, cos, radians, pi
pygame.init()
game=True
width=round(pi*200)
height=round(pi*200)
root=pygame.display.set_mode((width, height))#, pygame.FULLSCREEN )
#root=pygame.Surface((width,height))
clock=pygame.time.Clock()


class Coords():
    def __init__(self, x,y, color, xstep, ystep):
        self.x=x
        self.y=y
        self.color=color
        self.xstep=xstep
        self.ystep=ystep
        self.xstate=0
        self.ystate=0
        self.get=False
        self.radius=100
        self.counter=0
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
        self.x=self.x+(cos(radians(self.y)))*3#+cos(3*radians(self.y))/0.5#+cos(5*radians(self.y))/5+cos(7*radians(self.y))/7
        self.y=self.y+(sin(radians(self.x)))*3#+sin(3*radians(self.x))/0.5#+sin(5*radians(self.x))/5+sin(7*radians(self.x))/7
        
    def whirlpool2(self, root):
        pygame.draw.rect(root, self.color,(self.x,self.y,5,5))
        self.a=self.x
        self.x=self.x+(cos(radians(self.y)))*3
        self.y=self.y+(sin(radians(self.a)))*3
        
a=[]
for i in range(1000):
    a.append(Coords(randint(0,width),randint(0,height), (randint(0,255),randint(0,255),randint(0,255),255), randint(1,4), randint(-4,-1)))
print("DONE!!!")

s = pygame.Surface((width,height), pygame.SRCALPHA)
s.set_alpha(35)               
s.fill((0,0,0))           

#a.append(Coords(round(pi)*60,round(pi)*60, (randint(0,255),randint(0,255),randint(0,255),255), randint(-4,4), randint(-4,4)))
#a.append(Coords(randint(0,640),randint(0,480), (randint(0,255),randint(0,255),randint(0,255),255), randint(-4,4), randint(-4,4)))
c=0
while game:# and c<300:
    #a.append(Coords(randint(0,640),randint(0,480), (randint(0,255),randint(0,255),randint(0,255),255), randint(-4,4), randint(-4,4)))
    for event in pygame.event.get():
        if event.type==pygame.QUIT: game=False

    for i in range(len(a)):
        #a[i].lines(root)
        a[i].whirlpool(root)
        #print(a[0].x)
    root.blit(s, (0,0))
    #for i in range(0,1000,10):
    #    pygame.draw.line(root,(255,255,255),(round(pi)*i,0), (round(pi)*i,height))
    #    pygame.draw.line(root,(255,255,255),(0,round(pi)*i), (width,round(pi)*i))
    #pygame.draw.rect(root,(0,255,255),(round(pi)*60, round(pi)*60,5,5 ))
    #print(len(a))
    #pygame.image.save(root, "gif/"+str(c)+".png")
    pygame.display.update()
    c+=1
    #clock.tick(60)
pygame.quit()
print("also Done!!!")
