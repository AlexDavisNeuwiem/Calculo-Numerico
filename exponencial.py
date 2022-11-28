# Aluno: Alex Davis Neuwiem da Silva
# Matrícula: 21202103

x = 2 #------------------------------ Valor escolhido para x
p = 6 #------------------------------ Precisão do resultado
i = 1 #------------------------------ Variável auxiliar do fatorial (índice)
sum_parc = float(0) #---------------- Soma Parcial (para comparação com o valor da precisão)
sum_total = pot = fat = float(1) #--- Valores iniciais das variáveis Soma Acumulada, Potência e Fatorial

while (abs(sum_total - sum_parc) > 10**(-p)): #--- Verificação da Precisão
    pot = pot*x
    fat = fat*i
    sum_parc = sum_total
    sum_total = sum_parc + (pot/fat)
    i += 1

print('Resultado aproximado: {}'.format(sum_total))