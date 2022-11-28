# Aluno: Alex Davis Neuwiem da Silva
# Matrícula: 21202103

import math

print('\n')
print('---------- Método das Diferenças Divididas de Newton ----------')
print('\n')

# Função que retorna o valor de g(x) no ponto V ----------------------------#
                                                                            #
def difdiv(x, y, v):                                                        #
                                                                            #
    # Instanciando N                                                        #
    n = len(x)                                                              #
                                                                            #
    # Instanciando a matriz A                                               #
    a = [[0 for i in range(n)] for j in range(n)]                           #
                                                                            #
    # Atribuindo os valores de Y à primeira coluna de A                     #
    for k in range(n) :                                                     #
        a[k][0] = y[k]                                                      #
                                                                            #
    # Calculando a matriz de diferenças divididas A                         #
    for j in range(1, n) :                                                  #
        for i in range(j, n) :                                              #
            a[i][j] = (a[i][j - 1] - a[i - 1][j - 1]) / (x[i] - x[i - j])   #
                                                                            #
    # Calculando o valor do polinômio P no ponto V                          #
    p = 0.0                                                                 #
    for i in range(n) :                                                     #
        aux = 1.0                                                           #
        for j in range(0, i) :                                              #
            aux = aux*(v - x[j])                                            #
        p = p + a[i][i]*aux                                                 #
                                                                            #
    return p                                                                #
                                                                            #
#---------------------------------------------------------------------------#


# Vetores dos pontos tebelados -#
                                #
x = [0.0, 1.0, 2.0, 3.0]        #
y = [-3.0, -2.0, 4.0, 0.0]      #
                                #
#-------------------------------#


# Vetores dos pontos não tabelados -#
                                    #
xx = []                             #
yy = []                             #
                                    #
#-----------------------------------#


# Valor do ponto a ser interpolado -------------------------#
                                                            #
v = 2.5                                                     #
                                                            #
p = difdiv(x, y, v)                                         #
                                                            #
print("VALOR DE g(x) NO PONTO 2.5:")                        #
                                                            #
print("g({}) = {}".format(v, p))                            #
                                                            #
#-----------------------------------------------------------#


# Valores dos pontos tabelados -----------------------------#
                                                            #
print("\nVALORES DOS PONTOS TABELADOS:")                    #
                                                            #
for i in range(0, 4):                                       #
    v = i                                                   #
    p = difdiv(x, y, v)                                     #
    print("g({}) = {}".format(v, p))                        #
                                                            #
#-----------------------------------------------------------#


# Valores de outros pontos ---------------------------------#
                                                            #
print("\nVALORES DE OUTROS PONTOS:")                        #
                                                            #
for i in range(-10, 11):                                    #
    v = i                                                   #
    xx.append(v)                                            #
    p = difdiv(x, y, v)                                     #
    yy.append(p)                                            #
    print("g({}) = {}".format(v, p))                        #
                                                            #
#-----------------------------------------------------------#


'''

#   OBS: O trecho a seguir fará o plot do gráfico com base nos pontos calculados
# no "for" da linha 87. Para realizar esse plot, primeiro é necessário instalar 
# a biblioteca "matplotlib" e descomentar as linhas 97 e 120.

import matplotlib.pyplot as plt

# Plotando os pontos 
plt.plot(xx, yy)
  
# Dando nome ao eixo X
plt.xlabel('Eixo x')

# Dando nome ao eixo Y
plt.ylabel('Eixo y')
  
# Dando nome ao gráfico
plt.title('Interpolação pelo método das Diferenças Divididas')
  
# Mostrando o gráfico
plt.show()

'''
