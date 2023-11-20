#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


# write 'hello world' to the console
print('hello world')

import random

validOptions = ['rock', 'paper', 'scissors'];
conversion ={'rock':'r','paper':'p','scissors': 't'};
reverseConversion ={'r': 'rock','p': 'paper','t': 'scissors'};

def play():
    user = input("¿Qué eliges? 'rock', 'paper', 'scissors'\n").lower();
    while user not in validOptions:
        user = input("Opcion no válida\n¿Qué eliges? 'rock', 'paper', 'scissors'\n").lower();
    user=conversion[user];

    computer = random.choice(['r', 'p', 't'])

    if user == computer:
        return (0, user, computer)

    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 't') or (player == 't' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True
    return False

def print_result(result, user, computer):
    if result == 0:
        print(f'Empate. Elegiste {reverseConversion[user]}, la computadora eligió {reverseConversion[computer]}')
    elif result == 1:
        print(f'¡Ganaste! Elegiste {reverseConversion[user]}, la computadora eligió {reverseConversion[computer]}')
    else:
        print(f'Perdiste. Elegiste {reverseConversion[user]}, la computadora eligió {reverseConversion[computer]}')

def main():
    marcador = 0;
    ganadas = 0;
    partidas = 0;
    play_again = True
    while play_again:
        result, user, computer = play();
        print_result(result, user, computer);
        marcador += result;
        if result > 0: ganadas += 1;
        partidas += 1;
        user = input("¿Quieres jugar de nuevo? Presiona 'y' para sí, 'n' para no\n").lower();
        while user != 'y' and user != 'n':
            user = input("Opción no válida\n¿Quieres jugar de nuevo? Presiona 'y' para sí, 'n' para no\n").lower();
        if user == 'y': play_again = True;
        else: play_again = False;

    print(f'Tu puntuacion es {marcador}\nHas ganado {ganadas} veces de {partidas} partidas\n¡Gracias por jugar!')

if __name__ == '__main__':
    main()