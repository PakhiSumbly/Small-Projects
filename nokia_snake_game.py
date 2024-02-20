#Implementation of the simplest version of the 90's Nokia phone's Snake game using Python programming language (created by Pakhi Sumbly).

import turtle
import random
import time

# Constants
GRID_SIZE = 20
DELAY = 0.1    #DELAY is used to set the speed of the snake to fast or slow

# Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=400, height=400)
screen.tracer(0)  # To turn off automatic screen updates

# Snake
snake = []
for i in range(5 ,0,-1):         
    segment = turtle.Turtle()
    segment.shape("square")
    segment.color("white")
    segment.penup()
    segment.goto(-i * GRID_SIZE, -GRID_SIZE*2)  # Modified starting position of snake
    snake.append(segment)

head = snake[0]
head.direction = RIGHT


# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(random.randint(-9, 9) * GRID_SIZE, random.randint(-9, 9) * GRID_SIZE)

# Functions
def go_up():
    if head.direction != DOWN:
        head.direction = UP

def go_down():
    if head.direction != UP:
        head.direction = DOWN

def go_left():
    if head.direction != RIGHT:
        head.direction = LEFT

def go_right():
    if head.direction != LEFT:
        head.direction = RIGHT

def move():
    x = head.xcor()
    y = head.ycor()

     #To insert a new segment at the beginning of the snake
    new_segment = turtle.Turtle()
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(x, y)
    snake.insert(0, new_segment)

    # To check for collision with food
    if head.distance(food) < GRID_SIZE:
        food.goto(random.randint(-9, 9) * GRID_SIZE, random.randint(-9, 9) * GRID_SIZE)

        # To create a new segment and append it to the snake
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        snake.append(new_segment)
        

    # To move the head and update the snake
    if len(snake) > 1:
        for i in range(len(snake) - 1, 0, -1):
            x = snake[i - 1].xcor()
            y = snake[i - 1].ycor()
            snake[i].goto(x, y)

        # To move the first segment to the head position
        snake[0].goto(head.xcor(), head.ycor())

        # To remove the last segment if the snake has grown
        if len(snake) > 1:
            snake[-1].goto(1000, 1000)  # To move the last segment out of the screen
            snake.pop()  

   # Move the head
    x = head.xcor()
    y = head.ycor()

        
    if head.direction == UP:
        y += GRID_SIZE
    elif head.direction == DOWN:
        y -= GRID_SIZE
    elif head.direction == LEFT:
        x -= GRID_SIZE
    elif head.direction == RIGHT:
        x += GRID_SIZE

    head.setx(x)
    head.sety(y)

    
# Keyboard bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the head and update the snake
    move()

    # Check for collision with walls or self
    if (
        head.xcor() > 190
        or head.xcor() < -190
        or head.ycor() > 190
        or head.ycor() < -190
        or any(segment.distance(head) < GRID_SIZE/2 for segment in snake[1:])
    ):
        head.goto(-175,-175)
        head.direction = RIGHT

        # Reset snake positions
        for i, segment in enumerate(snake):
            segment.goto(-175, -175)  # Reset the position of each segment

    time.sleep(DELAY)
