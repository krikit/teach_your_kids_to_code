import turtle
t = turtle.Pen()
number = int(turtle. numinput("Number of sudes or circles",
                              "How many sides or circles in your shape?", 6))
shape = turtle.textinput("Witch shape do you want?",
                         "Enter 'p' for polygon or 'r' for rosette:")
for x in range(number):
    if shape == 'r':
        t.circle(100)
    else:
        t.forward(150)
    t.left(360/number)
