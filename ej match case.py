#!/usr/bin/env python3
"""
Autor : Natalia Adell <10752563@iespenyagolosa.es>
Fecha   : 02/11/22
Propósito: Adivinar un personaje de Marvel
"""
#Ejemplo uso de match case

#Pedimos el primer número
num1=int(input('Introduce el primer número. '))
#Pedimos el segundo número
num2=int(input('Escribe el segundo número: '))


#Pedimos la operación a realizar
operacion=input('Introduce la operación (+, -, *, /): ')

match operacion: 
    case '+':
        resultado=num1+num2
    case '-': 
        resultado=num1-num2
    case'*': 
        resultado=num1*num2
    case'/':
        resultado=num1/num2