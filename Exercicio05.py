#Ler 10 valores e escrever quantos desses valores são Negativos!
Neg = 0
for X in range(10):
    Num = int(input("Digite 10 Números: "))

    if Num < 0:
        Neg = Neg + 1

print(Neg, end=" ") 