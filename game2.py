# El codigo funciona bien pero tengo dudas sobre variables dentro y fuera de las funciones.
# A veces calculos que hago dentro de funciones no actualizan la variable fuera de la funcion.
# Incluso si se las paso como argumentos de la funcion.
# Quise intentar hacer el calculo de quien gana sin tantos IF's..para ello utilize una matriz con todos los resultados posibles


import random

gestures = ["rock", "paper", "scissors", "lizard", "spock"]
cpu_score = 0
player_score = 0
choice_dictionary = {"rock": 0, "paper": 1,
                     "scissors": 2, "lizard": 3, "spock": 4}

result_matrix = [[0, 1, 2, 2, 1],
                 [2, 0, 1, 1, 2],
                 [2, 1, 0, 2, 1],
                 [1, 2, 1, 0, 2],
                 [2, 1, 2, 1, 0]]


def how_many_rounds():
    while True:
        try:
            how_many_rounds_input = int(
                input("How many rounds to win the game.  Please enter an odd number: "))
            if (how_many_rounds_input % 2 != 0):
                return how_many_rounds_input
        except:
            print("Please enter only numbers! \n")


def cpu_throw(gestures):
    computer_choice_index = choice_dictionary.get(random.choice(gestures))
    return computer_choice_index


def player_throw():
    while True:
        choice_input = input(
            "Please type your choice: 'rock', 'paper','scissors', 'lizard', 'spock' \n")
        player_choice_index = choice_dictionary.get(choice_input, 5)
        break
    return player_choice_index


def calculate_round(player_play, cpu_play):
    result_index = result_matrix[player_play][cpu_play]
    return result_index


def game_round():
    print(f"Current Score is: You: {player_score} - {cpu_score} \n")
    player_play = player_throw()
    cpu_play = cpu_throw(gestures)
    print(f"Computer plays {gestures[cpu_play]}")
    winner = calculate_round(player_play, cpu_play)
    message_list = ["That ended in a TIE", "Sorry, you lost!", "You WIN!!!!"]
    print(message_list[winner])
    return winner


print("IronHack Rock Paper Scissors Lizard Spock: \n")
rounds_to_win = how_many_rounds()
print(f"First to win {rounds_to_win} rounds wins. Good Luck! \n")

while player_score != rounds_to_win or cpu_score != rounds_to_win:
    result = game_round()
    if result == 1:
        cpu_score += 1
    if result == 2:
        player_score += 1
    if player_score == rounds_to_win:
        print(f"Current Score is: You: {player_score} - {cpu_score} \n")
        print(
            f"YOU HAVE WON ALL {rounds_to_win} ROUNDS....you are the CHAMPION!")
        break
    if cpu_score == rounds_to_win:
        print(f"Current Score is: You: {player_score} - {cpu_score} \n")

        print(
            f"Sorry the computer was first to win {rounds_to_win} rounds..try again")
        break
