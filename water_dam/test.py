from Integrator import Integrator
import matplotlib.pyplot as plt
import numpy as np
import math

# MÉTODO PARA CALCULAR EL AGUA EVAPORADA
def evaporated_water(h, beta):
    beta_A_h = 0 
    if(h >= 0 and h <= 2):
        beta_A_h = 100 * h**2 # Si 0 <= h <= 2 entonces  A(h) = 100 * h^2
    else:
        beta_A_h = 400 * (h - 1) # Si h > 2 entonces A(h) = 400 * (h - 1)

    return beta * beta_A_h # Se multiplica A(x) con beta

def next_water_level(h, v):
    return math.sqrt(np.abs(h**2 + (2*v)))

# MÉTODO PRINCIPAL
def main():
    # Valores de los volúmenes de la presa desde t = 1 hasta t = n (donde n = 100)
    volume_values = [14.31711, 109.8815, 51.14796, 160.3442, 157.7805,175.5750,121.2473,161.8492,187.721,169.4947,140.8879,119.2000,37.49091,25.01957,22.79820,0,0,0,0,0,0,10.62324,0,0,0,22.28223,52.6329,144.3477,93.8219,139.6688,187.2834,112.8247,170.1796,134.1929,90.87007,76.63679,104.8290,77.77952,80.05338,59.25845,3.165104,4.118153,0,0,0,0,0,0,0,14.57985,36.72097,110.4422,51.784,116.5769,86.67932,95.27534,169.7252,153.6469,102.1357,102.4133,93.9651,47.40445,51.57885,8.300242,0,8.257363,0,0,0,0,0,0,0,0,45.41098,49.1152,78.02648,115.5585,136.0315,79.32947,172.7445,105.3199,181.9667,175.0501,177.4771,67.73758,123.1144,107.1043,44.44291,0.9399437,22.811,0,0,0,0,0,0,0,0,0]
    h_values = [] # Lista donde se almacenarán las alturas que se obtienen por día hasta t = n

    alpha = 1 # Volumen de agua tomado para su consumo
    beta = 0.05 # Valor que forma parte del cálculo para el agua evaporada

    h_max = 10 # Nivel máximo de agua de la presa
    h_t = 1 # Nivel de agua de la presa en el primer día empieza en 1
    

    for v in volume_values:
        # El nivel de agua no puede superar el nivel máximo 
        # (en este caso se podría decir que se ha desbordado y el sobrante se ha perdido)
        if(h_t > h_max):
            h_t = h_max
        
        # El nivel de agua no puede ser menor a 0
        if(h_t < 0):
            h_t = 0

        # Se almacena el nivel de agua del día actual t
        h_values.append(h_t)
        
        # Cálculo del agua perdida debido a la evaporación
        beta_A_h = evaporated_water(h_t, beta)

        # Cálculo del nivel de agua al comienzo del día siguiente (t + 1)
        h_t =  next_water_level(h_t, v - alpha - beta_A_h)

    # Dibujo de la gráfica
    x = np.linspace(0,100,100)
    plt.plot(x, h_values)
    plt.grid()

    plt.show()

main()