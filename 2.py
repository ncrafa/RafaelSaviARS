#Criação de um simulador de preço.
#A. Você deve perguntar ao cliente o preço do produto.
#B. Você deve perguntar em seguida a forma de pagamento com as opções a vista, a prazo sendo 1x
#no cartão, a prazo da loja em 5x, a prazo da loja em 10x.
#C. A vista o produto sairá 50% a menos do valor.
#D. A prazo em 1x no cartão o produto sairá 10% a menos do valor.
#E. A prazo da loja em 5x o produto sairá 10% a mais do valor.
#F. A prazo da loja em10x o produto sairá 50% a mais do valor.
#G. Você deve mostrar ao cliente preço do produto com as taxas.
#H. As questões a prazo, você deverá mostrar também os valores de cada parcela.


def opcoes():
    escolha = 1
    produtos  =  ["bicicleta","boneca","luminaria"]
    bicicleta  =  1
    boneca  = 2
    luminaria  =  3
    valorBike = 1000
    valorBoneca = 200
    valorLuminaria = 450
    while  escolha  ==  1 :
        print ( "Digite 1 para bicileta" )
        print ( "Digite 2 para  boneca" )
        print ( "Digite 3 para luminaria " ) 
        print ("Digite 4 para sair")          
        operacao  =  int ( input ( "Deseja realizar qual operação:"))
        if operacao ==4:
            print("Volte sempre!!!")
            escolha = 0
        if  operacao  ==  1 :
            print("O preço do produto é de R$ ",valorBike)
            comprar  =  int ( input ( "Deseja ver as informações para compra?\n 1 - Sim desejo! \n 2- Não,obrigado!" ))
            while  comprar  == 1:
                opcaoCompra= int(input("Você tem as seguintes opções\n 101 - A vista \n 102 - A prazo sendo 1x no cartão \n 103 - A prazo da loja em 5x\n 104 - A prazo da loja em 10x \n OBS: A vista o produto sairá 50% a menos do valor \n A prazo em 1x no cartão o produto sairá 10% a menos do valor \n A prazo da loja em 5x o produto sairá 10% a mais do valor \n A prazo da loja em 10x o produto sairá 50% a mais do valor \n Como deseja realizar a compra? " ))
                if opcaoCompra == 101:
                    valorPagar = 1000*0.5
                    print("o valor total a pagar será de ",valorPagar)
                if opcaoCompra == 102:
                    valorPagar = 1000*0.10
                    print("o valor total a pagar será de ",valorPagar)
                if opcaoCompra == 103:
                    valorPagar = 1000 + (1000*0.10)
                    parcelas = valorPagar/5
                    print("o valor total a pagar será de ",valorPagar,"com 5 parcelas de R$",parcelas)
                if opcaoCompra == 104:
                    valorPagar = 1000 + (1000*0.50)
                    parcelas = valorPagar/10
                    print("o valor total a pagar será de ",valorPagar,"com 10 parcelas de R$",parcelas)
                comprar = 0
                escolha = 0
        if  operacao  ==  2 :
            print("O preço do produto é de R$",boneca)
            comprar  =  int ( input ( "Deseja ver as informações para compra?\n 1 - Sim desejo! \n 2- Não,obrigado!" ))
            while  comprar  == 1:
                opcaoCompra= int(input("Você tem as seguintes opções\n 101 - A vista \n 102 - A prazo sendo 1x no cartão \n 103 - A prazo da loja em 5x\n 104 - A prazo da loja em 10x \n OBS: A vista o produto sairá 50% a menos do valor \n A prazo em 1x no cartão o produto sairá 10% a menos do valor \n A prazo da loja em 5x o produto sairá 10% a mais do valor \n A prazo da loja em 10x o produto sairá 50% a mais do valor \n Como deseja realizar a compra? " ))
                if opcaoCompra == 101:
                    valorPagar1 = 200*0.5
                    print("o valor total a pagar será de ",valorPagar1)
                if opcaoCompra == 102:
                    valorPagar1 = 200*0.10
                    print("o valor total a pagar será de ",valorPagar1)
                if opcaoCompra == 103:
                    valorPagar1 = 200 + (200*0.10)
                    parcelas = valorPagar1/5
                    print("o valor total a pagar será de ",valorPagar1,"com 5 parcelas de R$",parcelas)
                if opcaoCompra == 104:
                    valorPagar1 = 200 + (200*0.50)
                    parcelas = valorPagar1/10
                    print("o valor total a pagar será de ",valorPagar1,"com 10 parcelas de R$",parcelas)
                comprar = 0
                escolha=0
        if  operacao  ==  3 :
            print("O preço do produto é de R$",valorLuminaria)
            comprar  =  int ( input ( "Deseja ver as informações para compra?\n 1 - Sim desejo! \n 2- Não,obrigado!" ))
            while  comprar  == 1:
                opcaoCompra= int(input("Você tem as seguintes opções\n 101 - A vista \n 102 - A prazo sendo 1x no cartão \n 103 - A prazo da loja em 5x\n 104 - A prazo da loja em 10x \n OBS: A vista o produto sairá 50% a menos do valor \n A prazo em 1x no cartão o produto sairá 10% a menos do valor \n A prazo da loja em 5x o produto sairá 10% a mais do valor \n A prazo da loja em 10x o produto sairá 50% a mais do valor \n Como deseja realizar a compra? " ))
                if opcaoCompra == 101:
                    valorPagar2 = 450*0.5
                    print("o valor total a pagar será de ",valorPagar2)
                if opcaoCompra == 102:
                    valorPagar2 = 450*0.10
                    print("o valor total a pagar será de ",valorPagar2)
                if opcaoCompra == 103:
                    valorPagar2 = 450 + (450*0.10)
                    parcelas = valorBoneca/5
                    print("o valor total a pagar será de ",valorBoneca,"com 5 parcelas de R$",parcelas)
                if opcaoCompra == 104:
                    valorBoneca = 450 + (450*0.50)
                    parcelas = valorBoneca/10
                    print("o valor total a pagar será de ",valorBoneca,"com 10 parcelas de R$",parcelas)
                comprar = 0
                escolha=0
opcoes()              


  
              


  
              




              











