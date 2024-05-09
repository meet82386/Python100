import turtle as t
import pandas as pd

screen = t.Screen()
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")

data = pd.read_csv("50_states.csv")

all_states = set(data.state.values)
print(all_states)

state_set = set()
tim = t.Turtle()
tim.penup()
tim.hideturtle()

while len(state_set) != 50:
    input_state = str(t.textinput(f"{len(state_set)}/50 Guessed Correct", "Enter state name: "))
    result = data[data.state == input_state.title()]
    print(result)

    if input_state.title() == "Exit":
        missing_states = list(all_states.difference(state_set))
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if len(result) == 1:
        state_name = result["state"].values[0]
        x_cor = result["x"].values[0]
        y_cor = result["y"].values[0]

        if state_name not in state_set:
            state_set.add(state_name)
            tim.goto(x_cor, y_cor)
            tim.write(state_name, align="Center")

t.mainloop()

screen.exitonclick()
