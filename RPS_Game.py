# importamos las distintas librerias que vamos a necesitar para realizar el juego la libreria de os
# fue un intento de conseguir un clear output, pero me lo hizo mejor la otra libreria.

import random
import os

import sys
#from IPython.core.display import clear_output
#!pip install ipython
import IPython
from IPython.display import clear_output
import time


# Definimos las posibles elecciones, tanto para el oredenador como para el jugador

gestures = ['rock', 'paper', 'scissors']


# función para que el jugador pueda seleccionar el número de rondas que quiere jugar contra la máquina. He restringido
# la posibilidad a 7 máximo porque me parecen más que suficientes.

def numero_rondas():
    
    """
    Ask user for a number between 3, 5 or 7.
    
    Returns:
        int: the selected number
    """
    
    while True:
        
        n_rondas = input('Selecciona el número de rondas que quieres jugar. 3 - 5 - 7: ')
        
        if n_rondas.isnumeric():
            n_rondas = int(n_rondas)
            
            if n_rondas == 3 or n_rondas == 5 or n_rondas == 7:
                return n_rondas
            
            else:
                clear_output(wait = True)
                os.system ("clear")
                os.system ("cls")
                print ('Recuerda que tienes que elegir entre los valores dados')
        
        else:
            clear_output(wait = True)
            os.system ("clear")
            os.system ("cls")
            print ('Introduce un número por favor')
            

def jugada_ordenador():
    
    """
    Choose one of the three gestures options randomly
    
    Returns:
        string: cpu 'choice'
    """
    return (gestures[random.randint(0,2)])

def jugada_player():
    
    """
    Ask user to choose the gesture to play
    
    Returns:
        string: choosen gesture
    """
    
    respuesta = ''                          
    while True:
        respuesta = input('Introduce una de estas tres opciones: rock✊,  paper🖐,  scissors✌: ')
        if respuesta not in gestures:
            clear_output()
            os.system ("clear")
            os.system ("cls")
            pass
        else:
            return respuesta

def definir_ganador(ordenador, jugador_01):
    
    """
    Evaluate the winner in the rock, paper scissors game between two player
    Args:
        string: cpu's gesture
        string: player's gesture
    Returns:
        int: 0 = tie, 1 = cpu win, 2 player win
    """
    
    if jugador_01 == ordenador:
        return 0
    
    elif ordenador == 'scissors' and jugador_01 == 'paper' or ordenador == 'paper' and jugador_01 == 'rock' or ordenador == 'rock' and jugador_01 == 'scissors':
        return 1
    
    elif jugador_01 == 'scissors' and ordenador == 'paper' or jugador_01 == 'paper' and ordenador == 'rock' or jugador_01 == 'rock' and ordenador == 'scissors':
        return 2


def victoria_de (ordenador, jugador_01, numero):
    
    """
    Based in the number return of definir_ganador function, print both gesture and print round resolution,
    add +1 score properly i needed
    
    Args:
        string: cpu's gesture
        string: player's gesture
        int: definir_ganador's number return
    
    Returns:
        None
    """
    
    global cpu_score
    global player_score
    puntuaciones = [None, cpu_score , player_score]
    
    ganadores = ['empate', 'el Ordenador', 'el Usuario']
    
    
    #print (f'La jugada del ordenador ha sido {ordenador}, por el contrario el usuario ha escogido {jugador_01}')
    
    if numero == 0:
        pass
        #print ('Esta ronda ha sido empate')
        
    else:
        #print (f'El ganador de esta ronda ha sido {ganadores[numero]}')
        if numero == 1:
            cpu_score +=1
        elif numero == 2:
            player_score += 1


# podría meter toda esta fantasía en la función anterior, pero como son pruebas y me parece que va a quedar muy loco,
# prefiero hacerlo en una función separada 😂

