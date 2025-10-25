'''
   NomeProg.. : T09P07_MOpMat-Joao Ribeiro.py
   Descrição.. : 07) Menu: Cálculos das Operações Matemáticas (07 opções).
   Autor......: Joao Ribeiro
'''
def soma():
    a = float(input("A: ")); b = float(input("B: "))
    print("Soma =", a + b)

def subtracao():
    a = float(input("A: ")); b = float(input("B: "))
    print("Subtração =", a - b)

def multiplicacao():
    a = float(input("A: ")); b = float(input("B: "))
    print("Multiplicação =", a * b)

def divisao():
    a = float(input("A: ")); b = float(input("B: "))
    if b == 0:
        print("Erro: divisão por zero")
    else:
        print("Divisão =", a / b)

def potencia():
    a = float(input("Base: ")); b = float(input("Expoente: "))
    print("Potência =", a ** b)

def raiz():
    a = float(input("Número: "))
    if a < 0:
        print("Erro: raiz de número negativo (número complexo não tratado)")
    else:
        print("Raiz quadrada =", a ** 0.5)

def resto():
    a = int(input("A (inteiro): ")); b = int(input("B (inteiro): "))
    if b == 0:
        print("Erro: módulo por zero")
    else:
        print("Resto =", a % b)

# Menu principal
while True:
    print("""
Menu - Operações Matemáticas
1) Soma
2) Subtração
3) Multiplicação
4) Divisão
5) Potência
6) Raiz Quadrada
7) Resto (módulo)
0) Sair
""")
    op = input("Escolha uma opção: ")
    if op == "1": soma()
    elif op == "2": subtracao()
    elif op == "3": multiplicacao()
    elif op == "4": divisao()
    elif op == "5": potencia()
    elif op == "6": raiz()
    elif op == "7": resto()
    elif op == "0":
        print("Encerrando menu.")
        break
    else:
        print("Opção inválida. Tente novamente.")
input()