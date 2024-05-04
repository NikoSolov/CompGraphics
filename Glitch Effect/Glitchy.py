
import pygame
import pygame.camera as cam
from random import randint
pygame.init()
cam.init()
#------------------------
maxCountCrop=50
minWidth, maxWidth = 30,100
minHeight, maxHeight = 30,100
#------------------------
camFlag=False
if (len(cam.list_cameras())!=0):
    camFlag=True
    camera=cam.Camera(cam.list_cameras()[0], (640,480))
    camera.start()
 
root=pygame.display.set_mode((640,480))
clock=pygame.time.Clock()
game=True
#------------
gradSurf = pygame.image.load("image.png")
#-------------
clk=0
while game:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            game=False
            

    if camFlag:
        pic = camera.get_image()
    else:
        pic=gradSurf


    if clk%5==0:
        root.fill((0,0,0))
        root.blit(pic, (0,0))
    if clk%10==0:
        for i in range(randint(1,maxCountCrop)):
            width=randint(minWidth, maxWidth)
            height=randint(minHeight, maxHeight)
            x=randint(0,640-width)
            y=randint(0,480-height)
            root.blit(pic.subsurface(x,y,width,height), (randint(0,640-width), randint(0,480-height)))
    pygame.display.update()
    clock.tick(60)
    clk+=1
pygame.quit()
camera.stop()