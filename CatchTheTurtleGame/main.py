import time
import turtle
import random

drawing_board = turtle.Screen()
drawing_board.title("Catch The Turtle")
drawing_board.bgcolor("light blue")
turtle_instance = turtle.Turtle()
drawing_board.screensize(400,400)
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.shapesize(3)
drawing_board.listen()
turtle_instance.speed(0)

def fly_turtle(x,y):
    turtle_instance.teleport(random.randint(-350,350), random.randint(-350,350))

while(1):

    turtle_instance.onclick(fly_turtle)

