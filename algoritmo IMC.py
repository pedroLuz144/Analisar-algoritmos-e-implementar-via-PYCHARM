def calcular_imc(peso, altura): #define uma funcao que ira receber os valores de duas variaveis

    imc = peso / (altura ** 2) #variavel "imc" recebe a variavel "peso" divida pela variavel "altura" que é multiplicada por dois
    return imc #retorna o valor de imc para a funçao

def classificar_imc(imc): #define uma funcao que ira receber os valores de uma variavel

    if imc < 18.5: #inicia um laço de repetiçao; caso a variavel imc retorne um valor abaixo do predefinido, esse laço ira retornar o valor estabelecido para ele para a funçao
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9: #caso a variavel imc retorne um valor maior ou igual do predefinido, ou menor do que o predefinido esse laço ira retornar o valor estabelecido para ele para a funçao
        return "Peso normal"
    elif 25 <= imc < 29.9: #caso a variavel imc retorne um valor maior ou igual do predefinido, ou menor do que o predefinido esse laço ira retornar o valor estabelecido para ele para a funçao
        return "Sobrepeso"
    elif 30 <= imc < 34.9: #caso a variavel imc retorne um valor maior ou igual do predefinido, ou menor do que o predefinido esse laço ira retornar o valor estabelecido para ele para a funçao
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9: #caso a variavel imc retorne um valor maior ou igual do predefinido, ou menor do que o predefinido esse laço ira retornar o valor estabelecido para ele para a funçao
        return "Obesidade grau 2"
    else: #caso nenhum dos laços anteriores tenham tido seus requisitos sanados, ira retornar o resultado deste ultimo laço
        return "Obesidade grau 3"

def sugestao_atividade_fisica(classificacao_imc): #define uma funcao que ira receber os valores de uma variavel

    if classificacao_imc == "Abaixo do peso": #inicia um laço de repetiçao; caso a variavel "classificacao_imc" retorne um valor igual ao predefinido, esse laço ira retornar o valor estabelecido para ele para a funçao
        return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em proteínas e calorias."
    elif classificacao_imc == "Peso normal": #caso a variavel "classificacao_imc" retorne um valor igual ao predefinido, esse laço ira retornar o valor estabelecido para ele para a funçao
        return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e natação, junto a um treino de força moderado."
    elif classificacao_imc == "Sobrepeso": #caso a variavel "classificacao_imc" retorne um valor igual ao predefinido, esse laço ira retornar o valor estabelecido para ele para a funçao
        return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além de exercícios de resistência."
    elif classificacao_imc == "Obesidade grau 1": #caso a variavel "classificacao_imc" retorne um valor igual ao predefinido, esse laço ira retornar o valor estabelecido para ele para a funçao
        return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um programa de reeducação alimentar."
    elif classificacao_imc == "Obesidade grau 2": #caso a variavel "classificacao_imc" retorne um valor igual ao predefinido, esse laço ira retornar o valor estabelecido para ele para a funçao
        return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e acompanhamento nutricional."
    else: #caso nenhum dos laços anteriores tenham tido seus requisitos sanados, ira retornar o resultado deste ultimo laço
        return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica, fisioterapia, e consultas regulares com um nutricionista."

peso = float(input("Digite seu peso (em kg): ")) #variavel vai receber um valor do tipo "real" que vai ser inserido pelo usuario do software
altura = float(input("Digite sua altura (em metros): ")) #variavel vai receber um valor do tipo "real" que vai ser inserido pelo usuario do software

imc = calcular_imc(peso, altura) #variavel recebe o valor dela a partir do retorno da funçao
classificacao_imc = classificar_imc(imc) #variavel recebe o valor dela a partir do retorno da funçao
sugestao = sugestao_atividade_fisica(classificacao_imc) #variavel recebe o valor dela a partir do retorno da funçao

print(f"Seu IMC é: {imc:.2f}") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel entre chaves
print(f"Classificação: {classificacao_imc}") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel entre chaves
print(f"Sugestão de atividade física: {sugestao}") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel entre chaves