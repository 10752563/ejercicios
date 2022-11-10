#!/usr/bin/env python3
"""
Autor : Natalia Adell <10752563@iespenyagolosa.es>
Fecha   : 31/10/22
Propósito: Calcular el área de un triangulo o de un círculo
"""
print('Cálculo de áreas, lige una figura geométrica: ')
print('a) triangulo')
print('b) círculo')
figura=input('¿Que figura quieres calcular (escribe C o T)? ').upper()
if figura=='T':
    base=float(input('Escribe la base: '))
    altura=float(input('Escribr la altura: '))
    area=base*altura/2
    print(f'Un triángulo de base {base} y de altura {altura} tiene un area de {area}')
elif figura=='C': 
    radio=float(input('Escribe el radio: '))
    area=3.14*radio**2
    print(f'Un círculo de radio {radio} tiene una area de {area}')
else :
    print(f'No es un círculo o un tríangulo')