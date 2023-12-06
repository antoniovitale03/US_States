from turtle import Turtle, Screen
import pandas
from Scoreboard import Scoreboard
scoreboard = Scoreboard
turtle = Turtle()
screen = Screen()
US_image = Turtle()
state = Turtle()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
US_image.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
def quiz():
    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                            prompt="What's another state name?").title()
        if answer_state.title() == "Exit":
            missing_states = [state for state in all_states if state not in guessed_states]
            my_data = pandas.DataFrame(missing_states)
            my_data.to_csv("states_to_learn.csv")
            break
        elif answer_state in all_states:
            state.hideturtle()
            state.penup()
            state_data = data[data.state == answer_state]
            x = int(state_data.x)
            y = int(state_data.y)
            state.goto(x, y)
            state.write(answer_state)
            guessed_states.append(answer_state)
        else:
            quiz()

quiz()







