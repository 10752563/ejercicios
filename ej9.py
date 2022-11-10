#!/usr/bin/env python3
"""
Autor : Natalia Adell <10752563@iespenyagolosa.es>
Fecha   : 08/11/22
Propósito: lista de números pares
"""

num1=int(input('Dime un número inicial: '))
num2=int(input('Dime el valor final: '))

while num1>=num2:
    print('El valor final es menor que el inicial')
    num2=int(input('Dime otro valor final: '))

for i in range(num1,num2+1):
    if i%2==0:
        print(i,end=', ')