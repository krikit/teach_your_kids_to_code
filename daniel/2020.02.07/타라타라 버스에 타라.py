simport turtle
t = turtle.Pen()
t.speed(0)
number_of_circles = int(turtle.numinput("Number", "How many circle do you want"))
for x in range(number_of_circles):
    t.circle(100)
    t.left(360/number_of_circles)
