def contadordevelocidade():
    velocidade = 50
    contador = 0
    print("Olá")
    while contador <10 and velocidade >=0 and velocidade <=100:
        print (f"velocidade atual= {velocidade} Km")
        op = input("deseja aumentar (A) ou dimunir a velocidade (D)").strip().upper()
        if op == "A":
            velocidade +=10
        elif op == "D":
            velocidade -=10
        else:
            print("Escolha invalida, tente novamente.")
            continue
        contador += 1
        if velocidade <= 0:
            print(f"Operação Finalizada, A velocidade chegou a 0 Km")
        elif velocidade >= 100:
            print(f"Operação Finalizada, A velocidade chegou a 100 Km")
        else:
            print(f"Operação Finalizada,"
                  f" A velocidade Não Atingiu o Limite, Velociade está há {velocidade} Km")

contadordevelocidade()