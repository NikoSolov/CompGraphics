import pygame
import os.path
from SymGen import Print
pygame.mixer.init()
pygame.init()
#Initialise Main Surfaces
root = pygame.display.set_mode((800,480))
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10,100)
cursor = pygame.Surface((32,32), pygame.SRCALPHA)
#Initialise Resources
image=pygame.image.load("sprites.png")
pygame.mixer.music.load('music.ogg')
pygame.mixer.Sound
clock=pygame.time.Clock()
homedir = os.path.expanduser("~")


#Game START!!!
game=True
FPS=30
animation=0
icony=0
###########################################
sec2=0
txt="INSTRUCTIONS!"
l=True
x1=0
y1=331
ln=0



#TextBox.fill((255,255,255))
#pygame.draw.rect(TextBox, (0,0,0), (5,5,190,190))
###########################################
from math import cos
from math import sin
class Graphic():
    def __init__(self, offset):
        self.clock=offset
# нужно научиться устанавливать self.clock --> offset
    def wave(self,image, applitude, period, speed, x):
        self.clock+=speed
        wavedimage=pygame.Surface((image.get_width()+applitude*2, image.get_height()+applitude*2), pygame.SRCALPHA)
        # HDMA is POWER!!!!
        if x==True:
            for i in range(image.get_height()):
                solve=round(sin((self.clock-i)/period)*applitude)+applitude
   #             wavedimage.blit(image,(0,i),(0,i+solve,image.get_width(),1))
                wavedimage.blit(image,(applitude,i),(solve,i,image.get_width(),1))
        else:
            for i in range(image.get_width()):
                solve=round(sin((self.clock-i)/period)*applitude)+applitude
   #             wavedimage.blit(image,(i,0),(i+solve,0,1,image.get_height()))
                wavedimage.blit(image,(i,applitude),(i,solve,1,image.get_height()))
        return wavedimage

Effects=Graphic(0)
##############################################
class Object():
    def __init__(self,x,y,image,rows,columns, uppart):
        self.image=image
        self.rows=rows
        self.columns=columns
        self.uppart=uppart
        self.x=x
        self.y=y
        self.anim=0
        self.direction=1
    def sprite(self):
        if self.anim>self.columns-1: self.anim=0
        sprite=self.image.subsurface((self.anim*self.image.get_width()/self.columns, self.direction*self.image.get_height()/self.rows, self.image.get_width()/self.columns, self.image.get_height()/self.rows))
        up=sprite.subsurface(0,0,self.image.get_width()/self.columns,self.uppart)
        down=sprite.subsurface((0,self.uppart,self.image.get_width()/self.columns,self.image.get_height()/self.rows-self.uppart))
        return sprite, up, down

Pongy=Object(30,30,image.subsurface(0,64,80,164), 4,4,22)
############################################
sec3=0
#Initialise Main Surfaces
#################################

Secret=False
if Secret:
    exe="Апогей БК-01ц\Апогей БК-01ц.exe"
    os.startfile(r"%s" % exe)
elif os.path.exists(homedir+"\Desktop\Secret.txt"): os.remove(homedir+"\Desktop\Secret.txt")
#################################
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
#############################################################    
    MusID=3
    pygame.mixer.music.set_volume(0)
    musicsheet=[[0,(2*60+53)*1000],
                [(2*60+55)*1000,(8*60+40)*1000],
                [(8*60+41)*1000,(12*60+19)*1000],
                [(12*60+20)*1000,(16*60+56)*1000]]
    if pygame.mixer.music.get_pos()>musicsheet[MusID][1]-musicsheet[MusID][0] or pygame.mixer.music.get_pos()==-1:
        pygame.mixer.music.play(-1,musicsheet[MusID][0]/1000)
#################################################################
    Icon = pygame.Surface((16,16), pygame.SRCALPHA)
    GUI=pygame.Surface((root.get_width(), root.get_width()), pygame.SRCALPHA)
    TextBox=pygame.Surface((200,200), pygame.SRCALPHA)
#    TextBox.set_palette([(0,0,0),(0,255,0)])
############  Secret of Intel 8080 (Windows)  ###################
    if Secret==True: 
        file = open(homedir+"\Desktop\Secret.txt", "w")
        file.write("Well, I impress. But, actually, you get just part of secret...\n0000: ")
        i=0
        for i in range(25):
            for j in range(16):
                for k in range(4):
                    A=image.subsurface((496,16,16,25)).get_at((j,i))[k]
                    if A<16: A="0"+str(hex(int(A)))[2:].upper()
                    else: A=str(hex(int(A)))[2:].upper()
                    file.write(A)
                    file.write(" ")
            if icony>41: icony=0
            Icon.blit(image.subsurface((496,icony,16,16)), (0,0))
            icony+=1    
        Secret=False
        Icon = pygame.Surface((16,16),pygame.SRCALPHA)
        file.write("\nAnd you must copy this...\nCheck your checksum: K,61F\n=>0000\n=>061F\n=>0C00")
        file.close()
        print("DONE!")
    else: Icon.fill((0,255,0))
