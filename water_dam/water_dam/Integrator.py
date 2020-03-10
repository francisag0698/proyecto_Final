import numpy as np
import math


class Integrator:
    def __init__(self, xMin, xMax, N = 1000000):
        self.__xMin = xMin
        self.__xMax = xMax
        self.__N = N
        self.__sumatoria = 0
    
    def __function_value(self, x):  # pi * x^2
        return math.pi * x**2
    
    def integrate(self):
        print("Calculando integral...")
        delta_x = (self.__xMax - self.__xMin) / (self.__N - 1)
        for i in range(self.__N):
            x_i = self.__xMin + (i * delta_x)
            self.__sumatoria += self.__function_value(x_i) * delta_x
        print(f"Respuesta: {round(self.__sumatoria, 5)}")
        return round(self.__sumatoria, 5)

    def bisection(self, a, b, tol):
        print("Ejecutando algoritmo root-finding...")
        xl = a
        xr = b
        while(np.abs(xl-xr) >= tol):
            c = (xl + xr)/2
            prod = self.__function_value(xl) * self.__function_value(c)
            if prod > tol:
                xl = c
            else:
                xr = c
        print(f"Respuesta: {round(c, 5)}")
        return c
