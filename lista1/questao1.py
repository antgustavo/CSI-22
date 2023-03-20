from turtle import *

pencolor("pink")
bgcolor("green")
speed(0)
width(2)

for j in range(5):
    setpos(-10*j,-10*j)
    pendown()
    for i in range(4):
        forward(20+20*j)
        left(90)
    penup()
done()