#################################################################
    TileSet=[[500,500],
             [[6,0,True,False],[5,0,True,False],[5,0,False,False],[6,0,False,False],[1,0,False,False]],
             [[4,0,False,False],[3,0,False,False],[3,0,False,False],[3,0,False,False],[3,0,False,False],[4,0,True,False]],
             [[3,0,False,False],[3,0,False,False],[3,0,False,False],[3,0,False,False],[3,0,False,False],[3,0,False,False]],
             [[4,0,False,True],[3,0,False,False],[3,0,False,False],[3,0,False,False],[3,0,False,False],[4,0,True,True]],
             [[1,0,False,True],[6,0,True,True],[5,0,True,True],[5,0,False,True],[6,0,False,True],[1,0,False,False]]]
    TileSet1=pygame.Surface((TileSet[0][0],TileSet[0][1]), pygame.SRCALPHA)
    for i in range(1,len(TileSet)): #Tile
        for j in range(len(TileSet[i])): #Pos_Tile
            Tile=pygame.transform.flip(image.subsurface(16*TileSet[i][j][0],16*TileSet[i][j][1],16,16), TileSet[i][j][2],TileSet[i][j][3])
            Tile=pygame.transform.scale(Tile, (Tile.get_width()*2,Tile.get_height()*2))
            TileSet1.blit(Tile,(j*16,(i-1)*16))
##########################################################
    animation+=1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:Pongy.direction=3;  Pongy.x-=2
    if keys[pygame.K_RIGHT]:Pongy.direction=2;  Pongy.x+=2
    if keys[pygame.K_UP]:Pongy.direction=0;  Pongy.y-=2
    if keys[pygame.K_DOWN]:Pongy.direction=1;  Pongy.y+=2
    if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]) and animation%5==0:
        Pongy.anim+=1
    if keys[pygame.K_ESCAPE]: game=False
    if keys[pygame.K_SPACE]: Secret=True
#################################################
    guy=pygame.Surface((8,8),pygame.SRCALPHA)
    guy_tiles=[[(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128)],
              [(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128)],
              [(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128)],
              [(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128)],
              [(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128),(128,128,128)],
              ]
##################################################
    sec2+=1
    if l==True:
        l=False
        if ln<=len(txt):ln+=1
        sec2=0
    for i in range(ln-1):
        TextBox.blit(image, (i*8+20,10), ((ord(txt[i])-32)//16*6,228+(ord(txt[i])-32)%16*8,5,7))
    if y1<(ord(txt[ln-1])-32)%16*8+228 and ln!=len(txt): y1+=1
    if x1<(ord(txt[ln-1])-32)//16*6 and ln!=len(txt): x1+=1
    
    if x1>=(ord(txt[ln-1])-32)//16*6 and y1>=((ord(txt[ln-1])-32)%16*8+228):
        x1=0
        y1=228
        l=True
    TextBox.blit(image, ((ln-1)*8+20,10), (x1,y1,5,7))
############################################################3
    sec3+=1

    pygame.mouse.set_visible(False)
    cursor.blit(image,(0,0),(144+sec3*32, 0, 32, 32))
    coord = pygame.mouse.get_pos()
    if sec3>5: sec3=0
############################################################3
##############################################################    
    #----Draw What You Want-----
    #BackGround Rendering
    root.fill((128,128,128))
    map=pygame.Surface((300,300))
    #TileSets 1(Map)
   # map.blit(TileSet1,(0,0))
    #Character
    map.blit(Pongy.sprite()[2],(Pongy.x, Pongy.y+Pongy.uppart))
  #  map.blit(man.sprite()[2],(man.x, man.y+man.uppart))
    map.blit(Pongy.sprite()[2],(100, 50+Pongy.uppart))
    map.blit(Pongy.sprite()[1],(Pongy.x, Pongy.y))
   # map.blit(man.sprite()[1],(man.x, man.y))
    map.blit(Pongy.sprite()[1],(100, 50))
    #TileSets 2
#    root.blit(TileSet2,(0,0))
    #---------------------------
    #GUI 1
    GUI=pygame.Surface((root.get_width(), root.get_width()), pygame.SRCALPHA)    
    GUI.blit(TextBox, (0,20))
    #GUI 2
#    GUI.blit(foregnd, (0,0))    
    #---------------------------
    maped = pygame.transform.scale(map, (map.get_width()*4, map.get_height()*4))   
    maped = pygame.transform.rotate(maped, 0)
    ###
    GUIed = pygame.transform.scale(GUI, (GUI.get_width()*2, GUI.get_height()*2))   
    GUIed = pygame.transform.rotate(GUIed, 0)
    ####
    root.blit(maped, (0,0))
    root.blit(GUIed, (0,0))
    data="x: "+str(Pongy.x)
    root.blit(Print(data, scale=4),(0,0))
    root.blit(cursor, coord)
    #Display Update
    pygame.display.update()
    #---------------------------
    clock.tick(FPS)

    #Timer FPS
    #    UwU
pygame.quit()
#END OF GAME




