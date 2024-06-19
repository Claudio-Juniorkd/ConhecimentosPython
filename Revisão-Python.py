#Algoritmo -> sequencia de passos para executar uma ação ou tarefa!

#3Estruturas possiveis no algoritmo:
#1 - Estrutura (Sequencia de passos continuos)
#2 - Condicional (DECISÃO- vou executar um script se acontecer X e outro se Y)
#3 - Repetição - permite executar varias vezes o mesmo codigo

#variaveis
#espaços de memoria que pode armazenar dados para a execução de um processo

#Int, Float, String e Boolean
#Int : Armazena valores inteiros (10, 14, 999...)
#Float : Numeros decimais (1.2, 1.4, 3.8... valores fracionais)
#String : Cadeia de caracteres: "Rua dos Bobos n 0" são valores literais, ou seja
#Não vou fazer calculos. Ex, Bruno, Gustavo
#Regras -> uma string deve estar entre "",'', "house's Fer"
#Boolean : é o poligrafo ele aceita dois valores true (verdadeiro) e false (falso)

#curso = Manufatura digital
#A Variavel "curso" recebe o valor "Manufatura Digital"
#print("Hi, I am Your Father!")

#para conversar com o usuário eu uso o input
#altura = float(input("Digite sua altura"))
#a variavel altura recebe um valor quebrado de altura

#print(f"sua altura é {altura}")
#exibe para mim "FORMARÇÃO" do texto com valor de uma variavel

#print("Cadastro De Uma Pessoa")
#nome = input("Digite seu nome")
#idade = int(input("Digite sua idade"))
#endereco = input("Digite um endereço")
#cpf = input("Digite seu CPF")
#distancia = input("Digite a distancia percorrida no dia")
#anoNascimento = input("Digite o ano do seu nascimento")
#print(nome, idade, endereco, cpf, distancia, anoNascimento)


#estrutura de algoritimo CONDICIONAL
#executo alguma instrução de acordo com os dados que tem. Por exemplo, só posso me alistar no exercito
#Se for maior idade
#Para usar o IF e Else, eu tenho que saber quais as opções que eu tenho!

nota = float(input("informe a nota 1"))
if(nota > 5):
    print("Você esta aprovado")
elif(nota== 5):
    print("Chama os pais, pq vc esta no conselho")
else:
    print("você esta reprovado")

#Se o salario for maior do que ue 1500 adicione 500
#Se o salario for maio rdo que 2000 some 400
#Se o salario for maior do que 3000 some 300


salario = float(input("Digite seu salario"))

if (salario>=1500):
    print(f"seu salario é {salario + 500}")
elif (salario>=2000):
    print(f"seu salario é {salario + 400}")
elif(salario>3000):
    print(f"seu salario é {salario + 300}") 
else: 
    print("você é pobre:(")