from turtle import Turtle, Screen
import random


is_race_on = False
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
y_positions = [-100, -50, 0, 50, 100, 150]

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bed", prompt= "Which turtle will win the race? [red, green, blue, yellow, orange, purple)")

all_turtles = []
for turtle_index in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(-230, y_positions[turtle_index])
    all_turtles.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            winning_turtle = t.pencolor()
            is_race_on = False
        t.forward(random.randint(0, 10))

if user_bet == winning_turtle:
    print(f"The winning turtle was {winning_turtle}. You won.")
else:
    print(f"The winning turtle was {winning_turtle}. You lost.")




screen.exitonclick()