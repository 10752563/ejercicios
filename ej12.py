#!/usr/bin/env python3
"""
Autor : Natalia Adell <10752563@iespenyagolosa.es>
Fecha   : 10/11/22
Propósito: Dibujar un rectángulo
"""

anch=int(input('Anchura del rectángulo: '))
alt=int(input('Altura del rectángulo: '))

for i in range(anch):
    for j in range(alt):
        print('*',end=' ')
    print()