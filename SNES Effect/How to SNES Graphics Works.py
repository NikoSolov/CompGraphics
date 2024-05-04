import pygame
from math import sin
from random import randint as rand
pygame.init()

root=pygame.display.set_mode((512,512))
clock=pygame.time.Clock()
game=True
i=0
clk=0
#-----------------------------
image=pygame.image.load("giygas.png")
#-----------------------------
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: game=False
################################################
    root.fill((128,128,128))
    period=15
    applitude=20
    solve=round(sin((clk-i)/period)*applitude)

    root.blit(image,(256,solve))
    pygame.draw.rect(root,(255,255,255),(256,i-1,image.get_width(),1))

    for y in range(i):
        sol=round(sin((clk-y)/period)*applitude)
        root.blit(
            image,
            (0,y),(0,y+sol,image.get_width(),1))
    pygame.draw.rect(root,(255,255,255),(0,i-1,image.get_width(),1))

    root.blit(image,(256+solve,256))
    pygame.draw.rect(root,(255,255,255),(256,256+i-1,image.get_width(),1))

    for y in range(i):
        sol=round(sin((clk-y)/period)*applitude)
        root.blit(
            image,
            (0,y+256),(sol,y,image.get_width(),1))
    pygame.draw.rect(root,(255,255,255),(0,256+i-1,image.get_width(),1))
    
    if i<image.get_height():
       i+=1
    else: i=0; clk+=1
    
################################################
    pygame.display.update()
    clock.tick(60)
pygame.quit()