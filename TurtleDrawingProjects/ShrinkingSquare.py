import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle Python")

turtle_incidance = turtle.Turtle()
turtle_incidance.color("blue")

def shrinkingSquare(size):

    for i in range(4):
        turtle_incidance.forward(size)
        turtle_incidance.left(90)
        size = size - 5

shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(110)
shrinkingSquare(90)
shrinkingSquare(70)
shrinkingSquare(50)
shrinkingSquare(30)
shrinkingSquare(10)

turtle.done()