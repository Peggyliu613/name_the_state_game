from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.title("Name The State Game")
screen.setup(725, 491)


pen = Turtle()
pen.penup()
pen.hideturtle()


data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()


player_ans_list = []
player_missing_state_list = []
while len(player_ans_list) < 50:
    player_ans = screen.textinput("Guess the state", "What is another state's name?").title()
    if player_ans == "Exit":
        break
    if player_ans in state_list and player_ans not in player_ans_list:
        pen.goto(int(data[data["state"] == player_ans].x), int(data[data["state"] == player_ans].y))
        pen.write(player_ans)
        player_ans_list.append(player_ans)

for state in state_list:
    if state not in player_ans_list:
        player_missing_state_list.append(state)

states_to_learn = {
    "states_you_missed": player_missing_state_list
}
pandas.DataFrame(states_to_learn).to_csv("states_to_learn")


screen.exitonclick()
