#simple snake game in using turtle
#game by WhiteDevil

import turtle
import time
import random


delay = 0.1

#score
score = 0
high_score = 0

#setup screen
wn = turtle.Screen()
wn.title("snake game by WhiteDevil")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

# snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0   High Score: 0 ", align="center",font=("Courier",20,"normal"))


#functions
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left" :
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

#keyboard winding
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#main loop
while True:
    wn.update()

    #check for collision with border
    if snake.xcor()>290 or snake.xcor() < -290 or snake.ycor() >290 or snake.ycor()<-290 :
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segments
        segments.clear()

        #reset score
        score = 0

        # reset delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))

    #check for collision with food
    if snake.distance(food) < 20:
        #move a food
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)

        #snake body or segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001

        #score increase
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier",20,"normal"))

    #move the end segments
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    move()
    #check for body collision
    for segment in segments :
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"

            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segments
            segments.clear()

            # reset score
            score = 0

            #reset delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",font=("Courier", 20, "normal"))


    time.sleep(delay)

wn.mainloop()
