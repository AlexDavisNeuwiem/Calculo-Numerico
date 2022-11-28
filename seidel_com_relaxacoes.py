# Aluno: Alex Davis Neuwiem da Silva
# Matrícula: 21202103

import math

print('\n')
print('---------- Método de Gauss-Seidel sem Relaxações ----------')
print('\n')

a = [[62.0, 24.0, 1.0, 8.0, 15.0], [23.0, 50.0, 7.0, 14.0, 16.0], [4.0, 6.0, 58.0, 20.0, 22.0], [10.0, 12.0, 19.0, 66.0, 3.0], [11.0, 18.0, 25.0, 2.0, 54.0]]
b = [110.0, 110.0, 110.0, 110.0, 110.0]

x = [0.0, 0.0, 0.0, 0.0, 0.0]
x0 = [0.0, 0.0, 0.0, 0.0, 0.0]

n = len(b)  # Tamanho de b
p = 10      # Precisão
k = 0       # Número de iterações

dx = 1.0    # Diferença entre x e x0
w = 1.0     # Variável de Relaxação

# Verificando a Precisão -- #
                            #
while( dx > 10**-p):        #
                            #
#-------------------------- #

    # Atualização de x0 --- #
                            #
    for i in range(n):      #
        x0[i] = x[i]        #
                            #
    #---------------------- #

    # Método de Gauss-Seidel ------------------------------ #
                                                            #
    for i in range(n):                                      #
        soma = 0.0                                          #
        for j in range(n):                                  #
            if (j != i):                                    #
                soma = soma + (a[i][j] * x[j])              #
        x[i] = (1 - w)*x0[i] + w*((b[i] - soma) / a[i][i])  #
                                                            #
    #------------------------------------------------------ #

    # Cálculo do dx ------------------- #
                                        #
    dx = 0.0                            #
    for i in range(n):                  #
        if (abs(x[i] - x0[i]) > dx):    #
            dx = abs(x[i] - x0[i])      #
                                        #
    # --------------------------------- #

    k += 1

print('         X     =  {}'.format(x))
print('     Precisão  =  {}'.format(dx))
print('     Iterações =  {}'.format(k))
print('         W     =  {}'.format(w))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------#

print('\n')
print('---------- Método de Gauss-Seidel com Relaxações ----------')
print('\n')

a = [[62.0, 24.0, 1.0, 8.0, 15.0], [23.0, 50.0, 7.0, 14.0, 16.0], [4.0, 6.0, 58.0, 20.0, 22.0], [10.0, 12.0, 19.0, 66.0, 3.0], [11.0, 18.0, 25.0, 2.0, 54.0]]
b = [110.0, 110.0, 110.0, 110.0, 110.0]

x = [0.0, 0.0, 0.0, 0.0, 0.0]
x0 = [0.0, 0.0, 0.0, 0.0, 0.0]

n = len(b)  # Tamanho da matriz b
p = 10      # Precisão
k = 0       # Número de iterações

dx = 1.0    # Diferença entre x e x0
w = 1.0562  # Variável de Relaxação

# Verificando a Precisão -- #
                            #
while( dx > 10**-p):        #
                            #
#-------------------------- #

    # Atualização de x0 --- #
                            #
    for i in range(n):      #
        x0[i] = x[i]        #
                            #
    #---------------------- #

    # Método de Gauss-Seidel ------------------------------ #
                                                            #
    for i in range(n):                                      #
        soma = 0.0                                          #
        for j in range(n):                                  #
            if (j != i):                                    #
                soma = soma + (a[i][j] * x[j])              #
        x[i] = (1 - w)*x0[i] + w*((b[i] - soma) / a[i][i])  #
                                                            #
    #------------------------------------------------------ #

    # Cálculo do dx ------------------- #
                                        #
    dx = 0.0                            #
    for i in range(n):                  #
        if (abs(x[i] - x0[i]) > dx):    #
            dx = abs(x[i] - x0[i])      #
                                        #
    # --------------------------------- #

    k += 1

