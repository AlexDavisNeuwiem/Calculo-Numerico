# Aluno: Alex Davis Neuwiem da Silva
# Matrícula: 21202103

import math

print('\n')
print('---------- Método de Gauss-Jacobi ----------')
print('\n')

a = [[3, -1, -1], [1, 3, 1], [2, -2, 4]]
b = [1, 5, 4]
x = [0, 0, 0]
x0 = [0, 0, 0]
n = len(b)
p = 6
k = 0
dx = 1

while( dx > 10**-p):
    
    for i in range(n):
        x0[i] = x[i]
    
    for i in range(n):
        soma = 0
        for j in range(n):
            if (j != i):
                soma = soma + (a[i][j] * x0[j])
        x[i] = (b[i] - soma) / a[i][i]
    
    dx = 0
    for i in range(n):
        if (abs(x[i] - x0[i]) > dx):
            dx = abs(x[i] - x0[i])
    
    k += 1

print('Aproximação de x: {}'.format(x))
print('Aproximação do erro: {}'.format(dx))
print('Total de iterações: {}'.format(k))