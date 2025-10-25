'''
   NomeProg.. : T08P05_CatAtleta-Joao Ribeiro.py
   Descrição.. : 05) Verificar a categoria de um atleta pela idade.
   Autor......: Joao Ribeiro
'''
# Ler idade
idade = int(input("Digite a idade do atleta: "))

# Determinar categoria
if idade < 7:
    categoria = "Abaixo de 7 (sem categoria específica)"
elif 7 <= idade <= 9:
    categoria = "Dente de Leite"
elif 10 <= idade <= 12:
    categoria = "Mirim"
elif 13 <= idade <= 15:
    categoria = "Infantil"
elif 16 <= idade <= 18:
    categoria = "Juvenil"
elif 19 <= idade <= 21:
    categoria = "Júnior"
else:
    categoria = "Profissional"

# Saída
print("Categoria:", categoria)


input()