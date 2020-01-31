# dongdong.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "green", "blue", "red", "blue", "red", "blue"]
your_name = turtle.textinput("Enter your name", "What is your name?")
size = int(turtle.textinput("Number of sides","How many sides do your want (1-10)!"))
for x in range(100):
    t.pencolor( colors[ x % size] )
    t.penup()
    t.forward( x * 3 / size + x)
    t.left(360/size + 1)
    t.pendown()
    t.write(your_name, font = ("Times", int( (x + 4) / 4), "bold") )
    t.width(x*size/90)

