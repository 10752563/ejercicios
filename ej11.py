#!/usr/bin/env python3
"""
Autor : Natalia Adell <10752563@iespenyagolosa.es>
Fecha   : 09/11/22
Propósito: Calcular número mayor, menor y la media
"""

cant=int(input('¿Cuantos números quieres introducir?: '))
minimo=1000000
maximo=0
suma=0
media=0
for i in range(1,cant+1):
    num=int(input('Diume el número {i} '))
    suma+=num
    if num<minimo:
        minimo=num
    if num>maximo:
        maximo=num
media=suma/cant
print(f'El número más pequeño es: {minimo}')
print(f'El número más grande es: {maximo}')
print(f'La media de todos los números es: {media}')