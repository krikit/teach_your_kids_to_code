#동호#천재#동호천재#클래스#동호와우.py - a spiral of rosettes!
import turtle
t = turtle.Pen()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
sides = int(turtle.numinput("Number of sides",
                             "How many sides in your spiral of rosettes? (2-6)", 4,2,6))
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
for m in range(100):
    t.forward(m*4)
    position = t.position() 
    heading = t.heading()   
    print(position, heading)
    for n in range(sides):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.circle(m/4)
        t.right(360/sides - 2)
        t.penup()
    t.setpos(position)  
    t.setheading(heading)
    t.left(360/sides + 2)
