from turtle import Turtle
import random

# food class renders itself as small blue circle and everytime the snake touches the food, the food is going to go
# to a new random location

class Food(Turtle):
    # inheritance

    def __init__(self):
        super(Food, self).__init__()
        # instead of creating a food object here like this:
        # self.food = Turtle()
        self.shape("turtle")
        # self.shape("turtle")
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # generally it is 20 by 20 but now we are making it 10 by 10
        self.color("green")
        self.speed("fastest")
        random_x = random.randint(-280, 280)  # cuz we dont want the snake to die at the wall
        random_y = random.randint(-280, 280)  # cuz we dont want the snake to die at the wall
        self.goto(random_x, random_y)

        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  # cuz we dont want the snake to die at the wall
        random_y = random.randint(-280, 280)  # cuz we dont want the snake to die at the wall
        self.goto(random_x, random_y)



