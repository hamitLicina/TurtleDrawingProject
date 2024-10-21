import turtle


turtle_drawing_board = turtle.Screen()
turtle_drawing_board.bgcolor("lightgreen")
turtle_drawing_board.title("Turtle Drawing Board")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shirinking(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

shirinking(150)
shirinking(130)
shirinking(110)
shirinking(90)
shirinking(70)
shirinking(50)
shirinking(30)
shirinking(10)

turtle.done()