from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anish Is Cute")

screen.tracer(0)
# Turn turtle animation on/off and set delay for update drawings. If n is given, only each n-th regular screen update
# is really performed. (Can be used to accelerate the drawing of complex graphics.) When called without arguments,
# returns the currently stored value of n.

# turtle.update()
# Perform a TurtleScreen update. To be used when tracer is turned off.


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")  # Up -  the first letter of up has to be capital
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 18:
        # print("hola hola")
        food.refresh()
        snake.extend()

        # to update the score
        score.increase_score()

    # detect collision with a wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        print("hello world")
        score.game_over()

    # detect collision with tail
    # if the head collides with any segment of the snake/tail:
        # trigger game over
    # for segment in snake.segments:
    #     # lets just loop through all the segments in the snake.segments
    #     if snake.head.distance(segment) < 10:
    #         # if the head of the snake has a distance of less than 10 from any of the segments
    #         game_is_on = False
    #         score.game_over()
        # but in this if loop in the beginning the snake head will be close to the snake segments so we need to bypass
        # the head and this we will do by if and elif and passing the if statement

    # for segment in snake.segments:

    #     if segment == snake.head:
    #         pass

    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score.game_over()


    # using the concept of slicing
    for segment in snake.segments[1:]:
        # this will give evrything apart from the forst element which is what we want
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
