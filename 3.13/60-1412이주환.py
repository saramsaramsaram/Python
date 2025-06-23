from turtle import *

d = 10
shape("turtle")
pensize(3)
down()

def turn_right():
    setheading(0)
    fd(d)
def turn_left():
    setheading(180)
    fd(d)
def turn_up():
    fd(d)
def turn_down():
    setheading(270)
    fd(d)

def black():
    clear()

def mouse():
    speed(0)
    pensize(2)
    onscreenclick(goto)
    onkeypress(black, "Escape")
    listen()


def keyboard():
    onkey(turn_right, "Right")
    onkey(turn_left, "Left")
    onkey(turn_up, "Up")
    onkey(turn_down, "Down")
    onkey(black, "Escape")
    listen()


keyboard()
mouse()