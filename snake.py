# everything related to the appearance and  behavior of the snake are all captured in the snake class


from turtle import Turtle, Screen

STARTING_CONSTANTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # def create_snake(self):
    #
    #     for position in STARTING_CONSTANTS:
    #         new_segment = Turtle("square")
    #         new_segment.color("white")
    #         new_segment.penup()
    #         new_segment.goto(position)
    #         self.segments.append(new_segment)

    def create_snake(self):

        for position in STARTING_CONSTANTS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("circle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # we are adding this code for the high score feature
    def reset(self):
        # we are clearing all the parts of the snake, but we cant completely reset it, it will still appear on the board,
        # and since our board is 600 by 600 we need to shift the snake segments to a location that insnt visible
        for seg in self.segments:
            seg.goto(1000, 1000)
        #     this will make sure that it will disappear off the screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    #     we are repeating the entire code that is in init cuz we are initialising again

    def extend(self):
        # add a new segment as soon as it touches the food
        self.add_segment(self.segments[-1].position())
        # if we have a list of 1, 2, 3 then -1 position will be 3

    def move(self):

        # segment1 = Turtle(shape="square")
        # segment1.color("white")
        #
        # segment2 = Turtle(shape="square")
        # segment2.color("white")
        # segment2.goto(-20, 0)
        #
        # segment3 = Turtle(shape="square")
        # segment3.color("white")
        # segment2.goto(-40, 0)

        # for seg in segments:
        #     seg.forward(20)
        #     time.sleep(1)

        # this does the job step by step and its problamatic for the snake when its going to take a turn so we use
        # the below code

        # for seg_num in range(start=2, stop=0, step=-1):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # self.segments[0].forward(MOVE_DIST)
        # but the 1st segment wont be moving so to move that forward, this step is used
        self.head.forward(MOVE_DIST)

        """
        This is the code that will get the snake to automatically move forwards and wont cause any error while turning 
        too cuz all the segments are following their predecessor
        """

    # def up(self):
    #     self.segments[0].setheading(UP)
    #
    # def down(self):
    #     self.segments[0].setheading(DOWN)
    #
    # def right(self):
    #     self.segments[0].setheading(RIGHT)
    #
    # def left(self):
    #     self.segments[0].setheading(LEFT)

    # but when this is the case it can turn around and go back too by changing its position of its head but that
    # shouldn't be the case so we change the code a bit

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
