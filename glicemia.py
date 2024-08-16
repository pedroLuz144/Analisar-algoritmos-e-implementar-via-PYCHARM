def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial): #define uma funcao que ira receber os valores de duas variaveis

    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200: #define um laço de repetição, onde se os valores inseridos de cada variavel for igual ou maior ao predefinido, ela retornara o resultado deste laço
        return "Diabetes" #retorna o "valor" para a funcao
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200: #define um laço de repetição, onde se os valores inseridos de cada variavel for igual ou maior ao predefinido, ou menor que o valor predefinido, ela retornara o resultado deste laço
        return "Pré-diabetes" #retorna o "valor" para a funcao
    else: #se não atender nenhum dos requisitos dos laços anteriores retornara o proximo valor
        return "Normal" #retorna o "valor" para a funcao

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): ")) #variavel vai receber um valor do tipo "real" que vai ser inserido pelo usuario do software
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): ")) #variavel vai receber um valor do tipo "real" que vai ser inserido pelo usuario do software

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial) #a variavel recebe o resultado da funcao
print(f"O diagnóstico é: {resultado}") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel entre chaves