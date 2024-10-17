#!/usr/bin/env python
'''Divisio entera. Fem una divisio de dos nomres i donem el quocient i el
residu
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24
Dividim dos nomres o fent que ho siguin depres fem la divisio de dos nomres
coresponent i donem com a reultats el quocient i el reidu de la divisio.
programa i el resultat esperat.
'''
__author__ = "Tristan Bert"
__email__ = "tbert@instituticaria.cat"
__date__ = "2024/10/16"

print('Quins dos nomre bols dividir:')

print('Quin es el dividend?')
dividend = int(input())

print('Quin es el divisor?')
divisor = int(input())

quocient = dividend//divisor
residu = dividend % divisor

print(f'Divisió: {dividend}/{divisor}')
print('Quocient:', quocient,)
print('Residu:', residu,)
