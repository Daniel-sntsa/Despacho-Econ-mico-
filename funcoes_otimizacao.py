import numpy as np
from scipy.optimize import minimize

def calcular_custo_minimo(funcs_custo, demandas, perdas, limites=0):
    n = len(funcs_custo)
    resultados = []

    def func_objetivo(potencias):
        return sum(sum(coeff * potencias[i]**(len(coeffs)-1-j) for j, coeff in enumerate(coeffs)) for i, coeffs in enumerate(funcs_custo))

    def func_perdas(potencias, perdas):
        return sum(sum(coeff * potencias[i]**(len(coeffs)-1-j) for j, coeff in enumerate(coeffs)) for i, coeffs in enumerate(perdas))

    def deriv_perdas(potencias, perdas):
        deriv = np.zeros(n)
        for i, coeffs in enumerate(perdas):
            for j, coeff in enumerate(coeffs):
                if len(coeffs)-1-j > 0:
                    deriv[i] += coeff * (len(coeffs)-1-j) * potencias[i]**(len(coeffs)-2-j)
        return deriv

    def restricao(potencias, D, perdas):
        return sum(potencias) - D - func_perdas(potencias, perdas)

    if limites == 0:
        limites = [(0, None) for _ in range(n)]

    for D in demandas:
        chute_inicial = [D / n] * n
        resultado = minimize(func_objetivo, chute_inicial,
                             constraints={'type': 'eq', 'fun': restricao, 'args': (D, perdas,)},
                             bounds=limites, method='SLSQP')

        if not resultado.success:
            raise ValueError(f"Não foi possível encontrar solução para a demanda {D}.")

        potencias_otimas = resultado.x
        fator_penalidade = 1 / (1 - deriv_perdas(potencias_otimas, perdas))
        lambida = resultado.jac * fator_penalidade
        perdas_geradores = [sum(coeff * potencias_otimas[i]**(len(coeffs)-1-j) for j, coeff in enumerate(coeffs)) for i, coeffs in enumerate(perdas)]
        perdas_total = sum(perdas_geradores)
        custo_geradores = [sum(coeff * potencias_otimas[i]**(len(coeffs)-1-j) for j, coeff in enumerate(coeffs)) for i, coeffs in enumerate(funcs_custo)]
        potencias_total = sum(potencias_otimas)

        resultados.append((potencias_otimas, resultado.fun, lambida, perdas_geradores, custo_geradores, perdas_total, potencias_total))

    return resultados


def calcular_lambida_na_potencia(funcs_custo, limites):
    lambidas = []
    for pot in limites:
        for coeffs in funcs_custo:
            deriv = sum(coeff * (len(coeffs)-1-j) * pot**(len(coeffs)-2-j) for j, coeff in enumerate(coeffs) if len(coeffs)-1-j > 0)
            lambidas.append(deriv)
    return lambidas


def calc_lambdas(funcs_custo, limites):
    lista_lambdas = []
    for i in range(len(funcs_custo)):
        lambida = calcular_lambida_na_potencia([funcs_custo[i]], limites[i])
        lista_lambdas.append(lambida)

    lambdas_min = [x[0] for x in lista_lambdas]
    lambdas_max = [x[1] for x in lista_lambdas]
    return [lambdas_min, lambdas_max]


def calcular_potencia_no_lambida(funcs_custo, lambida):
    potencias = []
    for coeffs in funcs_custo:
        deriv_coeffs = [(len(coeffs)-1-j) * coeff for j, coeff in enumerate(coeffs[:-1])]
        deriv_coeffs[-1] -= lambida
        roots = np.roots(deriv_coeffs)
        real_roots = [r.real for r in roots if np.isclose(r.imag, 0)]
        if not real_roots:
            raise ValueError("Não foi possível encontrar potência para o lambda fornecido.")
        potencias.append(min(real_roots))
    return [float(p) for p in potencias]
