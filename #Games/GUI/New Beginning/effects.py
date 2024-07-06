import pygame as pg
from math import sin, radians
clock=pg.time.Clock()
game=True
width,height=1024,768
#width,height=512, 384

root=pg.display.set_mode((width,height))

class image():
    def __init__(self):
        global width, height
        self.image=pg.image.load("deltarune.png")
        self.image=pg.transform.scale(self.image, (self.image.get_width()*8, self.image.get_height()*8,))
        print(self.image.get_width())
        self.x=width//2-self.image.get_width()//2
        self.y=height//2-self.image.get_height()//2
        self.a=32
        self.counter=0
        self.amp=100
        self.period=0.1
        self.mode="wave_in"
        #self.image.set_alpha(self.a)
    def draw(self, root):
        self.image.set_alpha(self.a)
        if self.mode=="default":  
            root.blit(self.image,(self.x,self.y))
        elif self.mode=="wave_in":
            for i in range(self.image.get_height()):
                root.blit(self.image,
                    (self.x+round(sin(radians(self.counter+i)/self.period)*self.amp),
                    self.y+i),(0,i,self.image.get_width(),2))
            self.counter+=1
            self.amp-=0.5
            if self.amp<1: self.mode="default"
#            self.amp-=1

delta=image()
delta.y=0
delta.a=255
a=[]
for i in range(8):
    a.append(image())
    a[i].counter+=i
    #a[i].y-=i*10
#a[0].y=0    
    
while game:
    for event in pg.event.get():
        if event.type==pg.QUIT: game=False
    root.fill((0,0,0))
    delta.draw(root)
    for i in range(len(a)):
        a[i].draw(root)

    #print(root.get_at((a[0].x,a[0].y)), root.get_at((delta.x,delta.y)))
                
    clock.tick(30)
    pg.display.update()
pg.quit()
