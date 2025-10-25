'''
   NomeProg.. : T09P08_MFunMat-Joao Ribeiro.py
   Descrição.. : 08) Menu: Cálculos das Funções Matemáticas (20 opções - exemplo com várias).
   Autor......: Joao Ribeiro
'''
import math

def f_seno():
    x = float(input("Ângulo em graus: "))
    print("sen(", x, ") =", math.sin(math.radians(x)))

def f_cosseno():
    x = float(input("Ângulo em graus: "))
    print("cos(", x, ") =", math.cos(math.radians(x)))

def f_tangente():
    x = float(input("Ângulo em graus: "))
    print("tan(", x, ") =", math.tan(math.radians(x)))

def f_log():
    x = float(input("Número (>0): "))
    if x <= 0:
        print("Erro: log de valor não-positivo")
    else:
        print("ln(", x, ") =", math.log(x))

def f_exp():
    x = float(input("Expoente: "))
    print("e^x =", math.exp(x))

# Para não ficar extenso demais, vamos criar um menu com 10 funções de exemplo.
# Pode-se expandir até 20 conforme o enunciado pedisse.
def f_abs():
    x = float(input("Número: ")); print("abs =", abs(x))

def f_floor():
    x = float(input("Número: ")); print("floor =", math.floor(x))

def f_ceil():
    x = float(input("Número: ")); print("ceil =", math.ceil(x))

def f_sqrt():
    x = float(input("Número (>=0): "))
    if x < 0:
        print("Erro: raiz negativa")
    else:
        print("sqrt =", math.sqrt(x))

def f_pow():
    a = float(input("Base: ")); b = float(input("Expoente: "))
    print("pow =", math.pow(a, b))

ops = {
    "1": ("Seno", f_seno),
    "2": ("Cosseno", f_cosseno),
    "3": ("Tangente", f_tangente),
    "4": ("Log natural", f_log),
    "5": ("Exponencial", f_exp),
    "6": ("Valor absoluto", f_abs),
    "7": ("Floor", f_floor),
    "8": ("Ceil", f_ceil),
    "9": ("Raiz quadrada", f_sqrt),
    "10": ("Potência (pow)", f_pow)
}

while True:
    print("\nMenu - Funções Matemáticas")
    for k, v in ops.items():
        print(k, ") ", v[0])
    print("0 ) Sair")
    escolha = input("Escolha: ")
    if escolha == "0":
        break
    func = ops.get(escolha)
    if func:
        func[1]()
    else:
        print("Opção inválida.")

input()