def cuenta_atras(ordenador, jugador_01, ganador):
    
    """
    Based in the number return of definir_ganador function, print both gesture and print round resolution
    
    Args:
        string: cpu's gesture
        string: player's gesture
        int: definir_ganador's number return
    
    Returns:
        Epilepsia
    """
    
    pantallazos = ['HA HABIDO UN EMPATE!!!!', 'HA GANADO EL ORDENADOR!!!!', 'EL JUGADOR ES EL QUE GANA!!!!']
    
    # mira mamá estoy usando un diccionario por primera vez!!!!!!!
    dict_emojis = {'paper' : '🖐', 'scissors' : '✌', 'rock' : '✊'}
    
    clear_output()
    os.system ("clear")
    os.system ("cls")
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''



             ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪           




''')
    time.sleep(0.15)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''


          ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
                     3            
          ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪  


''')
    time.sleep(0.22)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''

     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
     ------------🧠-🧠-🧠--------------
                     3            
     ------------------------------------
     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    

''')
    time.sleep(0.3)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------

                     3
             
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    time.sleep(0.8)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''



             ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪           




''')
    time.sleep(0.15)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''


          ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
                     2            
          ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪  


''')
    time.sleep(0.22)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''

     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
     ------------🧠-🧠-🧠--------------
                     2            
     ------------------------------------
     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    

''')
    time.sleep(0.3)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------

                     2
             
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    time.sleep(0.8)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''



             ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪           




''')
    time.sleep(0.2)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''


          ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
                     1            
          ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪  


''')
    time.sleep(0.36)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''

     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫
     ------------🧠-🧠-🧠--------------
                     1            
     ------------------------------------
     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    

''')
    time.sleep(0.4)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------

                     1
             
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    
    time.sleep(0.8)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------

                     
             
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    time.sleep(0.2)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------
''')
    print(
f'                                      LA JUGADA')

    print('\n')
    print(
f'{dict_emojis[jugador_01]}')

    print(
'''
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    
    time.sleep(0.2)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------
''')
    print(
f'                             LA JUGADA DE LA MÁ')

    print('\n')
    print(
f'HA SIDO {dict_emojis[jugador_01]}')

    print(
'''
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    
    time.sleep(0.2)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------
''')
    print(
f'                LA JUGADA DE LA MÁQUINA HA S')

    print('\n')
    print(
f' DEL JUGADOR HA SIDO {dict_emojis[jugador_01]}')

    print(
'''
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    
    time.sleep(0.2)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------
''')
    print(
f'    LA JUGADA DE LA MÁQUINA HA SIDO {dict_emojis[ordenador]}')
    print('\n')
    print(
f'     LA JUGADA DEL JUGADOR HA SIDO {dict_emojis[jugador_01]}')

    print(
'''
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    
    time.sleep(1.5)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------

               EL GANADOR ES...
             
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    
    time.sleep(1.2)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------
''')
    print('\n')
    print(f'          {pantallazos[ganador]}')
    print('\n')
    print(
'''
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')


# me he creado una función para pedir un número, me vale para utilizarla recorriendo menús

def introduce_numero ():
    
    """
    Ask user for a number
    
    Returns:
        int: selected number
    """
    
    numero = ''
    
    while True:
        numero = input('Por favor introduce la opción deseada: ')
        if numero.isnumeric():
            numero = int(numero)
            return numero
            
        else:
            print ('debes introducir un valor adecuado')
        
        
def pantalla_final(cpu_score, player_score, rounds_to_win):
    
    """
    Print the final result for the current game
    
    Args:
        int: Number of cpu's wins
        int: Number of usser's wins
        int: Number of wins needed to win the game
    
    Returns:
        more epilepsy
    """
    
    print('''



             ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪           




''')
    time.sleep(0.15)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''


          ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
                     3            
          ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪  


''')
    time.sleep(0.22)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''

     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
     ------------🧠-🧠-🧠--------------
                     3            
     ------------------------------------
     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    

''')
    time.sleep(0.3)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------

                     3
             
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    time.sleep(0.8)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''



             ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪           




''')
    time.sleep(0.15)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''


          ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
                     2            
          ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪  


''')
    time.sleep(0.22)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''

     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
     ------------🧠-🧠-🧠--------------
                     2            
     ------------------------------------
     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    

''')
    time.sleep(0.3)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------

                     2
             
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    time.sleep(0.8)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''



             ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪           




''')
    time.sleep(0.2)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''


          ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
                     1            
          ▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪  


''')
    time.sleep(0.36)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''

     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
     ------------🧠-🧠-🧠--------------
                     1            
     ------------------------------------
     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    

