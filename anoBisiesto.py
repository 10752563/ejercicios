#!/usr/bin/env python3
ano=int(input('Introduce un año para comprobar si es bisiesto: '))
condicion1=(ano%4==0) and not (ano%100==0)
condicion2=(ano%400==0)
if condicion1 or condicion2:
    print('Es un año bisiesto.')
else:
    print('No es un año bisiesto.')