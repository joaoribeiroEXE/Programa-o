'''
   NomeProg.. : T09P04_NPosNegNulo-Joao Ribeiro.py
   Descrição.. : 04) Verificar se um número é Negativo, Positivo ou Nulo.
   Autor......: Joao Ribeiro
'''
# Ler número
n = float(input("Digite um número: "))

# Teste das condições
if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Nulo (zero)")

input()