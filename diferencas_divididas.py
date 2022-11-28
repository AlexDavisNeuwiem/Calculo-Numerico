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


# Valor do ponto a ser interpolado -------------------------#
                                                            #
v = 2.5                                                     #
                                                            #
p = difdiv(x, y, v)                                         #
                                                            #
print("   VALOR DE g(x) NO PONTO 2.5:")                     #
                                                            #
print("      g({}) = {}".format(v, p))                      #
                                                            #
#-----------------------------------------------------------#


# Valores dos pontos tabelados -----------------------------#
                                                            #
print("\n   VALORES DOS PONTOS TABELADOS:")                 #
                                                            #
for i in range(0, 4):                                       #
    v = i                                                   #
    p = difdiv(x, y, v)                                     #
    print("      g({}) = {}".format(v, p))                  #
                                                            #
#-----------------------------------------------------------#


# Valores de outros pontos ----------------------------------------------------#
                                                                               #
print("\n   VALORES DE OUTROS PONTOS:")                                        #
                                                                               #
v = [0.0, 0.25, 0.50, 0.75, 1.0, 1.25, 1.50, 1.75, 2.0, 2.25, 2.50, 2.75, 3.0] #
p = []                                                                         #
                                                                               #
for num in v:                                                                  #
    p.append(difdiv(x, y, num))                                                #
                                                                               #
for i in range(len(v)):                                                        #
    print("      g({}) = {}".format(v[i], p[i]))                               #
                                                                               #
#------------------------------------------------------------------------------#


'''

#   OBS: O trecho a seguir fará o plot do gráfico com base nos pontos calculados
# no "for" da linha 82. Para realizar esse plot, primeiro é necessário instalar 
# a biblioteca "matplotlib" e descomentar as linhas 91 e 114.

import matplotlib.pyplot as plt

# Plotando os pontos 
plt.plot(v, p)
  
# Dando nome ao eixo X
plt.xlabel('Eixo x')

# Dando nome ao eixo Y
plt.ylabel('Eixo y')
  
# Dando nome ao gráfico
plt.title('Interpolação pelo método das Diferenças Divididas')
  
# Mostrando o gráfico
plt.show()

'''
