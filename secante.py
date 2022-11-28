# Aluno: Alex Davis Neuwiem da Silva
# Matrícula: 21202103

import math

def func(x): #----------------------- Definição da função
    y = math.exp(x) - 2* math.cos(x)
    return y

print('\n')
print('---------- Método da Secante ----------')
print('\n')

x0 = 0 #---------------------------------------------- Definição do x0
x = 2 #----------------------------------------------- Definição do x
p = 6 #----------------------------------------------- Precisão da raiz
k = 0 #----------------------------------------------- Variável para o cálculo de iterações

while( abs(func(x)) > 10**-p): #---------------------- Verificação da precisão
    aux = x
    x = x - ((x-x0)*func(x)/(func(x)-func(x0)))
    x0 = aux
    k += 1
    

print('Aproximação de x: {}'.format(x))
print('Aproximação de f(x): {}'.format(func(x)))
print('Total de iterações: {}'.format(k))