#!/usr/bin/env python3
"""
Autor : Natalia Adell <10752563@iespenyagolosa.es>
Fecha   : 09/11/22
Propósito: Números factoriales
"""

num=int(input('Escribe un número positivo: '))
factorial=1

for i in range(1,num+1):
    factorial=factorial*i

print(f'El factorial de {num} es {factorial}')