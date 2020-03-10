from Integrator import Integrator
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    # Ingreso de datos
    h_max = float(input("Altura máxima de agua: "))
    h = float(input("Altura actual de agua: "))

    # Comprobar condiciones de la altura ingresada
    if(h < 0):
        h = 0 # h = 0 cuando este sea menor a 0
    elif (h > h_max):
        h = h_max # h = h_max cuando h supere el limite

    integrator = Integrator(0, h) #Clase integradora
    V = integrator.integrate() #Se integra la funcion pi * x^2
    u = integrator.bisection(-1*h, h, 1e-6) #Algoritmo root-finding | Metodo de Bisección con tolerancia de 1e-6
    V_u = V + u #Volumen total de la presa

    # FUNCION PARA DIBUJAR LA GRAFICA
    x = np.linspace(-5,5,100)
    plt.plot(x, integrator.function_value(x))
    plt.grid()

    # Valor del volumen cuando la altura es la máxima
    integrator_max = Integrator(0, h_max)
    v_max = integrator_max.integrate()

    # Comprobar si V(u) supera a V(h_max) entonces se vuelve
    # a realizar el calculo con u = h_max ó u = 0
    if(V_u > v_max):
        V_u = V + h_max

    if(V_u < 0):
        V_u = V

    # RESULTADOS
    print(f"V(u): {round(V_u, 5)}, V_max(h_max): {round(v_max,5)}")
    plt.show()
    
main()
    