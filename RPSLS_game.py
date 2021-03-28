#!/usr/bin/env python
# coding: utf-8

# # Rock, Paper, Scissors, Lizard & Spock
# ![](images/rpsls.jpg)
# 
# In this challenge, you need to improve the previous game by adding two new options. To know more about the rules of the improved version of rock, paper, scissors, check this [link](http://www.samkass.com/theories/RPSSL.html). 
# 
# In addition, you will also need to improve how the game interacts with the player: the number of rounds to play, which must be an odd number, will be requested to the user until a valid number is entered. Define a new function to make that request.
# 
# **Hint**: Try to reuse the code that you already coded in the previous challenge. If your code is efficient, this bonus will only consist of simple modifications to the original game.

# In[1]:


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


# In[15]:


#1.- Definimos las posibles elecciones, tanto para el oredenador como para el jugador

#añado a la lista las dus gestures que faltaban
gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']


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


# In[19]:


#2.- Definiremos la jugada del ordenador

def jugada_ordenador():
    
    """
    Choose one of the three gestures options randomly
    
    Returns:
        string: cpu 'choice' from a gesture's list
    """
    
    # Hago que el return amplie el rango para obetener todas las posibilidades
    return (gestures[random.randint(0,4)])


# In[17]:


#3.- Le preguntamos al jugador cual quiere que sea su jugada

def jugada_player():
    
    """
    Ask user to choose the gesture to play
    
    Returns:
        string: choosen gesture from a gesture's list
    """
    
    respuesta = ''                          
    while True:
        respuesta = input('Introduce una de estas opciones: rock✊,  paper🖐,  scissors✌, lizard🤏, spock🖖: ').lower()
        if respuesta not in gestures:
            #clear_output()
            #os.system ("clear")
            #os.system ("cls")
            pass
        else:
            return respuesta


# In[61]:


#4.- Evaluamos el ganador de una ronda (aqui meter lista (mejor un diccionario) de relaciones ganadoras) 
## he metido el diccionario dentro de esta función, pero me planteo la posibilidad de sacarlo

def definir_ganador(ordenador, jugador_01):
    
    """
    Evaluate the winner in the rock, paper scissors round between two player
    Args:
        string: cpu's gesture
        string: player's gesture
    Returns:
        int: 0 = tie, 1 = cpu win, 2 player win
    """
    relacion_ganadora= {
  
        'rock' : ['scissors', 'lizard'],
        'paper' : ['rock', 'spock'],
        'scissors' : ['paper', 'lizard'], 
        'lizard' : ['paper', 'spock'], 
        'spock' : ['rock', 'scissors']
    }
    
    if jugador_01 == ordenador:
        return 0
    
    elif ordenador == 'rock' and jugador_01 in relacion_ganadora[ordenador] or ordenador == 'paper' and jugador_01 in relacion_ganadora[ordenador] or ordenador == 'scissors' and jugador_01 in relacion_ganadora[ordenador] or ordenador == 'lizard' and jugador_01 in relacion_ganadora[ordenador] or ordenador == 'spock' and jugador_01 in relacion_ganadora[ordenador]:
        return 1
    
    elif jugador_01 == 'rock' and ordenador in relacion_ganadora[jugador_01]or jugador_01 == 'paper' and ordenador in relacion_ganadora[jugador_01] or jugador_01 == 'scissors' and ordenador in relacion_ganadora[jugador_01] or jugador_01 == 'lizard' and ordenador in relacion_ganadora[jugador_01] or jugador_01 == 'spock' and ordenador in relacion_ganadora[jugador_01]:
        return 2
        
    
# No lo borro por Morriña y miedo a parte iguales 🤣
#    if jugador_01 == ordenador:
#        return 0
#    
#    elif ordenador == 'scissors' and jugador_01 == 'paper' or ordenador == 'paper' and jugador_01 == 'rock' or ordenador == 'rock' and jugador_01 == 'scissors':
#        return 1
#    
#    elif jugador_01 == 'scissors' and ordenador == 'paper' or jugador_01 == 'paper' and ordenador == 'rock' or jugador_01 == 'rock' and ordenador == 'scissors':
#        return 2


# In[6]:


#5.- Sacamos por pantalla todas las evaluaciones previas (en verdad esta solo actualiza las variables *_score)

def victoria_de (ordenador, jugador_01, numero):
    
    """
    Based in the number return of definir_ganador function, add +1 in *_score properly if needed
    
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
    
    
    
    if numero == 0:
        pass
        
    else:       
        if numero == 1:
            cpu_score +=1
        elif numero == 2:
            player_score += 1


# In[7]:


#6.- podría meter toda esta fantasía en la función anterior, pero como son pruebas y me parece que va a quedar muy loco,
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
    dict_emojis = {'paper' : '🖐', 'scissors' : '✌', 'rock' : '✊', 'lizard' : '🤏', 'spock' : '🖖'}
    # Y lo he ampliado a mano como los buenos Noob en vez de con una función.
    
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

     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫
     ------------🧠-🧠-🧠-------------
                     3            
     -----------------------------------
     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫    

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

     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫
     ------------🧠-🧠-🧠-------------
                     2            
     -----------------------------------
     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫    

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
     ------------🧠-🧠-🧠-------------
                     1            
     -----------------------------------
     ▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫    

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


# In[8]:


#7.- Me he creado una función para pedir un número, me vale para utilizarla recorriendo menús

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


# In[9]:


#8.- Función que imprime el resultado del juego tras haber superado todas las rondas seleccionadas o tras haber ganado un jugador

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


# In[66]:


#10.- ESTRUCTURA DEL JUEGO

# En este bloque vamos a condensar el flujo del juego, me copiaré aquí algunas de las variables
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

#### Venga planteate en un futuro meter el juego como tal en una deficición y poder elegir desde el menú opciones a qué juego quieres jugar

exit = False
opcion_menu = 0
turnos = 0

while not exit:

    print ('''

▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪
-----------------🧠-🧠-🧠------------------
---------------------------------------------

 1.- Jugar: piedra ✊, papel 🖐, tijera ✌,
                 lagarto🤏, spock🖖.
 
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


# In[ ]:




