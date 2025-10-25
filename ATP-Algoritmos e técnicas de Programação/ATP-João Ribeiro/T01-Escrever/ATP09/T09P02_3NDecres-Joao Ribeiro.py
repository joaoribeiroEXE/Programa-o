'''
   NomeProg.. : T09P02_3NDecres-Joao Ribeiro.py
   Descrição.. : 02) Ordenar 3 Números em Ordem Decrescente.
   Autor......: Joao Ribeiro
'''
# Ler três números
a = float(input("Digite o 1º número: "))
b = float(input("Digite o 2º número: "))
c = float(input("Digite o 3º número: "))

# Ordenar usando comparações
if a >= b and a >= c:
    primeiro = a
    if b >= c:
        segundo, terceiro = b, c
    else:
        segundo, terceiro = c, b
elif b >= a and b >= c:
    primeiro = b
    if a >= c:
        segundo, terceiro = a, c
    else:
        segundo, terceiro = c, a
else:
    primeiro = c
    if a >= b:
        segundo, terceiro = a, b
    else:
        segundo, terceiro = b, a

# Saída
print("Ordem decrescente: ", primeiro, segundo, terceiro)

input()