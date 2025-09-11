import turtle
import pandas 


# Initial Setup.
screen = turtle.Screen()
screen.background = "blank_states_img.gif"
screen.title("US States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reading 50 States Data
all_states_data= pandas.read_csv("50_states.csv")
states = all_states_data.state
states_list = states.tolist()



# Collecting Input from User
correct_guesses = []
score = 0

for state in states_list:

    if score >= 1:
        answer_state = screen.textinput(title = f"{score}/50 states correct", prompt = "Whats another state name?")
    else:
        answer_state = screen.textinput(title = "Guess the State", prompt = "Guess a state")

    
    answer_state = answer_state.title()
    state_info = all_states_data[all_states_data.state == answer_state]

    if answer_state == "Exit":
        remaining_states = set(states_list) - set(sorted(correct_guesses))
        remaining_states = pandas.DataFrame(remaining_states)
        remaining_states.to_csv("remaining_states")
        break
        

    # 3. Write correct guesses onto the map.
    if answer_state in states_list:
        score += 1
        correct_guesses.append(answer_state)
        print("state found")
        t = turtle.Turtle()
        t.hideturtle()
        t.color("black")
        t.penup()
        t.speed("fastest")
        new_x = int(state_info.x)
        new_y = int(state_info.y)
        t.goto(new_x, new_y)
        t.write(answer_state)
