#!/usr/bin/env python3
"""
Autor : Natalia Adell <10752563@iespenyagolosa.es>
Fecha   : 07/11/22
Propósito: lista números consecutivos
"""

num=int(input('Escribe un número y te diré los consecutivos hasta este: '))
if num>=0:
     for i in range(num+1):
          print(i,end=', ')
else:
     for i in range(0,num-1,-1):
          print(i,end=", ")

print()