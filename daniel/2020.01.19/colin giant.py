# dongdong.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "blue", "red", "blue", "red", "blue", "red", "blue"]
for x in range(400):
    t.pencolor(colors[x % 8])
    t.forward(2 * x)
    t.right(360 / 8)
