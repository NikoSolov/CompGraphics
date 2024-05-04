import pygame
from math import sin
from pygame._sdl2 import Window, Texture, Image, Renderer, get_drivers, messagebox
clock = pygame.time.Clock()
#--------------------
winSize = (200,100)
winCount = 60
winDistance = 20
A = 200
F = 100
offSpeed = 20
#--------------------

a=[]
for i in range(winCount):
    a.append(Window("DUNE",winSize))
    a[i].opacity=0.5
    a[i].position=(i*winDistance,200)
off=0
game=True
while game:
    for event in pygame.event.get():
        if (event.type==pygame.QUIT or (event.type==pygame.KEYDOWN)):
            game=False
    for i in range(len(a)):
        x,y=a[i].position
        y=400+sin((x+off)/F)*A
        a[i].position=x,y
    off+=offSpeed
    clock.tick(60)
pygame.quit()