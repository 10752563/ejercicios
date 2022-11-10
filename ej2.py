#!/usr/bin/env python3
"""
Autor : Natalia Adell <10752563@iespenyagolosa.es>
Fecha   : 25/10/22
Propósito: Conversión de segundos a minutos
"""

print('Convertidor de segundos a minutos')

segundos=float(input('Escribe el tiempo en segundos: '))
minutos=segundos//60
segundos_restantes=segundos%60
print(f'{segundos} seg son {minutos} min y {segundos_restantes}')