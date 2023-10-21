import turtle
import random

# method to action
def fly_turtle(x, y):
    # some motion
    turtle.teleport(random.randint(-350,350),random.randint(-350,350))


# turtle speed to slowest
turtle.speed(1)

# motion
turtle.fd(100)

# allow user to click
# for some action
turtle.onclick(fly_turtle)

turtle.mainloop()