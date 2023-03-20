from turtle import *

pencolor("blue")
bgcolor("green")
c = 0 
speed(0)

penup()
setpos(-200,0)
pendown()

for j in range(103):
    c+=3
    right(90)
    forward(c)
right(90)
c = 0

penup()
setpos(200,0)
pendown()

for j in range(103):
    c+=3
    right(89)
    forward(c)
right(90)

done()