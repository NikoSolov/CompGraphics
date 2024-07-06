import os, pygame
from random import randint

dic={"Р":(75,26), "Б":(171,26), "Ы":(267,26), "В":(363,26), "Т":(458,26), "Е":(123,74), "Ю":(219,74), "Ч":(315,74),"Ж":(411,74),
"Ш":(75,122), "Л":(171,122), "О":(267,122), "Э":(363,122), "Щ":(458,122), "П":(27,171), "Ё":(123,171), "И":(219,171), "М":(315,171),"Й":(411,171),"Н":(507,171),
"С":(75,220), "К":(171,220), "Ф":(267,220), "Я":(363,220), "У":(458,220), "Д":(123,266), "Х":(219,266), "Ц":(315,266),"З":(411,266),"А":(171,316),"Г":(363,316),
}

clock=pygame.time.Clock()
root=pygame.display.set_mode((536*2,344*2))
surf=pygame.Surface((536, 344))
lab=pygame.image.load("Room.png")

if os.path.isdir("Result_5")==False:
    os.mkdir("Result_5")

mylist = os.listdir("Files")

for file in mylist:
    n=0
    print(file)
    f=open("Files//"+file,"r",encoding='utf-8')
    if os.path.isdir("Result_5//"+file)==False:
        os.mkdir("Result_5//"+file)
    surf.blit(lab,(0,0))
    

    coord=dic["О"]
    c=0
    for i in range(15):
        f.readline()
        
    a=f.readline()
    while a!="":
        sym=a[a.find(":")+a.find('\t')+1+1:][0]
        b=ord(sym)
        if (b>1039 and b<1072 or b==1025):
            if coord==(0,0):coord=dic[sym]
            else:
                pygame.draw.line(surf, (randint(64,255),randint(64,255),randint(64,255)),coord, dic[sym], width=4)
                pygame.image.save(surf, "Result_5//"+file+"//"+str(n)+".png")
                n+=1
                root.blit(pygame.transform.scale(surf, (536*2,344*2)), (0,0))
                coord=dic[sym]
        if sym=='+' and c==0:
            c=1
        elif sym=='+' and c==1:
            surf.blit(lab,(0,0))
            c=0
        a=f.readline()
        pygame.display.update()
        #clock.tick(60)
    f.close()
pygame.quit()
    
