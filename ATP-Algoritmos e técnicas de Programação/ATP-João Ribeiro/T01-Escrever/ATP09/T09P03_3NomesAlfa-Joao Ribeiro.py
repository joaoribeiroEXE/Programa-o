'''
   NomeProg.. : T09P03_3NomesAlfa-Joao Ribeiro.py
   Descrição.. : 03) Ordenar 3 Nomes em Ordem Alfabética.
   Autor......: Joao Ribeiro
'''
# Ler três nomes (trim e lower para comparação consistente)
n1 = input("Digite o 1º nome: ").strip()
n2 = input("Digite o 2º nome: ").strip()
n3 = input("Digite o 3º nome: ").strip()

# Para manter a exibição original, usaremos tuplas (nome, chave de comparação)
t = [(n1, n1.lower()), (n2, n2.lower()), (n3, n3.lower())]

# Ordenar pela chave (alfabética)
t_sorted = sorted(t, key=lambda x: x[1])

# Saída (apenas os nomes originais na ordem)
print("Ordem alfabética:")
for nome, _ in t_sorted:
    print(nome)
input()