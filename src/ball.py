import turtle
import time

screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("Bouncy Ball!")
screen.bgcolor("#32CD32")
screen.tracer(0)

turtle.getcanvas().config(bd=0, highlightthickness=0) # Remove ugly borders on window

ball = turtle.Turtle()
ball.fillcolor("white")
ball.color("white")
ball.shape("circle")
ball.shapesize(screen.window_width() / 300)
ball.penup()

screen.listen()
screen.onkey(lambda: ball.goto(0, 0), "w")

dx, dy = 2, 2

while True:
    ball.goto(ball.xcor() + dx, ball.ycor() + dy)

    if abs(ball.xcor()) + 15 >= screen.window_width() / 2: # Calculating screen width and height on the fly allows for resizing to work flawlessly
        dx *= -1
    if abs(ball.ycor()) + 15 >= screen.window_height() / 2:
        dy *= -1
    
    screen.update()
    time.sleep(0.01)