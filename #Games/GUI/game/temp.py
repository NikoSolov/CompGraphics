import pygame
import os
'''
# FOR RASPBERRY GPIO

import RPi.GPIO as GPIO
f=True
def gpion():
    global f
    if f==True: GPIO.output(2, False); f=False
    else: GPIO.output(2, True); f=True
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, False)

'''
# Setup
# Do Once
pygame.init()
pygame.mixer.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,100)
# Do More
root = pygame.display.set_mode((500,500))
pygame.display.set_caption("Something in my way")

Icon = pygame.image.load("Soul.png")
pygame.display.set_icon(Icon)

pygame.mixer.music.load("mus_anothermedium.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)


class Object():
    def draw(self, sprites, direction):
        sprite=pygame.image.load(self.image)
        #SpriteSheet
        sprite=pygame.transform.scale(sprite, (sprite.get_width()*self.scale, sprite.get_height()*self.scale))
        sprite=pygame.transform.rotate(sprite, self.angle)
        if (self.sprite_index>self.sprites-1): self.sprite_index=0
        root.blit(sprite,(self.x,self.y),(16*self.scale*self.sprite_index,32*self.scale*self.sprite_direction,16*self.scale,32*self.scale))
# Asterix
asterix=Object()
asterix.x=16
asterix.y=32
asterix.width=16
asterix.height=32
asterix.speed=5
asterix.scale=4
asterix.angle=0
asterix.sprites=4
asterix.sprite_index=0
asterix.sprite_direction=0
asterix.image='asterix.png'

game=True

clock=pygame.time.Clock()
# Functions
def draw():
    root.fill((128,128,128))
    asterix.draw(4, 4)
    pygame.display.update()
i=0
# Game LOOP
while game:
    i+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    keys = pygame.key.get_pressed()
    # Check keys
    if keys[pygame.K_LEFT] and asterix.x>4:
        asterix.x-=asterix.speed
        asterix.sprite_direction=1
        if (i%5==0):asterix.sprite_index+=1
    elif keys[pygame.K_RIGHT] and asterix.x<500-asterix.width*asterix.scale-4:
        asterix.x+=asterix.speed
        asterix.sprite_direction=2
        if (i%5==0):asterix.sprite_index+=1
    elif keys[pygame.K_UP] and asterix.y>4:
        asterix.y-=asterix.speed
        asterix.sprite_direction=3
        if (i%5==0):asterix.sprite_index+=1
    elif keys[pygame.K_DOWN] and asterix.y<500-asterix.height*asterix.scale-4:
        asterix.y+=asterix.speed
        asterix.sprite_direction=0
        if (i%5==0):asterix.sprite_index+=1
    else: asterix.sprite_index=0
    draw()
    clock.tick(60)
    
pygame.quit()
