from Integrator import Integrator
import numpy as np
import math

def main():
    h_max = float(input("Nivel máximo de agua: "))
    h = float(input("Nivel actual de agua: "))
    v = float(input("Volumen actual: "))

    if(h < 0):
        h = 0
    elif (h > h_max):
        h = h_max

    integrator = Integrator(0, h)
    V = integrator.integrate()
    u = integrator.bisection(h, v, 1e-6) # Tolerancia de 1e-6
    V_u = V + u

    integrator_max = Integrator(0, h_max)
    v_max = integrator_max.integrate()

    print(f"V(u): {round(V_u, 5)}, V_max(h_max): {round(v_max,5)}")
    if(V_u <= v_max and V_u >= 0):
        print("La ecuación tiene solución.")
    else:
        print("La ecuación no tiene solución.")

main()
    