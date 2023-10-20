import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.speed(0)

'''
#square
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)    

#star
for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(200)
'''

#polygon
num_sides = 6
angle = 360.0 / num_sides
side_length = 100

for i in range(num_sides):
    turtle_instance.left(angle)
    turtle_instance.forward(side_length)

turtle.done()