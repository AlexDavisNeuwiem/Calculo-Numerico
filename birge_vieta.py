# Aluno: Alex Davis Neuwiem da Silva
# Matrícula: 21202103

import math

def func(x):
    y = x**3 + 2*x - 1
    return y

a = [1, 0, 2, -1] #------------ Polinômio de exemplo

print('\n')
print('---------- Método de Birge Vieta ----------')
print('\n')

x = 1 #---------------- Definição do x
p = 8 #---------------- Precisão da raiz
k = 0 #---------------- Variável para o cálculo de iterações
b = c = 1

while( abs(func(x)) > 10**-p): #----- Verificação da precisão
    for i in range(len(a) - 1):
        b = b*x + a[i]
        c = c*x + b
    b = b*x + a[len(a) - 1]
    x = x - b/c
    k += 1
    
print('Aproximação de x: {}'.format(x))
print('Aproximação de f(x): {}'.format(func(x)))
print('Total de iterações: {}'.format(k))

#-------------------------------------------------------------------------------------------#

def deriv(x): #---------------------- Definição da derivada da função
    y = 3*(x**2) + 2
    return y

print('\n')
print('---------- Método de Newton ----------')
print('\n')

x = 1 #---------------- Definição do x
p = 8 #---------------- Precisão da raiz
k = 0 #---------------- Variável para o cálculo de iterações

while( abs(func(x)) > 10**-p): #----- Verificação da precisão
    x = x - func(x)/deriv(x) #---- Atualização do x
    k += 1
    

print('Aproximação de x: {}'.format(x))
print('Aproximação de f(x): {}'.format(func(x)))
print('Total de iterações: {}'.format(k))