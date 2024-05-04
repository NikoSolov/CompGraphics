import pygame
pygame.init()
from math import sin
pygame.init()
###################### FUNCTIONS #######################################
def wave(image, offset, clock, applitude, period, typ, flip):
    clck=offset
    clck+=clock
    wavedimage=pygame.Surface((image.get_width()+applitude*2, image.get_height()+applitude*2), pygame.SRCALPHA)
    if typ==True:
        if flip==False:
            for i in range(image.get_height()):
                solve=round(sin((clck-i)/period)*applitude+applitude)
                wavedimage.blit(image,(0,i),(solve,i,image.get_width(),1))
        else:
            for i in range(image.get_width()):
                solve=round(sin((clck-i)/period)*applitude)+applitude
                wavedimage.blit(image,(i,0),(i,solve,1,image.get_height()))
    else:
        if flip==False:
            for i in range(image.get_height()):
                solve=round(sin((clck-i)/period)*applitude+applitude)
                wavedimage.blit(image,(0,i),(0,i+solve,image.get_width(),1))
        else:
            for i in range(image.get_width()):
                solve=round(sin((clck-i)/period)*applitude)+applitude
                wavedimage.blit(image,(i,0),(i+solve,0,1,image.get_height()))
    return wavedimage
#-------------------------------------------------------------------------------#
def mosaic(image, extent):
    changed_image=pygame.transform.scale(image,(image.get_width()-extent%image.get_width(),image.get_height()-extent%image.get_height()))
    changed_image=pygame.transform.scale(changed_image,(changed_image.get_width()+extent%image.get_width(),changed_image.get_height()+extent%image.get_height()))        
    return changed_image
#-------------------------------------------------------------------------------#
def TV_Frame(image, offset, clock, applitude, period, mode):
    clck=offset
    clck+=clock
    changed_image=pygame.Surface((image.get_width(),image.get_height()), pygame.SRCALPHA)    
    if mode=='H':
        for i in range(image.get_width()):
            solve=round(sin((clk-i)/period)*255)
            imag=image.subsurface((i,0,1,image.get_height()))
            imag.set_alpha(255-solve)
            changed_image.blit(imag,(i,0))
    elif mode=='V':
        for i in range(image.get_height()):
            solve=round(sin((clk-i)/period)*255)
            imag=image.subsurface((0,i,image.get_width(),1))
            imag.set_alpha(255-solve)
            changed_image.blit(imag,(0,i))
    elif mode=='B':
        for i in range(image.get_height()):
            solve=round(sin((clk-i)/period)*255)
            imag=image.subsurface((0,i,image.get_width(),1))
            imag.set_alpha(255-solve)
            changed_image.blit(imag,(0,i))
        for i in range(image.get_width()):
            solve=round(sin((clk-i)/period)*255)
            imag=image.subsurface((i,0,1,image.get_height()))
            imag.set_alpha(255-solve)
            changed_image.blit(imag,(i,0))            
    return changed_image
###################################################################################

root=pygame.display.set_mode((1280,512))
clock=pygame.time.Clock()
game=True
clk=0
sec=0
############################ GAME START ######################################
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: game=False
    
    root.fill((128,128,128))
    
    img=pygame.image.load("giygas.png")
#substring
    wavedimage=pygame.Surface((img.get_width()+4*2, img.get_height()+4*2), pygame.SRCALPHA)
    for i in range(img.get_height()):
        solve=round(sin((clk-i)/15)*(10-round(sin(sec)*10)))
        if i%2==0:
            wavedimage.blit(img,(0,i),(10+solve,i,img.get_width(),1))
        else:
            wavedimage.blit(img,(0,i),(10-solve,i,img.get_width(),1))
    root.blit(wavedimage,(1024,256))
#поперечные волны
    clk+=2
    root.blit(wave(img,5,clk,3,15, True,  True),(0,0))
    root.blit(wave(img,0,clk,3,15, False, True),(256,0))
#продольные волны
    root.blit(wave(img,5,clk,3,15, True,  False),(0,256))
    root.blit(wave(img,0,clk,3,15, False, False),(256,256))
#TV_frame(Телевизор, который медленно прорисовывает кадр)
    root.blit(TV_Frame(img, 5, clk, 3, 15, 'V'),(512,0))
    root.blit(TV_Frame(img, 5, clk, 3, 15, 'H'),(512,256))
    root.blit(TV_Frame(img, 5, clk, 3, 15, 'B'),(768,256))
#mosaic effect
    root.blit(mosaic(img,clk),(768,0))
#WOMBO_COMBO MODE
    root.blit(
        wave(
            wave(
                wave(
                    wave(
                        mosaic(
                            TV_Frame(img, 5, clk, 3, 15, 'B'),
                        clk),
                    5,clk,3,15, True,  True),
                5,clk,3,15, True,  False),
            5,clk,3,15, False,  True),
        5,clk,3,15, False,  False),
        (768,256)
        )
#Transparency
    sec+=0.01
    imag=pygame.image.load("giygas.png")
    imag.set_alpha(128)
    root.blit(wave(imag,45,clk,10-round(sin(sec)*10),15, True,  False),(1024,0))
    root.blit(wave(imag,0,clk,10-round(sin(sec)*10),15, True,  False),(1024,0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
