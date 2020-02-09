#동균천재
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
family = []
name = turtle.textinput("my family",
                        "enter a name, or just hit [ENTER] to end:")
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
while name != "":
    family.append(name)
    name = turtle.textinput("my family",
                        "enter a name, or just hit [ENTER] to end:")
for x in range (100):
    t.penup()
    t.forward(x*4)
    position = t.position()
    heading = t.heading()
    for y in range (len(family)):
        t.pencolor(colors[y%len(family)])
        t.penup()
        t.forward(x/2)
        t.write(family[y%len(family)], font = ("Arial", int((x+4)/4), "bold") )
        t.pendown()
        t.right(360/len(family) + 2)
    t.setpos(position)      
    t.setheading(heading)
    t.left(360/len(family) + 2)
    
    
