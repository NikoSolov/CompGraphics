import pygame
from classes import *

class main():
    muse=mouse(0,0,(30,30))
    game=True
    width,height=640,480
    root=pygame.display.set_mode((width, height))
   
    while game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print('doen') 
                game=False
#            if event.type==pygame.KEYDOWN:
#                print("down")

        root.fill((128,128,128))

        muse.update()

        pygame.display.update()

    pygame.quit()


if __name__=='__main__':
    main()

