# dongdong.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "blue", "purple", "gold", "pink", "blue", "red", "blue"]
your_name = turtle.textinput("Enter sour name","what is your name?")
for x in range(100):
    t.pencolor(colors[x % 4])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(your_name, font = ("Monaco",int( (x + 4) / 4), "bold") ) 
    t.left(92)
