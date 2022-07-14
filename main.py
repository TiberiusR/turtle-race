from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="What color do you think will win the race?").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


y_axis = -100
for turtle_index in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_axis)
    y_axis += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for t in screen.turtles():
        if t.xcor() > 230:
            is_race_on = False
            if t.pencolor() == user_bet:
                print(f"You've won! The {t.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {t.pencolor()} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        t.fd(rand_distance)

screen.exitonclick()
