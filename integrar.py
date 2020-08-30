####################################################################
# Alejandro Tejada 17584
# Diego Sevilla 17238
####################################################################
# Curso: Modelación y simulación
# Programa: integrar.py
# Propósito: este programa es para la hoja de Barnsley
# Fecha: 08/2020
####################################################################
# %%
import math


def pseudo(a, m):
    def inner_pseudo(xo, n):
        items = list(range(n))
        items[0] = xo

        for i in range(1, n):
            items[i] = (a*items[i-1]) % m

        return [i/float(m) for i in items]
    return inner_pseudo


# Calculando integrales con numeros randoms
# def g(x): return 5*x**2+3*x+2
# definimos la función
def g(x): return 2*((math.exp((-1) * ((1/x)-1)**2))/(x**2))


mi_pseudo = pseudo(m=2**31-1, a=7**5)

mis_randoms = mi_pseudo(xo=5, n=100000)

a_evaluar = [g(i) for i in mis_randoms]

print(sum(a_evaluar)/len(a_evaluar))
