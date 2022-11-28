# Aluno: Alex Davis Neuwiem da Silva
# Matrícula: 21202103

import math

def func(x): #----------------------- Definição da função
    y = math.exp(x) - 2* math.cos(x)
    return y

print('\n')
print('---------- Método da Bisseção ----------')
print('\n')

a = 0 #------------------------------ Menor valor do intervalo inicial
b = 2 #------------------------------ Maior valor do intervalo inicial
p = 6 #------------------------------ Precisão da raiz
x_m = 1 #---------------------------- Valor inicial da média
k = 0 #------------------------------ Variável para o cálculo de iterações

while( abs(func(x_m)) > 10**-p): #--- Verificação da precisão
    x_m = (a + b) / 2 #-------------- Atualização do x_m
    k += 1
    
    if(func(a) * func(x_m) < 0): #--- Verificação do intervalo da raiz
        b = x_m
    else:
        a = x_m

print('Aproximação de x: {}'.format(x_m))
print('Aproximação de f(x): {}'.format(func(x_m)))
print('Total de iterações: {}'.format(k))