#!/usr/bin/env python3
"""
Autor : Natalia Adell <10752563@iespenyagolosa.es>
Fecha   : 08/11/22
Propósito: diferentes listas a partir de un número
"""

num=int(input('Escribe un número positivo: '))
while num<=0:
    print('¡Te he pedido un número positivo!')
    num=int(input('Escribe un número positivo: '))

for i in range(0,num+1):
    print(i,end=", ")

print()
for i in range(num,0-1,-1):
    print(i,end=", ")

print()
for i in range(1,num):
    print(i,end=", ")

print()
for i in range(num-1,0,-1):
    print(i,end=", ")

print()
for i in range(0,num+1):
    print(i,end=", ")

for i in range(num-1,0-1,-1):
    print(i,end=', ')