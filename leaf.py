
####################################################################
# Alejandro Tejada 17584
# Diego Sevilla 17238
####################################################################
# Curso: Modelación y simulación
# Programa: leaf.py
# Propósito: este programa es para la hoja de Barnsley
# Fecha: 08/2020
####################################################################
#%%#
# --------------------- ZONA DE LIBRERIAS---------------
import matplotlib.pyplot as plt
from random import randint

# initializing the list
x = []
y = []

# setting first element to 0
x.append(0)
y.append(0)

current = 0
# Creamos el ciclo
for i in range(1, 100000):

    #! P	= {0.85,	0.07,	0.07,	0.01}
    # se genera un random entre 1 y 100
    z = randint(1, 100)
    # las coordenadas X, Y de las ecuaciones son ingresadas en cada lista

    # Para la probabilidad de: 0.01
    # ? f4(x, y) à (x*0.0 + y*0.0, x*0.0 + y*0.16)
    if z == 1:
        x.append(0)
        y.append(0.16*(y[current]))

    # Para la probabilidad de:  0.85
    # ? f1(x, y) à (x*0.85 + y*0.04 + 0.0, x*-0.04 + y*0.85 + 1.6)
    if z >= 2 and z <= 86:
        x.append(0.85*(x[current]) + 0.04*(y[current]))
        y.append(-0.04*(x[current]) + 0.85*(y[current])+1.6)

    # Para la probabilidad de: 0.07
    # ? f3(x, y) à (x*0.2 + y*-0.26 + 0.0, x*0.23 + y*0.22 + 1.6)
    if z >= 87 and z <= 93:
        x.append(0.2*(x[current]) - 0.26*(y[current]))
        y.append(0.23*(x[current]) + 0.22*(y[current])+1.6)

    # Para la probabilidad de:  0.07
    # ? f2(x, y) à (-0.15*x + 0.28*y + 0.0, x*0.26 + y*0.24 + 0.44)
    if z >= 94 and z <= 100:
        x.append(-0.15*(x[current]) + 0.28*(y[current]))
        y.append(0.26*(x[current]) + 0.24*(y[current])+0.44)

    current = current + 1
# Se desplega el título y los valores
plt.title("Hojita de Barnsley")
plt.scatter(x, y, s=0.2, edgecolor='red')
plt.xlabel('Lista de X')
plt.ylabel('Lista de Y')
plt.show()

# %%
