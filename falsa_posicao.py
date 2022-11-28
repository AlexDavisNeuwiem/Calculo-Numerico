# Aluno: Alex Davis Neuwiem da Silva
# Matrícula: 21202103

import math

def func(x): #----------------------- Definição da função
    y = math.exp(x) - 2* math.cos(x)
    return y

print('\n')
print('---------- Método da Falsa Posição Original ----------')
print('\n')

a = 0 #------------------------------ Menor valor do intervalo inicial
b = 2 #------------------------------ Maior valor do intervalo inicial
p = 6 #------------------------------ Precisão da raiz
x_k = 1 #---------------------------- Valor inicial da média
k = 0 #------------------------------ Variável para o cálculo de iterações

while( abs(func(x_k)) > 10**-p): #------------------------------- Verificação da precisão
    x_k = a - (func(a)*(b-a)/(func(b)-func(a))) #-------------- Atualização do x_m
    k += 1
    
    if (func(a) * func(x_k) < 0): #------------------------------- Verificação do intervalo da raiz
        b = x_k
    elif (func(b) * func(x_k) < 0):
        a = x_k

print('Aproximação de x: {}'.format(x_k))
print('Aproximação de f(x): {}'.format(func(x_k)))
print('Total de iterações: {}'.format(k))

#------------------------------------------------------------------------------------------------------------------#

print('\n')
print('---------- Método da Falsa Posição Modificado ----------')
print('\n')

a = 0 #------------------------------ Menor valor do intervalo inicial
b = 2 #------------------------------ Maior valor do intervalo inicial
p = 6 #------------------------------ Precisão da raiz
x_k = 1 #---------------------------- Valor inicial da média
k = 0 #------------------------------ Variável para o cálculo de iterações
fa = func(a)
fb = func(b)

while( abs(func(x_k)) > 10**-p): #------------------------------- Verificação da precisão
    x_k = a - (fa*(b-a)/(fb-fa)) #-------------- Atualização do x_m
    k += 1
    
    if (fa * func(x_k) < 0): #------------------------------- Verificação do intervalo da raiz
        b = x_k
        pa = func(b)/(func(b)+func(x_k))
        fa = func(a)*pa
        fb = func(x_k)
    elif (fb * func(x_k) < 0):
        a = x_k
        pb = func(a)/(func(a)+func(x_k))
        fa = func(x_k)
        fb = func(b)*pb
        
print('Aproximação de x: {}'.format(x_k))
print('Aproximação de f(x): {}'.format(func(x_k)))
print('Total de iterações: {}'.format(k))