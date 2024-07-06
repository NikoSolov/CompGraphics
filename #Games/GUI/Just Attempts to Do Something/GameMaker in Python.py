import pygame                                   #
import os                                       #
clock=pygame.time.Clock()                       #
clk=0                                           #
game=True                                       #
#################################################
image=pygame.image.load("sprites.png")
class Screen():#?
    def __init__(self,x=0,y=0,width=1024,height=768,caption="GameMakerStudio in Python", icon=None):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.root=pygame.display.set_mode((self.width,self.height))
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (self.x,self.y)
        os.environ['SDL_VIDEO_CENTERED'] = '0'
        self.caption=caption
        pygame.display.set_caption(caption)
        if icon==None:
            self.icon=pygame.image.load("logo.png")
        else:
            self.icon=icon
        pygame.display.set_icon(self.icon)
    def Redreding(self,surface,coord):
        self.root.blit(surface, coord)
##########################################################################
class viewport:
    class camera:
        pass
    def __init__(self,x,y,width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def set_camera(self, x,y,width,height, angle=0):
        self.camera.x=x
        self.camera.y=y
        self.camera.width=width
        self.camera.height=height
        self.camera.angle=angle
    def surf(self,room):
        surf=pygame.Surface((self.width,self.height))
        image=room.subsurface((self.camera.x,self.camera.y, self.camera.width, self.camera.height))
        image=pygame.transform.rotate(image, self.camera.angle)
        surf.blit(pygame.transform.scale(image,(self.width, self.height)),(0,0))
        return surf
#######################################################################
def Room(width=1024, height=768, *layers):
    surf=pygame.Surface((width,height))
    surf.fill((128,128,128))
    for layer in layers:
        surf.blit(layer,(0,0))
    return surf
##########################################################################
class tilemap():
    clk=0
    def surf(self,image, tileset):
        surf=pygame.Surface((tileset[0][0],tileset[0][1]))
        for y in range(1, len(tileset)):
            for x in range(len(tileset[y])):
                if type(tileset[y][x]) is list:
                    surf.blit(image, (x*tileset[0][2],(y-1)*tileset[0][3]),
                    (tileset [y] [x] [self.clk % len( tileset[y] [x] )] * tileset[0][2] % image.get_width(),
                     tileset [y] [x] [self.clk % len( tileset[y] [x] )] * tileset[0][2] // image.get_width() * tileset[0][3],
                     tileset [0][2], tileset [0][3]))
                else:
                    surf.blit(image, (x*tileset[0][2],(y-1)*tileset[0][3]),
                    (tileset [y] [x] * tileset[0][2] % image.get_width(),
                     tileset [y] [x] * tileset[0][2] // image.get_width() * tileset[0][3],
                     tileset [0][2], tileset [0][3]))
        return surf
#########################################################3
class instances:
    pass
##########################################################
screen=Screen(0,0,500,500)
tilemap=[
    (0,0,16,16,500,500),
    [(1,0),(2,0),(3,0)],
    [(3,0),(3,0),(3,0)],
    [(1,0),(2,0),(3,0)],
    [(3,0),(3,0),(3,0)]
    ]
tileset1=[
    (0,0,16,16, 500,500),
    [(1,0),(2,0),(3,0)],
    [(3,0),(3,0),(3,0)]
    ]
tileset2=[
    (0,0,16,16, 500,500),
    [(1,0),(2,0),(3,0)],
    [(3,0),(3,0),(3,0)]
    ]

viewport0=viewport(0,0,500,500)
viewport0.set_camera(0,0,100,100)
###############################################################
while game:                                                   #
    for event in pygame.event.get():                          #
        if event.type == pygame.QUIT: game=False              #
    keys = pygame.key.get_pressed()                           #
    if keys[pygame.K_ESCAPE]: game=False                      #
###############################################################
    room=Room(1000,1000,tilemap(tileset))
    viewport0.x+=1
    viewport0.y+=1
    
#camera
#root.blit(pygame.transform.scale(Room.surf.subsurface((camera.x,camera.y,camera.width, camera.height)),(viewport.width, viewport.height)),(0,0))


#################################################
    screen.Redreding(viewport0.surf(room),(viewport0.x,viewport0.y))#      #
    screen.Redreding(viewport0.surf(room),(viewport0.x+100,viewport0.y))#      #
    pygame.display.update()                     #
    clock.tick(60)                              #
    clk+=1                                      #
pygame.quit()                                   #
#################################################
