'''
   NomeProg.. : T09P10_MReg3-Joao Ribeiro.py
   Descrição.. : 10) Cálculos das Regras de 3: Porcentagem, Velocidade Média,
                 Consumo Médio e Circuito Simples. Cada item com 3 sub-itens.
   Autor......: Joao Ribeiro
'''
def porcentagem():
    print("Porcentagem - opções: 1) Valor correspondente a uma %  2) Qual % de um valor  3) Aumentar/Diminuir por %")
    op = input("Escolha sub-opção: ")
    if op == "1":
        valor = float(input("Valor total: ")); pct = float(input("Percentual (%): "))
        print(f"Resultado = {valor * pct/100:.2f}")
    elif op == "2":
        parte = float(input("Parte: ")); total = float(input("Total: "))
        if total == 0: print("Erro: total zero")
        else: print(f"Percentual = {parte/total*100:.2f}%")
    elif op == "3":
        valor = float(input("Valor inicial: ")); pct = float(input("Percentual (%): "))
        tipo = input("Aumentar (A) ou Diminuir (D)? ").strip().upper()
        if tipo == "A":
            print("Novo valor =", valor * (1 + pct/100))
        else:
            print("Novo valor =", valor * (1 - pct/100))
    else:
        print("Opção inválida")

def velocidade_media():
    print("Velocidade média - opções: 1) Distância/Tempo 2) Soma tempos com segmentos 3) Conversão unidades")
    op = input("Escolha sub-opção: ")
    if op == "1":
        d = float(input("Distância (km): ")); t = float(input("Tempo (h): "))
        if t == 0: print("Erro: tempo zero")
        else: print("Velocidade média =", d / t, "km/h")
    else:
        print("Sub-opção simplificada selecionada (implemente conforme necessário)")

def consumo_medio():
    print("Consumo médio: km por litro")
    km = float(input("Km percorridos: ")); litros = float(input("Litros consumidos: "))
    if litros == 0: print("Erro: litros zero")
    else: print("Consumo médio =", km / litros, "km/l")

def circuito_simples():
    print("Circuito simples - Exemplo: calcular resistência equivalente em série/paralelo")
    op = input("1) Série 2) Paralelo: ")
    if op == "1":
        r1 = float(input("R1: ")); r2 = float(input("R2: "))
        print("Req =", r1 + r2)
    else:
        r1 = float(input("R1: ")); r2 = float(input("R2: "))
        if r1 == 0 or r2 == 0:
            print("Erro: resistência zero em paralelo")
        else:
            print("Req =", 1 / (1/r1 + 1/r2))

# Menu principal com 4 grupos (cada grupo tem sub-opções)
while True:
    print("""
Menu - Regras de 3
1) Porcentagem (3 sub-itens)
2) Velocidade Média (3 sub-itens)
3) Consumo Médio (3 sub-itens)
4) Circuito Simples (3 sub-itens)
0) Sair
""")
    op = input("Escolha: ")
    if op == "1": porcentagem()
    elif op == "2": velocidade_media()
    elif op == "3": consumo_medio()
    elif op == "4": circuito_simples()
    elif op == "0": break
    else: print("Opção inválida")
input()