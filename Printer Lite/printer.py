import pygame as pg
pg.init()

width,height=1024,768

root=pg.display.set_mode((width, height))
clock=pg.time.Clock()

game=True

class line():
    a=[]
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        line.a.append(self)
    def draw(root):
        for i in line.a:
            pg.draw.line(root,(255,255,255),(i.x1,i.y1),(i.x2,i.y2),2)
    def check():
        #pg.mouse.set_cursor(pg.cursors.arrow)
        x,y=pg.mouse.get_pos()
        flag=pg.mouse.get_pressed()[0]
        rel_x,rel_y=abs(pg.mouse.get_rel()[0]),abs(pg.mouse.get_rel()[1])
        point=False
#        print(x,y)
        for i in line.a:
            if (x>=i.x1-2 and x<=i.x1+2 and y>=i.y1-2 and y<=i.y1+2) or\
               (x>=i.x2-2 and x<=i.x2+2 and y>=i.y2-2 and y<=i.y2+2):
                pg.mouse.set_cursor(pg.cursors.diamond)
                point=True
                break
            else:pg.mouse.set_cursor(pg.cursors.arrow); point=False
        if flag and point:
            print(rel_x,rel_y)
            for i in line.a:
                if (x>=i.x1-rel_x*2 and x<=i.x1+rel_x*2 and y>=i.y1-rel_y*2 and y<=i.y1+rel_y*2):
                    i.x1,i.y1=pg.mouse.get_pos()
                elif (x>=i.x2-rel_x*2 and x<=i.x2+rel_x*2 and y>=i.y2-rel_y*2 and y<=i.y2+rel_y*2):
                    i.x2,i.y2=pg.mouse.get_pos()                
            
            
line(100,100,500,400)

while game:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            game=False
    root.fill((0,0,0))
    line.draw(root)
    line.check()
    pg.display.update()
    clock.tick(60)

pg.quit()