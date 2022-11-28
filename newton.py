# Aluno: Alex Davis Neuwiem da Silva
# Matrícula: 21202103

import math

def func(x): #----------------------- Definição da função
    y = math.exp(x) - 2* math.cos(x)
    return y

def deriv(x): #---------------------- Definição da derivada da função
    y = math.exp(x) + 2* math.sin(x)
    return y

print('\n')
print('---------- Método de Newton ----------')
print('\n')

x = 1 #---------------- Definição do x
p = 6 #---------------- Precisão da raiz
k = 0 #---------------- Variável para o cálculo de iterações

while( abs(func(x)) > 10**-p): #----- Verificação da precisão
    x = x - func(x)/deriv(x) #---- Atualização do x
    k += 1
    

print('Aproximação de x: {}'.format(x))
print('Aproximação de f(x): {}'.format(func(x)))
print('Total de iterações: {}'.format(k))