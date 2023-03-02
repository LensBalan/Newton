#Autor: Leonardo Balan
#Newton.py

#O Método de Newton é uma técnica para aproximar uma solução para uma equação não-linear. 
#Ele é baseado no conceito de interpolação polinomial, onde a equação é aproximada por 
#uma função polinomial que passa por uma série de pontos dados.

#4 pontos, achar aproximação para f(x) dado x presente no intervalo de variação dos pontos

import numpy as np

#Função para o cálculo de Newton
def newton(x_vet, y_vet, x):
    
    # Determinando os coeficientes do polinômio
    coeficientes = np.zeros(len(x_vet))
    for i in range(len(x_vet)):
        coeficientes[i] = y_vet[i]
        for j in range(i):
            coeficientes[i] = (coeficientes[i] - coeficientes[j] * (x_vet[i] - x_vet[j])) / (x_vet[i] - x_vet[j])
    
    # Calculando o valor da função aproximada em x
    result = 0
    for i in range(len(x_vet) - 1, -1, -1):
        result = result * (x - x_vet[i]) + coeficientes[i]
    return result

# Exemplo de uso
x_vet = [0, 1, 3, 4]
y_vet = [0, 1, 27, 64]
x = 2
aproximacao = newton(x_vet, y_vet, x)
print("=== Aproximação para F(x) com x =",x,"===\n                F(x) =" , aproximacao)