''')
    time.sleep(0.4)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------

                     1
             
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    
    time.sleep(0.8)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------

                     
             
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    time.sleep(0.2)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------

        EL RESULTADO FINAL HA SIDO...

---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    time.sleep(2)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")
    print('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠-------------------

''')
    
    if cpu_score == rounds_to_win:
        print (' EL GANADOR TOTAL HA SIDO EL ORDENADOR!!!! ')
        
    elif player_score == rounds_to_win:
        print ('  EL GANADOR TOTAL HA SIDO EL USUARIO!!!! ')
        
    else:
        print( 'HA SIDO EMPATE AL FINAL DE TODAS LAS RONDAS. ')
    
    
    
    
    print('''

---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')
    time.sleep(4)
    clear_output(wait = True)
    os.system ("clear")
    os.system ("cls")


# en este bloque vamos a condensar el flujo del juego, me copiaré aquí algunas de las variables
# que necesito por claridad visual y para que estén inicializadas correctamente cuando empiece el juego, evitando errores
# a causa de pruebas anteriores.

n_rounds = 3
rounds_to_win = int(n_rounds / 2) +1
cpu_score = 0
player_score = 0

# necesito crearme unas variables para almacenar las jugadas de los jugadores en cada ronda y el resultado de las mismas
ordenador = ''
jugador_01 = ''
ganador = 0

# Nos hacemos un menú para que el usuario sepa que puede empezar el juego. No sé si poner un menú más con opciones y que
# ahí el jugador defina el número de rondas. Ponemos la opción salir a un número más que las otras, para que no se de sin
# querer a salir cuando quieres entrar en opciones

exit = False
opcion_menu = 0
turnos = 0

while not exit:

    print ('''

▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠------------------
---------------------------------------------

 1.- Jugar a piedra ✊, papel 🖐 o tijera ✌.
 
 2.- Opciones (selección Nº de rondas)
 
 4.- Salir del programa.

---------------------------------------------
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
'''
f'RONDAS: {n_rounds}'
          )

    # esta opción es para que en caso de que el usuario haya introducido un valor distinto a los del menú, llamarle la atención a ello
    #if opcion_menu != 0:
    #    print ('Tienes que introducir una opción válida') 
        
    opcion_menu = introduce_numero()

    if opcion_menu == 4:
        exit = True
    
    elif opcion_menu == 2:
        n_rounds = numero_rondas()
        rounds_to_win = int(n_rounds / 2) +1
        clear_output()
        os.system ("clear")
        os.system ("cls")

    elif opcion_menu == 1:
        
        turnos = 0
        cpu_score = 0
        player_score = 0
        clear_output()
        os.system ("clear")
        os.system ("cls")
        print ('''
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠------------------

             ¡¡¡¡A JUGAR!!!!
             
---------------------------------------------
▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪    
''')

        # declaramos un bucle que se repetirá hasta que se juegue el número de turnos seleccionados
        # o hasta que un jugador alcance las victorias necesarias
        while turnos < n_rounds and cpu_score < rounds_to_win and player_score < rounds_to_win:
            
            #primero veremos cual es la jugada del ordenador
            ordenador = jugada_ordenador()
            
            # preguntamos al jugador por su opción
            jugador_01 = jugada_player()
            
            # comparamos los distintos resultados y lo guardamos en la variable ganador
            ganador = definir_ganador(ordenador, jugador_01)
            print (ganador)
            
            # imprimimos por pantalla el resultado del ganador de esta ronda
            victoria_de(ordenador, jugador_01, ganador)
            cuenta_atras(ordenador, jugador_01, ganador)
            
            turnos += 1
            
            
            #print (turnos, cpu_score, player_score, n_rounds, rounds_to_win)
            
        time.sleep(3)
        clear_output(wait = True)
        os.system ("clear")
        os.system ("cls")
        
        # pasamos por pantalla el resultado final una vez sale del bucle y salimos del while
        pantalla_final(cpu_score, player_score, rounds_to_win)
        #lear_output(wait = True)

    else:
        clear_output()
        os.system ("clear")
        os.system ("cls")

print ('HASTA PRONTO!!!!')
time.sleep(2)