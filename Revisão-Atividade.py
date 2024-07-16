# nome = input("Digite seu nome")
# empresa = input("Digite o nome da empresa")
# codbarra = int(input("Digite o codigo de barra"))
# sabor = input("Digite o sabor")
# kcal = float(input("Digite as calorias"))
# volume = float(input("Digite o volume"))
# desine = input("Digite como é seu desine")
# fabricacao = input("Digite sua data de fabricação")
# validade = input("Digite sua data de validade")
# receita = input("Digite como é sua receita")
# arm = input("Digite como é feito seu armazenamento")
# embalagem = input("Digite como é feito sua embalagem")
# preco = float(input("Digite qual é seu preço"))
# transporte = input("Digite como é feito seu transporte")
#
#
# print(f'seu nome é: {nome}')
# print(f'sua empresa é: {empresa}')
# print(f'seu codigo de barras é: {codbarra}')
# print(f'seu sabor é: {sabor}')
# print(f'suas calorias são: {kcal}')
# print(f'seu volume é: {volume}')
# print(f'seu desine é: {desine}')
# print(f'sua data de fabricação é: {fabricacao}')
# print(f'sua data de validade é: {validade}')
# print(f'sua receita é: {receita}')
# print(f'seu armezanamento é feito dessa forma: {arm}')
# print(f'seu preço é: {preco}')
# print(f'sua embalagem é feita assim: {embalagem}')
# print(f'seu transporte é feito assim: {transporte}')

print("Boa tarde, seja bem vindo a nossa loja")
limite = 2500
senha = 1234
produto = input("Digite o nome do seu produto:")
valor = float(input("Digite o valor do seu produto:"))
forma = int(input("Digite sua forma de pagamento: \n [1] Dinheiro \n [2] Credito \n [3] Débito \n [4] Pix \n"))
if forma == 1:
    din = float(input("Qual o valor dado em especie:"))
    if(din > valor):
        print("Parabens pela sua compra, seu troco é de ", din - valor)
    elif(din == valor):
        print("Parabens pela compra, até a proxima")
    else:
        print("Eiiiiiita bixo pobre tá necessitando de uma cesta basica, te manca e vai embora")
elif forma == 2:
    tsenha = int(input("Digite sua senha:"))
    if tsenha==senha:
        print("Voçê pode continuar a fazer sua compra")
        if(limite >= valor):
            op = input("Deseja parcelar sua compra? S - Sim ou N - Não")
            if(op == 'N'):
                print("Parabens pela sua compra, seu saldo atual é ", limite - valor)
            elif(op == 'S'):
                nparcela = int(input("Digite em quantas vezes quer parcelar?"))
                print("Parabens pela sua compra, a parcela foi de ", valor/nparcela)
            else:
                print("Digite um valor valido")
        else:
            print("Saldo insuficiente")
    else:
        print("Sua senha está incorreta")
elif forma == 3:
    rsenha = int(input("Digite sua senha:"))
    if rsenha == senha:
        print("Voçê pode continuar a fazer sua compra")
        if(limite >= valor):
            print("Parabens pela sua compra, seu saldo atual é ", limite - valor)
        else:
            print("Saldo insuficiente")
    else:
        print("Sua senha está incorreta")
elif forma == 4:
    piz = float(input("Digite o saldo do seu pix que sera passado:"))
    if(piz > valor):
        print("Parabens pela sua compra, seu saldo atual é de ", piz - valor)
    elif(piz == valor):
        print("Parabens pela compra, até a proxima")
    else:
        print("Saldo insuficiente")
else:
    print("Erro: por favor tente novamente")
print("COMPRA FINALIZADA!, OBRIGADO E VOLTE SEMPRE (^-^)")