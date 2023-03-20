from turtle import *

def draw_poly(t, n, sz):
    speed(0)
    bgcolor("green")
    pencolor("pink")
    width(t)
    for i in range(n):
        forward(sz)
        left(360/n)
    done()

draw_poly(2,9,50)