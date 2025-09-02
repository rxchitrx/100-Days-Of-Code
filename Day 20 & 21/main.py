from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

blocks = []

for position in starting_positions:
    new_block = Turtle("square")
    new_block.color("white")
    new_block.penup()
    new_block.goto(position)
    blocks.append(new_block)




game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for block_num in range (len(blocks) - 1, 0, -1):
        new_x = blocks[block_num - 1].xcor()
        new_y = blocks[block_num - 1].ycor()
        blocks[block_num].goto(new_x, new_y)

    blocks[0].forward(20)
    blocks[0].left(90)

screen.exitonclick()