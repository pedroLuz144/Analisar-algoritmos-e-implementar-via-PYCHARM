def calcular_media_e_aprovacao(notas, nota_minima_aprovacao): #define uma funcao que ira receber os valores de duas variaveis
    total_notas = 0 #variavel recebe o valor de 0
    num_alunos = len(notas) #variavel recebe o valor de outra variavel
    aprovados = [] #define uma variavel vetor, que podera receber mais de um resultado
    reprovados = [] #define uma variavel vetor, que podera receber mais de um resultado

    for aluno, nota in notas.items(): #inicia um laço de repetiçao
        total_notas += nota #variavel recebe ela mesma somando com outra variavel
        if nota >= nota_minima_aprovacao: #laço onde se a variavel "nota" for maior ou igual a variavel "notaMinima", ira inserir o aluno na variavel vetor de "aprovados"
            aprovados.append(aluno)
        else: #caso a variavel "nota" nao atenda ao requisito do laço anterior, ira inserir o aluno na variavel vetor de "reprovados"
            reprovados.append(aluno)

    media_turma = total_notas / num_alunos #variavel recebe duas variaves sendo uma dividida pela outra

    return media_turma, aprovados, reprovados #retorna os valores encontrados durante a funçao

notas = { #dentro dessas chaves sao exibidas as notas que foram analisadas na funçao anterior
    "Alice": 85,
    "Bruno": 72,
    "Carlos": 60,
    "Diana": 95,
    "Eduardo": 55
}

nota_minima_aprovacao = 70 #define o valor da varivael "notaMinima"

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao) #variaveis recebem o valor delas a partir do retorno da funçao

print(f"Média da turma: {media_turma:.2f}") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel entre chaves
print(f"Alunos aprovados: {', '.join(aprovados)}") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel entre chaves
print(f"Alunos reprovados: {', '.join(reprovados)}") #"imprime" no terminal o que foi apresentado entre aspas junto do valor da variavel entre chaves