# import turtle
# import pandas as pd
# import os

# # Change directory to the script's location
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# # Load the screen and image
# screen = turtle.Screen()
# screen.title("US States Guessing Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

# # Load states data from CSV
# data = pd.read_csv("50_states.csv")
# all_states = data["state"].tolist()
# guessed_states = []

# # Game loop
# while len(guessed_states) < 50:
#     answer_state = screen.textinput(
#         title=f"{len(guessed_states)}/50 States Correct",
#         prompt="What's another state name?"
#     )
    
#     if answer_state is None:  # User clicked cancel
#         break
    
#     answer_state = answer_state.title()
    
#     if answer_state in all_states and answer_state not in guessed_states:
#         guessed_states.append(answer_state)
#         state_data = data[data["state"] == answer_state]
        
#         # Create turtle to write state name at coordinates
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         x = int(state_data.x.values[0])
#         y = int(state_data.y.values[0])
#         t.goto(x, y)
#         t.write(answer_state, font=("Arial", 10, "normal"))

# screen.exitonclick()

import turtle
import os
import pandas as pd

screen = turtle.Screen()
screen.title("US States Guessing Game")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?")
states_data = pd.read_csv("50_states.csv")
state_list = states_data["state"].tolist()

while(len(guessed_states) < 50):
    if answer_state is None:
        break
    if answer_state.lower() == "exit":
        break
    answer_state = answer_state.title()
    if answer_state in state_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        print(guessed_states)
        cords = states_data[states_data["state"] == answer_state][["x", "y"]].values[0]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(cords[0], cords[1])
        t.write(answer_state)

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?")

states_to_learn = [state for state in state_list if state not in guessed_states]
states_to_learn_df = pd.DataFrame(states_to_learn, columns=["state"])
states_to_learn_df.to_csv("states_to_learn.csv", index=False)