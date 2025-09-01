import turtle as t
import random

timmy = t.Turtle()
timmy.speed("fastest")
t.colormode(255)

color_list = [(228, 227, 225), (227, 223, 226), (198, 173, 119), (214, 225, 218), (222, 224, 229), (162, 100, 54), (126, 35, 23), (185, 158, 50), (5, 55, 83), (51, 32, 28), (110, 68, 86),
              (116, 162, 176), (22, 120, 171), (76, 34, 43), (66, 154, 132), (83, 140, 64), (7, 65, 44), (184, 97, 79), (128, 37, 41), (204, 201, 147), (145, 178, 162), (174, 152, 157),
              (177, 201, 185), (219, 182, 168), (25, 80, 60)]


def horizontal_line():
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.fd(50)
        timmy.pendown()

def reset_pos_to_y():
        timmy.penup()
        timmy.goto(0, timmy.ycor() + 70)

for _ in range(10):
    horizontal_line()
    reset_pos_to_y()


screen = t.Screen()
screen.exitonclick()

