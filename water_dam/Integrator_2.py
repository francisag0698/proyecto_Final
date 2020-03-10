import numpy as np
import math


class Integrator:
    def __init__(self, xMin, xMax, N = 1000000):
        self.__xMin = xMin
        self.__xMax = xMax
        self.__N = N
        self.__sumatoria = 0
    
    def function_value(self, x):  # x
        return x
    
    def integrate(self):
        print("Calculando integral...")
        delta_x = (self.__xMax - self.__xMin) / (self.__N - 1)
        for i in range(self.__N):
            x_i = self.__xMin + (i * delta_x)
            self.__sumatoria += self.function_value(x_i) * delta_x
        print(f"Respuesta: {round(self.__sumatoria, 5)}")
        return round(self.__sumatoria, 5)