print('         X     =  {}'.format(x))
print('     Precisão  =  {}'.format(dx))
print('     Iterações =  {}'.format(k))
print('         W     =  {}'.format(w))


'''
----------------------------------- Conclusões -----------------------------------

a) Verificando a convergência do Sistema:

        Para conferir a eficiência desse método iterativo, nosso Sistema Linear 
    deve cumprir a principal condição de convergência: ser Diagonal Dominante.
        Um Sistema é Diagonal Dominante se os módulos dos elementos da diagonal
    principal forem iguais ou maiores que a soma dos módulos dos outros elemen-
    tos em cada linha e pelo menos um elemento da diagonal principal tem que ser
    maior que a soma dos outros elementos em uma linha.
        É importante ressaltar que ser Diagonal Dominante é uma condição sufici-
    ente, mas não necessária para que o método convirja. Ou seja, é possível ob-
    ter o resultado de um Sistema Linear mesmo ele não sendo Diagonal Dominante.
        Com isso, temos que:
        
            |A[0][0]| > |A[0][1]| + |A[0][2]| + |A[0][3]| + |A[0][4]|
            |A[1][1]| > |A[1][0]| + |A[1][2]| + |A[1][3]| + |A[1][4]|
            |A[2][2]| > |A[2][0]| + |A[2][1]| + |A[2][3]| + |A[2][4]|
            |A[3][3]| > |A[3][0]| + |A[3][1]| + |A[3][2]| + |A[3][4]|
            |A[4][4]| > |A[4][0]| + |A[4][1]| + |A[4][2]| + |A[4][3]|
        
        Ou seja:
        
            62 > 24 + 01 + 08 + 15   -->   62 > 48   -->   Verdadeiro
            50 > 23 + 07 + 14 + 16   -->   50 > 60   -->   Falso
            58 > 04 + 06 + 20 + 22   -->   58 > 52   -->   Verdadeiro
            66 > 10 + 12 + 19 + 03   -->   66 > 44   -->   Verdadeiro
            54 > 11 + 18 + 25 + 02   -->   54 > 56   -->   Falso
    
        Assim, percebemos que a matriz A não é Diagonal Dominante por causa de
    duas linhas que não satisfazem o critério da soma, porém isso não garante a 
    não-convergência do Sistema, apenas não podemos afirmar se ele convirgirá ou
    não.


b) Resultado do Método de Gauss-Seidel sem Relaxações:

                  1.000000000000361
        	      1.0000000000071956
        X     =	  1.0000000000177987
        	      0.9999999999950744
        	      0.9999999999894702
    
    Precisão  =   4.02569089175131e-11
    
    Iterações =   22


c) Conclusões a respeito do Método de Gauss-Seidel com Relaxações:

        Para encontrar o fator de relaxação ótimo, primeiramente foi necessário 
    verificar se esse seria um caso de Sub-Relaxação ou Sobrerrelaxação.
        Dessa forma, foi simples encontrar o caso de relaxação de nossa variável
    w, uma vez que  w = 1.1  nos garante  17  iterações enquanto  w = 0.9  apre- 
    senta  29  iterações. Ou seja, esse é um caso de Sobrerrelaxação.
        A seguir, foi preciso refinar w. Para fazer isso, o valor de  w  foi in-
    crementado de 0.01 até atinjir-se 16 iterações com w = 1.06. Nesse processo,
    observou-se que em qualquer ponto no intervalo 1.06 <= w <= 1.09, a quanti-
    dade de iterações se estabiliza em 16.
        Para refiná-lo ainda mais,  w  foi acrescido de  0.001  até chegarmos em 
    1.057  e depois acrescentou-se  0.0001  até encontrarmos  17  iterações em 
    w = 1.0561  e  16  iterações em  w = 1.0562. De maneira semelhante, foi pos-
    sível obter 16 iterações com 1.0925.
        Portanto, concluiu-se que o valor ótimo de w está em algum ponto no in-
    terválo  1.0561 < w < 1.0926  e, com isso, optou-se por utilizar  w = 1.0562 
    como fator de relaxação na realização deste trabalho.


----------------------------------------------------------------------------------
'''