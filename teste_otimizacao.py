import numpy as np
from tabulate import tabulate
from funcoes_otimizacao import calcular_custo_minimo, calc_lambdas, calcular_potencia_no_lambida

# 🔹 Dados de teste
funcs_custo = [
    [0.08, 6, 50],
    [0.1, 4, 60],
    [0.04, 8, 40]
]
limites = [
    [50, 220],
    [50, 200],
    [50, 200]
]
demandas = [200, 500]
perdas = [[0], [0], [0]]

# 🔹 Execução do cálculo
try:
    resultados = calcular_custo_minimo(funcs_custo, demandas, perdas, limites)
    for i, (potencias, custo_total_minimo, custo_marginal, perdas_geradores, custos_totais_geradores, perdas_total, potencias_total) in enumerate(resultados):
        print(f"\n===== RESULTADO PARA DEMANDA {demandas[i]} =====")
        headers = ["Gerador", "Potência (MW)", "Perdas (MW)", "Custo (R$)", "Custo Marginal (R$/MWh)"]
        data = [
            [f"Gerador {j+1}", round(p,3), round(perdas_geradores[j],3), round(custos_totais_geradores[j],2), round(custo_marginal[j],3)]
            for j, p in enumerate(potencias)
        ]
        data.append(["TOTAL", round(potencias_total,3), round(perdas_total,3), round(custo_total_minimo,2), "-"])
        print(tabulate(data, headers=headers, tablefmt="pretty"))

    # 🔹 Cálculo de lambdas
    lambdas_Gmin, lambdas_Gmax = calc_lambdas(funcs_custo, limites)
    print("\nLambda Geração Mínima:", lambdas_Gmin)
    print("Lambda Geração Máxima:", lambdas_Gmax)

    # 🔹 Potências para um lambda específico
    Potencias_tomada = calcular_potencia_no_lambida(funcs_custo, min(lambdas_Gmax))
    print("\nPotências calculadas para λ mínimo:", Potencias_tomada)

except ValueError as e:
    print(e)
