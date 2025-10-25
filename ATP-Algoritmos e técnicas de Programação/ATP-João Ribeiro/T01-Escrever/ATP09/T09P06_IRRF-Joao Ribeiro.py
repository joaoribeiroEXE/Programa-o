'''
   NomeProg.. : T09P06_IRRF-Joao Ribeiro.py
   Descrição.. : 06) Calcular o IRRF (Imposto de Renda Retido na Fonte) mensal.
                 Usa tabela vigente a partir de 01/05/2025 (faixas/aliquotas/parcela a deduzir).
   Autor......: Joao Ribeiro
'''
# Observação: as faixas, alíquotas e parcela a deduzir foram consultadas em publicações oficiais.
# Referência: tabela IRRF/2025 (válida a partir de 01/05/2025).
# Entrada: salário bruto, INSS retido e número de dependentes.
salario = float(input("Salário bruto mensal (R$): "))
inss = float(input("INSS retido na folha (R$): "))
dependentes = int(input("Número de dependentes: "))

# Dedução por dependente (valor mensal)
deducao_dependente = 189.59  # conforme tabela atual (valor consultado)
# Calcular base de cálculo
base = salario - inss - (dependentes * deducao_dependente)

# Garantir não-negatividade
if base <= 0:
    irrf = 0.0
    aliquota = 0.0
    parcela_deduzir = 0.0
else:
    # Aplicar tabela progressiva (valores válidos a partir de 01/05/2025)
    # Faixas base de cálculo (R$) e parâmetros:
    # Até 2428.80 -> isento
    # 2428.81 - 2826.65 -> 7.5% , parcela a deduzir = 182.16
    # 2826.66 - 3751.05 -> 15%  , parcela a deduzir = 394.16
    # 3751.06 - 4664.68 -> 22.5%, parcela a deduzir = 675.49
    # Acima de 4664.68 -> 27.5%, parcela a deduzir = 908.73

    if base <= 2428.80:
        aliquota = 0.0
        parcela_deduzir = 0.0
    elif base <= 2826.65:
        aliquota = 0.075
        parcela_deduzir = 182.16
    elif base <= 3751.05:
        aliquota = 0.15
        parcela_deduzir = 394.16
    elif base <= 4664.68:
        aliquota = 0.225
        parcela_deduzir = 675.49
    else:
        aliquota = 0.275
        parcela_deduzir = 908.73

    # Cálculo do IRRF
    irrf = base * aliquota - parcela_deduzir
    if irrf < 0:
        irrf = 0.0

# Saída
print(f"Base de cálculo: R$ {base:.2f}")
print(f"Alíquota aplicada: {aliquota*100:.2f}%")
print(f"Parcela a deduzir: R$ {parcela_deduzir:.2f}")
print(f"IRRF mensal: R$ {irrf:.2f}")
input()