import pygame
pygame.init()
game=True

root=pygame.display.set_mode((640, 480))
clock=pygame.time.Clock()

class Sprite():
    def __init__(self,source, sprite_array, coords, direction, scale=1):
        self.sprite_array=sprite_array
        self.source=source
        (self.x, self.y)=coords
        self.sprite_num=0
        self.sprite_time=0
        self.counter=0
        self.scale=scale
        self.sprite_anim=False
        self.directions={"down":0, "up":1, "left":2, "right":3}
        self.dir="down"
    def draw(self,root):
        #print(self.directions[self.dir], self.sprite_num)
        img=pygame.transform.scale(
            pygame.image.load(self.source).subsurface(self.sprite_array[self.directions[self.dir]][self.sprite_num]),
            (self.sprite_array[self.directions[self.dir]][2]*self.scale,
             self.sprite_array[self.directions[self.dir]][3]*self.scale))
        root.blit(img,(self.x,self.y))

array=[[(0,0,19,29), (19,0,19,29), (0,0,19,29), (38,0,19,29)],
       [(57,0,19,29), (76,0,19,29), (57,0,19,29), (95,0,19,29)],
       [(114,0,17,29), (131,0,17,29)],
       [(148,0,17,29), (165,0,17,29)]
      ]
Frisk=Sprite("frisk.png", array, (0,0), "down", 5)

while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: game=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: Frisk.x-=1; Frisk.dir="left"
    if keys[pygame.K_RIGHT]: Frisk.x+=1; Frisk.dir="right"
    if keys[pygame.K_UP]: Frisk.y-=1; Frisk.dir="up"
    if keys[pygame.K_DOWN]: Frisk.y+=1; Frisk.dir="down"


    root.fill((0,0,0))
    
    Frisk.draw(root)

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
