#NomeProg..: [T03P19_RestoReal-JoaoRibeiro.py]
#Descrição...: xx) Absoluto.................................... de um (1) Número [T03P01_Absoluto-JoaoRibeiro.py]
#Autor...........: Joao Ribeiro


import math
import cmath

n1= float(input('1° N°: '))
n2= float(input('2° N°'))

ab= math.fmod(n1, n2)

print(f'O resultado do resto da divisão entre {n1} e {n2} é =', ab)