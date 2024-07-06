import pygame
root=pygame.display.set_mode((1024,512))
game=True
clock=pygame.time.Clock()
surf=pygame.Surface((512,512))
surf.fill((128,128,128))
cursor=pygame.Surface((64,64))

tiles=pygame.image.load("sprites.png").subsurface((0,0,128,64))
tiles=pygame.transform.scale(tiles, (tiles.get_width()*4,tiles.get_height()*4))
draw=False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: game=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: game=False
#-------------------------------------------------------#
    root.fill((0,0,0))

    if pygame.mouse.get_pos()[0]>512 and pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[1]<256:
        cursor=tiles.subsurface(((pygame.mouse.get_pos()[0]-512)//64)*64, (pygame.mouse.get_pos()[1]//64)*64, 64,64)
        draw=True
    if draw and pygame.mouse.get_pos()[0]<513 and pygame.mouse.get_pressed()[0]:
        print(True)
        surf.blit(cursor, ((pygame.mouse.get_pos()[0])//64*64, pygame.mouse.get_pos()[1]//64*64))
    if keys==False: key=True
    if keys[pygame.K_r]: cursor=pygame.transform.rotate(cursor, 90); key=False

    print(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
    root.blit(surf, (0,0))
    root.blit(tiles, (513,0))
    root.blit(cursor, (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
#------------------------------------------------------#
    pygame.display.update()

    clock.tick(60)

pygame.quit()

