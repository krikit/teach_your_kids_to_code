# dongdong.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "green", "blue", "red", "blue", "red", "blue"]
your_name = turtle.textinput("Enter your name", "What is your name?")
for x in range(100):
    t.pencolor( colors[ x % 4] )
    t.penup()
    t.forward( x * 4 )
    t.pendown()
    t.write(your_name, font = ("Times", int( (x + 4) / 4), "bold") )
    t.left(92)
