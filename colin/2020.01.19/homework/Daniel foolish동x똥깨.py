# coding.py
import turtle
sides = input("Enter number of sides between 2 and 6:")
sides = int(sides)
print(sides)
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["yellow", "red", "blue", "green", "orange", "pink"]
for x in range(100):
    t.pencolor( colors[x%sides] )
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/90)
 
