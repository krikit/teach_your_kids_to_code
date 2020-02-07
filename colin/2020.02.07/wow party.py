#coconut100.py
import turtle
t = turtle.Pen()
t.speed(0)
number_of_circles = int(turtle.numinput("Number input", "How many circles do you want"))
for x in range(number_of_circles):
    t.circle(100)
    t.left(360/number_of_circles)
