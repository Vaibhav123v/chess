import turtle
import time

t = turtle.Turtle()
t.speed(0)
def box(ln):
    for i in range(4):
        t.forward(ln)
        t.left(90)

x=0
y=0
count =2
while True:
    t.goto(x,y)
    t.pendown()
    x+=40
    t.begin_fill()
    if count%2==0:
        t.fillcolor("yellow")
    else:
        t.fillcolor("red")

    count +=1
    box(40)
    t.end_fill()
    
    if x>=40*8:
        x =0
        y +=40
        t.penup()
        count+=1

    if y >=40*8:
        break

t.hideturtle()
turtle.done()
