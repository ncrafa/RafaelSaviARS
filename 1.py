#2) (4.0) Criação de um simulador de caixa eletrônico.
#A. Você deve perguntar ao usuário qual será o valor para ser sacado (Apenas números inteiros)
#B. O programa deve informar quantas cédulas de cada valor deverá ser entregue ao usuário
#C. As cédulas deveram ser nos valores de R$50, R$20, R$ 10 e R$ 1.
#D. Devem também fazer na letra A as verificações de erros possíveis

#Sora desculpa, mas não consegui concluir a logíca do exercício :( . Me encuquei com essa k
valor = int(input("qual o valor a ser sacado ?"))
 
while valor > 50:
    if   valor > 50 and valor%50 == 0:
        cinquenta = valor/50
        print("Você receberá ",cinquenta,"notas de cinquenta")
        valor = 0
    if   valor > 50 and valor%50 > 0:
        cinquenta = valor/50
        a = valor%50
while valor > 20:
    if   valor > 20 and valor%20 == 0:
        a = a/20
        print("Você receberá ",cinquenta,"notas de cinquenta e ",a,"notas de 20")
        valor = 0
    if   valor > 20 and valor%20 > 0:
        vinte = a/20
        b = a%20
while valor >10:        
    if   valor > 10 and valor%10 == 0:
         dez = b/10
         print("Você receberá ",cinquenta,"notas de cinquenta,",a,"notas de 20 e ",dez,"notas de 10 reais" )
         valor = 0
    if   valor > 10 and valor%10 > 0:
        dez = b/5
        c = b%5
while valor > 5:
    if   valor > 5 and valor%5 == 0:
        valorCinco = c/5 
        print("Você receberá ",cinquenta,"notas de cinquenta,",a,"notas de 20, ",dez,"notas de 10 e ",c,"de 5 reais" )
        valor = 60
    if valor > 5 and valor%5 > 0:
        valorUm = c/5
        d = c%1
        print("Você receberá ",cinquenta,"notas de cinquenta,",a,"notas de 20, ",dez,"notas de 10 e ",c,"de 5 reais e ",d,"notas de 1 real" )
valor = 0
