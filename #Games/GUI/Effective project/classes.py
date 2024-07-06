import pygame

class mouse():
    def __init__(self,x,y,sprite=None,size=(10,10)):
        self.x=x
        self.y=y
        if sprite==None:
            self.size=size
            self.sur=pygame.Surface(size)

    def update(self):
        
        pass
