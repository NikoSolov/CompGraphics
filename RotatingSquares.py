#################################
#... Made by Nikolai Solovyov...#
#                               #
#...with love for people and    #
#    hatred of the government...#
#################################
import turtle
from math import sqrt

window = turtle.Screen()
window.setup(width=0.66, height=0.98)
turtle.speed(0)

array=['red','green','blue','yellow']

def set_start(q):
        turtle.penup()
        turtle.goto(0,0)
        turtle.backward(436)
        turtle.left(90) 
        turtle.forward(q)
        turtle.right(90)
        turtle.pendown()

def turle():
	turtle.right(45)
	turtle.forward(sqrt(150**2+150**2)/2)
	turtle.left(45-n)
	turtle.forward(2)
	turtle.left(46+n)
	turtle.forward(sqrt(150**2+150**2)/2)
	turtle.left(135)	
	turtle.forward(150)
	turtle.left(180)
	turtle.pendown()


set_start(340)

for n in range(360):
	for i in range (4):
		turtle.forward(150)
		turtle.right(90)
	turtle.penup()
	turle()

set_start(90)


for n in range(360):
	for i in range (4):
		turtle.color(array[i])
		turtle.forward(150)
		turtle.right(90)
	turtle.penup()
	turle()
        
array1=['red','orange','yellow','green','dodgerblue','blue','indigo']

turtle.penup()
turtle.goto(0,0)
turtle.backward(436)
turtle.right(90) 
turtle.forward(160)
turtle.right(90)
turtle.pendown()

for j in range (0, 360, 7):
	for i in range(7):
		turtle.color(array1[i])
		turtle.begin_fill()
		for n in range (4):
			turtle.forward(150)
			turtle.right(90)
		turtle.end_fill()
		turtle.right(45)
		turtle.forward(sqrt(150**2+150**2)/2)
		turtle.left(45-(i+j))
		turtle.forward(2)
		turtle.left(46+(i+j))
		turtle.forward(sqrt(150**2+150**2)/2)
		turtle.left(135)	
		turtle.forward(150)
		turtle.left(180)
		turtle.pendown()
turtle.mainloop()
