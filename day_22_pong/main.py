import turtle as t
from ball import Ball
import time
from paddle import Paddle
from scoreboard import Scoreboard

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200
RIGHT_PADDLE_X_POS = 550
LEFT_PADDLE_X_POS = -550
PADDLE_SIZE = 5

ball = Ball()
right_paddle = Paddle(RIGHT_PADDLE_X_POS)
left_paddle = Paddle(LEFT_PADDLE_X_POS)

player_one_scoreboard = Scoreboard(1)
player_two_scoreboard = Scoreboard(2)

screen = t.Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.tracer(0)
screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)

    ball.move() 

    for paddle_segment in right_paddle.paddle_segments:
        if ball.distance(paddle_segment) < 15:
            print("MAIN: ball within 15 of right paddle.")
            ball.paddle_bounce()
            break

    for paddle_segment in left_paddle.paddle_segments:
        if ball.distance(paddle_segment) < 15:
            print("MAIN: ball within 15 of right paddle.")
            ball.paddle_bounce()
            break

    result = ball.out_of_bounds()
    if result == 1:
        # print("MAIN: ball.out_of_bounds returned 1")
        player_one_scoreboard.increase_score()
    elif result == 2:
        # print("MAIN: ball.out_of_bounds returned 2")
        player_two_scoreboard.increase_score()      
    




screen.exitonclick()