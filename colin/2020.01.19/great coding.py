# coding.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(10000000)
colors = ["red" , "yellow"]
for x in range(100):
    t.pencolor( colors[ x % 2] )
    t.forward(2*x)
    t.right(26)
