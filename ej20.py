#!/usr/bin/env python3
"""
Autor : Natalia Adell <10752563@iespenyagolosa.es>
Fecha   : 03/11/22
Propósito: Adivinar un número
"""
from random import randrange 

num1=int(input('Valor mínimo: '))
num2=int(input('Valor máximo'))
aleatorio=randrange(num1,num2)
intentos=1
print(f'A ver si adivinas el número entero entre {num1} y {num2}.')

numero=int(input('Escribe un número: '))

while numero != aleatorio: 
    intentos += 1
    if numero<aleatorio:
        numero=int(input('¡Demasiado pequeño! Inténtalo de nuevo: '))
    else:
        numero=int(input('¡Demasiado grande! Inténtalo de nuevo: '))
print(f'¡Acertaste! Te ha costado {intentos} intentos.')