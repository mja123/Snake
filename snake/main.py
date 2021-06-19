"""
  PROGRAMACIÓN I
  PROF. ERASO Y PROF. ONTIVEROS
  TP 5
  SNAKE

  AUTORES:
  MATÍAS AGUILAR
  FRANCISCO GONZÁLEZ DEL SOLAR
"""

import os
import random
import time
import keyboard as kb

run = True
vibora = [[5, 5]]


ROWS = 10
COLS = 10

print("Bienvenidos/as al juego de snake!")
nombre_usuario = input("Por favor, ingrese su nombre: ")


def comprobar_estado():
    """
    Comprueba si el jugador ha perdido.
    """
    for i in range(len(vibora)):
        if i != 0:
            if vibora[i][0] == vibora[0][0] and vibora[i][1] == vibora[0][1]:
                return False
    return True



def mostrar_juego(fruta):
    """
    Muestra en pantalla el tablero, la víbora y la fruta.
    """

    os.system('cls') 
    for row in range(ROWS):
        for col in range(COLS):            
            if row == fruta[0] and col == fruta[1]:
                print('F', end=" ")
            else:
                pos = [row, col]
                if pos in vibora:
                    print('#', end=" ")
                else:
                    print('.', end=" ")
        print()

def limite_tablero():
    """
    Delimita los bordes del tablero, cuando la vibora se encuentra con uno, continua hasta la parte
    opuesta del tablero.
    """
    if vibora[0][0] >= ROWS:
        vibora[0][0] = 0
    elif vibora[0][0] < 0:
        vibora[0][0] = ROWS
    if vibora[0][1] >= COLS:
        vibora[0][1] = 0
    elif vibora[0][1] < 0:
        vibora[0][1] = COLS

def posicionar_fruta():
    """
    Elige una posición aleatoria en el tablero que no coincida con la posición de la víbora.
    """

    row = random.randint(0, ROWS - 1)
    col = random.randint(0, COLS - 1)
    fruta = [row, col]

    while fruta in vibora:
        row = random.randint(0, ROWS - 1)
        col = random.randint(0, COLS - 1)
        fruta = [row, col] 
    
    return fruta

def comer_fruta(fruta):
    """
    Si la cabeza de la vibora coincide con la fruta, se agrega
    un elemento al array vibora (una parte de cuerpo) y retorna
    Verdadero.
    """

    global vibora

    if vibora[0] == fruta:
        vibora.append(["A", "A"])
        return True



def actualizar_posicion(direccion):
    """
    Actualiza la posición de la vibora en el tablero luego de realizar un movimiento
    por teclado.
    """
    global vibora
    for i in range(len(vibora) - 1, -1, -1):
        if i != 0: # Actualizar cuerpo
            vibora[i][0] = vibora[i - 1][0]
            vibora[i][1] = vibora[i - 1][1]
        else: # actualizar cabeza
            vibora[0][0] += direccion[0]
            vibora[0][1] += direccion[1]
            
def escuchar_teclado(direccion):
    """
    Cambia la dirección de la vibora a medida que se presionan las respectivas teclas del teclado.
    """
 
    if kb.is_pressed('up'):
        if direccion != [1, 0]:
            direccion = [-1, 0]
    elif kb.is_pressed('down'):
        if direccion != [-1, 0]:
            direccion = [1, 0]    
    elif kb.is_pressed('right'):
        if direccion != [0, -1]:
            direccion = [0, 1]        
    elif kb.is_pressed('left'):
        if direccion != [0, 1]:
            direccion = [0, -1 ]

    return direccion


def fin_juego():
    """
    Muestra el puntaje final obtenido luego de perder.
    """
    global vibora
    os.system('cls') 
    puntaje = (len(vibora) - 1) * 100

    print(f'¡Qué pena! Perdiste. {nombre_usuario} Sos un LOSER!!!!')
    print(f'Tu puntaje es: {puntaje}')
    

def reiniciar_juego():
    """
    Da la opción de reiniciar el juego una vez perdido.
    """
    global run, vibora

    jugar_nuevamente = input("¿Jugar nuevamente? Si (s) / No (n): ")
    if jugar_nuevamente == "s":

        vibora = [[5, 5]]
        posicion_fruta = posicionar_fruta()
        run = True

def main ():
    """
    Parte principal del programa, maneja las llamadas a las distintas funciones, se encarga del funcionamiento
    del juego.
    """
    global vibora, run
    direccion = [1, 0]
    posicion_fruta = posicionar_fruta()  


    while run:

        if comer_fruta(posicion_fruta):
            posicion_fruta = posicionar_fruta()

        actualizar_posicion(direccion)
        limite_tablero()
        mostrar_juego(posicion_fruta)
        direccion = escuchar_teclado(direccion)
        
        run = comprobar_estado()
        if run == False:
            fin_juego()
            reiniciar_juego()

        time.sleep(0.1)


if __name__ == '__main__':
    main()