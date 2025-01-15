from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []
pos = -100
for x in range(0,6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[x])
    turtle.goto(x=-230,y=pos)
    pos += 40
    all_turtles.append(turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The winning color is {winner}")
            else:
                print(f"You lost! The winning color was {winner}")
        
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
    










screen.exitonclick()
