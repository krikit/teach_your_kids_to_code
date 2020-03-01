import random
import turtle
t = turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor("white")
def draw_similey(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    #Head
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    #left eye
    t.setpos(x-15, y+60)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    #right eye
    t.setpos(x+15, y+60)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    #mouth
    t.setpos(x-25, y+40)
    t.pencolor("red")
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)
for n in range(50):
    x = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
                         turtle.window_height()//2)
    draw_similey(x,y)
