def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios, custo_pedagio):#define uma funcao que ira receber os valores de algumas variaveis

    custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel #variavel recebe a variavel "distancia" dividida pela variavel "custoCombustivel" e ambas sendo multiplicadas pela variavel "custo_combustivel"

    custo_pedagio_total = numero_pedagios * custo_pedagio #variavel recebe o valor de duas variaveis, sendo uma multiplicada pela outra

    custo_total = custo_combustivel_total + custo_pedagio_total #variavel recebe o valor de duas variaveis, sendo uma somada com a outra

    return custo_total, custo_combustivel_total, custo_pedagio_total #retorna os valores das variaveis para a funçao

distancia = float(input("Digite a distância da viagem (em km): ")) #variavel vai receber um valor do tipo "real" que vai ser inserido pelo usuario do software
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): ")) #variavel vai receber um valor do tipo "real" que vai ser inserido pelo usuario do software
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): ")) #variavel vai receber um valor do tipo "real" que vai ser inserido pelo usuario do software
numero_pedagios = int(input("Digite o número de pedágios no percurso: ")) #variavel vai receber um valor do tipo "inteiro" que vai ser inserido pelo usuario do software
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): ")) #variavel vai receber um valor do tipo "real" que vai ser inserido pelo usuario do software

custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios, custo_pedagio) #variaveis recebem o valor delas a partir do retorno da funçao

print(f"Custo total da viagem: R${custo_total:.2f}") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel entre chaves
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel entre chaves
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel entre chaves