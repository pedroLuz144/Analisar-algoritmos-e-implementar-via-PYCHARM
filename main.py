def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso): #estabelece uma "classe" que leva consigo as atribuicoes o valor principal, a taxa de juros anual e o dias de atraso
    taxa_juros_diaria = taxa_juros_anual / 365 / 100 #a variavel "taxa_juros_diaria" recebe o valor da variavel "taxa_juros_anual" dividida por 365 que e dividada por 100

    juros = valor_principal * taxa_juros_diaria * dias_atraso #a variavel juros recebe o valor da variavel "valor_principal" multiplicada pela "taxa_juros_diaria" multiplicada pela "dia_atraso"

    valor_total = valor_principal + juros #a variavel "valor_total" recebe o valor da variavel "valor_principal" somada com a variavel "juros"
    return valor_total, juros #

valor_principal = 1000.00 #variavel "valor_principal" recebe o valor de 1000.00
taxa_juros_anual = 5.0 #variavel "taxa_juros_anual" recebe o valor de 5.0
dias_atraso = 30 #variavel "dias_atraso" recebe o valor de 30
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso) #
print(f"Valor total a ser pago: R${valor_total:.2f}") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel "valor_total"
print(f"Valor dos juros: R${juros:.2f}") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel "valor_total"