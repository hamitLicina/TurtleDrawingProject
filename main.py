import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor('green')
drawing_board.title('Turtle Drawing')
turtle_instance = turtle.Turtle()

turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)

# square
for i in range(4):
    turtle_instance.forward(200)
    turtle_instance.right(90)

# star
for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(300)

# polygon
turtle_instance_second =turtle.Turtle()
num_sides = 6
angle = 360.0/num_sides
side_length = 200

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)

turtle.done()