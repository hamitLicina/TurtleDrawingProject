import turtle
from random import random

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("pink")
turtle_screen.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("red")
turtle.speed(0)
turtle_colors = ["blue", "purple", "green", "orange", "black", "yellow", "red"]

for i in range(17):
    turtle_instance.color(turtle_colors[i % 7])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)


turtle.done()