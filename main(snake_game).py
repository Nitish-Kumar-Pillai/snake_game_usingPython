from turtle import *
from snake import *
from food import *
from scoreboard import *
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increse_score()
    if snake.segment[0].xcor() > 280 or snake.segment[0].ycor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() < -280:
        gameIsOn = False
        scoreboard.game_over()

    for j in snake.segment:
        if j == snake.segment[0]:
            pass
        elif snake.segment[0].distance(j) < 5:
            gameIsOn = False
            scoreboard.game_over()




    snake.move()





screen.exitonclick()