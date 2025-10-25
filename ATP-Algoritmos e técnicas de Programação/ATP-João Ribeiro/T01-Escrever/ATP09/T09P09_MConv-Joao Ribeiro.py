'''
   NomeProg.. : T09P09_MConv-Joao Ribeiro.py
   Descrição.. : 09) Menu: Cálculos das Conversões (08 opções).
   Autor......: Joao Ribeiro
'''
def c_celsius_to_f():
    c = float(input("Temperatura em Celsius: "))
    f = c * 9/5 + 32
    print(f"{c} °C = {f:.2f} °F")

def c_f_to_c():
    f = float(input("Temperatura em Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f} °F = {c:.2f} °C")

def km_to_miles():
    km = float(input("Distância em km: "))
    print(f"{km} km = {km/1.60934:.4f} milhas")

def miles_to_km():
    mi = float(input("Distância em milhas: "))
    print(f"{mi} milhas = {mi*1.60934:.4f} km")

def m_to_cm():
    m = float(input("Comprimento em metros: "))
    print(f"{m} m = {m*100:.2f} cm")

def cm_to_m():
    cm = float(input("Comprimento em centímetros: "))
    print(f"{cm} cm = {cm/100:.2f} m")

def liters_to_gallons():
    l = float(input("Litros: "))
    print(f"{l} L = {l/3.78541:.4f} galões (US)")

def gallons_to_liters():
    g = float(input("Galões (US): "))
    print(f"{g} galões = {g*3.78541:.4f} L")

menu = {
    "1": ("Celsius -> Fahrenheit", c_celsius_to_f),
    "2": ("Fahrenheit -> Celsius", c_f_to_c),
    "3": ("Km -> Milhas", km_to_miles),
    "4": ("Milhas -> Km", miles_to_km),
    "5": ("Metros -> Centímetros", m_to_cm),
    "6": ("Centímetros -> Metros", cm_to_m),
    "7": ("Litros -> Galões (US)", liters_to_gallons),
    "8": ("Galões (US) -> Litros", gallons_to_liters)
}

while True:
    print("\nMenu - Conversões")
    for k, v in menu.items():
        print(k, ") ", v[0])
    print("0 ) Sair")
    op = input("Escolha: ")
    if op == "0": break
    if op in menu:
        menu[op][1]()
    else:
        print("Opção inválida.")
input()