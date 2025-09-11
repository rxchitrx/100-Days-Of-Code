from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width = 800, height = 600)
screen.tracer(0)

paddle_right = Paddle((380, 0))
paddle_left = Paddle((-380, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

game_on = True
while game_on: 
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(paddle_right) < 40 and ball.xcor() > 240 or ball.distance(paddle_left) < 40 and ball.xcor() < -240:
        ball.paddle_bounce()
    
    if ball.xcor() > 400:
        scoreboard.increment_left()
        ball.reset_position()

    if ball.xcor() < -400:
        scoreboard.increment_right()
        ball.reset_position()
    


    
    
screen.exitonclick()












