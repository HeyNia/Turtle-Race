from turtle import Turtle, Screen
from tkinter import messagebox
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
START_X = -230
FINISH_X = 230

COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]
Y_POSITIONS = [-70, -40, -10, 20, 50, 80]

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle Race")
screen.colormode(255)
screen.bgcolor((255, 230, 204))


def create_turtles():
    turtles = []

    for color, y_position in zip(COLORS, Y_POSITIONS):
        turtle = Turtle(shape="turtle")
        turtle.speed("fast")
        turtle.penup()
        turtle.color(color)
        turtle.goto(START_X, y_position)
        turtles.append(turtle)

    return turtles


user_bet = screen.textinput(
    title="Make Your Bet",
    prompt=f"Which turtle will win?\nChoose from: {', '.join(COLORS)}"
)

user_bet = user_bet.strip().lower() if user_bet else ""

if user_bet not in COLORS:
    messagebox.showwarning(
        "Invalid Bet",
        "Please choose one of the available turtle colors."
    )
else:
    all_turtles = create_turtles()
    race_on = True

    while race_on:
        for turtle in all_turtles:
            turtle.forward(random.randint(0, 10))

            if turtle.xcor() >= FINISH_X:
                race_on = False
                winner = turtle.pencolor()

                if winner == user_bet:
                    message = f"You win! The {winner} turtle won!"
                else:
                    message = f"You lose! The {winner} turtle won!"

                messagebox.showinfo("Race Result", message)
                break

screen.exitonclick()