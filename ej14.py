#!/usr/bin/env python3
"""
Autor : Natalia Adell <10752563@iespenyagolosa.es>
Fecha   : 10/11/22
Propósito: Vocales por una vocal
"""

frase=int(input('Dime una frase: '))
vocal=int(input('Dime una vocal: '))
VOCALES='aeiouAEIOU'
frase_n=[]

for i in range(len(frase)):
    if frase[i] in VOCALES:
        frase_n.append(vocal)
    else:
        frase_n.append(frase[i])



print(f'La frase ahora es {frase_n}')