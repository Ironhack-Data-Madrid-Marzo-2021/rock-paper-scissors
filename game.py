import random

gestures = ["rock", "paper", "scissors"]
n_rounds = 7
rounds_to_win = 4
cpu_score = 0
player_score = 0
champion = 0


def cpu_throw(gestures):
    return random.choice(gestures)


def player_throw():
    while True:
        choice_input = input(
            "Please type your choice: 'rock', 'paper' or 'scissors ' \n")
        if choice_input == "rock" or choice_input == "paper" or choice_input == "scissors":
            break
    return choice_input


def calculate_round(player_play, cpu_play):
    if player_play == cpu_play:
        return 0
    elif player_play == "rock":
        if cpu_play == "scissors":
            return 2
        else:
            return 1
    elif player_play == "paper":
        if cpu_play == "rock":
            return 2
        else:
            return 1
    elif player_play == "scissors":
        if cpu_play == "paper":
            return 2
        else:
            return 1


def game_round():
    print(f"Current Score is: You: {player_score} - {cpu_score} \n")

    player_play = player_throw()
    cpu_play = cpu_throw(gestures)
    print(f"Computer plays {cpu_play}")
    winner = calculate_round(player_play, cpu_play)
    if winner == 0:
        print(f"That ended in a TIE")
    if winner == 1:
        print("Sorry, you lOST!")
    if winner == 2:
        print("You WIN!!!!!")
    return winner


print("IronHack Rock Paper Scissors: First to 4 WINS! \n")
while player_score != rounds_to_win or cpu_score != rounds_to_win:
    result = game_round()
    if result == 1:
        cpu_score += 1
    if result == 2:
        player_score += 1
    if player_score == rounds_to_win:
        print("YOU HAVE WON ALL 4 ROUNDS....CHAMPION!")
        break
    if cpu_score == rounds_to_win:
        print("Sorry the computer was fisrt to win 4..try again")
        break
