#Ler um Valor e Imprimir todos o valores Maiores que 0 até ele.
Num = int(input("Digite um Número: "))

if Num > 0:
    for X in range(1,Num +1):
        print(X)
else:
        print("NÚMERO INVÁLIDO!")   