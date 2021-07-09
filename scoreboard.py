from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Courier", 26, "normal")

class Score(Turtle):

    # def __init__(self):
    #     super().__init__()
    #     self.score = 0
    #     self.penup()
    #     self.color("white")
    #     self.goto(0, 270)
    #
    #     self.write(f"Score : {self.score} ", align="center", font=("Arial", 22, "normal"))
    #     but when we do this,the turtle is present there somewhere in the middle, so we want that to disappear sorted()
    #
    #     self.hideturtle()
    #
    # def increase_score(self):
    #     # but when we do this, the score just gets overwritten so we need to clear before writing again
    #     self.score += 1
    #     self.write(f"Score : {self.score} ", align="center", font=("Arial", 22, "normal"))

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        # we wont be using this line and we will take input from the data.txt file itself
        # data.txt - this file is created so that we get to know the high score and store it in a file
        with open("data.txt") as data:
            # we will use the with keyword so that we don't have to manage the closing of file, python will manage it
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)

        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score} ", align=ALIGNMENT, font=FONT)
        # but when we do this,the turtle is present there somewhere in the middle, so we want that to disappear sorted()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # commenting out these to make a few changes like, displaying the high score and still continuing with the game
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_score()

