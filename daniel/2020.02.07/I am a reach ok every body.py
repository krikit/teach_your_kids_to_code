import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
t.width(2)
number_of_circles = int(turtle.numinput("Number", "How many circle do you want" , 6))
for x in range(number_of_circles):
    t.pencolor('red')
    t.circle(100)
    t.pencolor('yellow')
    t.circle(50)
    t.left(360/number_of_circles)