# dongdong.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "green", "blue", "gray", "white", "purple", "orange"]
your_name = turtle.textinput("Enter your name", "How many circles do you want(1-8)?")
your_name = int(your_name)
for x in range(100):
    t.pencolor( colors[ x % 8] )
    t.circle( x )
    t.left(360/your_name + 1)
    t.width(x*your_name/90)
