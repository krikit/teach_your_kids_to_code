# dongdong.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = 7
colors = ["red", "blue", "purple", "gold", "pink", "orange", "green" , "brown" , "yellow" , "white"]
for x in range(200):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 90)
    t.width(x*sides/200)
