#!/usr/bin/env python3
"""
Autor : Natalia Adell <10752563@iespenyagolosa.es>
Fecha   : 07/11/22
Propósito: tabla de multiplicar
"""

num=int(input('Escribe un número y te diré su tabla de multiplicar: '))
for i in range(1,11):
    print(f'{num}x{i}={num*i}')