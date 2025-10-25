'''
   NomeProg.. : T09P01_3NCres-Joao Ribeiro.py
   Descrição.. : 01) Ordenar 3 Números em Ordem Crescente.
   Autor......: Joao Ribeiro
'''
# Ler três números
a = float(input("Digite o 1º número: "))
b = float(input("Digite o 2º número: "))
c = float(input("Digite o 3º número: "))

# Ordenar usando comparações (if/elif/else)
if a <= b and a <= c:
    primeiro = a
    if b <= c:
        segundo, terceiro = b, c
    else:
        segundo, terceiro = c, b
elif b <= a and b <= c:
    primeiro = b
    if a <= c:
        segundo, terceiro = a, c
    else:
        segundo, terceiro = c, a
else:
    primeiro = c
    if a <= b:
        segundo, terceiro = a, b
    else:
        segundo, terceiro = b, a

# Saída
print("Ordem crescente: ", primeiro, segundo, terceiro)
input()