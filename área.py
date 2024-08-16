def calcular_area_comodos(): #define uma nova função
    total_area = 0 #define a variavel com o valor de 0

    while True: #abre um laço de repetição no codigo

        largura = float(input("Digite a largura do cômodo (em metros): ")) #variavel vai receber um valor do tipo "real" que vai ser inserido pelo usuario do software
        comprimento = float(input("Digite o comprimento do cômodo (em metros): ")) #variavel vai receber um valor do tipo "real" que vai ser inserido pelo usuario do software

        area_comodo = largura * comprimento # variavel recebe outras duas variaveis, sendo uma multiplicada pela outra
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.") #"imprime" no terminal o que esta entre aspas mais o valor da variavel dentre as chaves

        total_area += area_comodo #a variavel recebe ela mesma somada com outra variavel

        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()#variavel vai receber um valor do tipo "string" que vai ser inserido pelo usuario do software
        if mais_comodos != 's': #se na linha de código anterior o usuario inserir uma letra diferente de "s", o laço se termina
    break #determina o final do laço de repetição

    return total_area #retorna o novo valor da variavel da area total

area_total = calcular_area_comodos() #a variavel recebe o resultado da funcao
print(f"A área total da casa é: {area_total:.2f} metros quadrados.") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel "area_total"