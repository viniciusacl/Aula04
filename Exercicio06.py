#Ler 10 valores e escrever quantos desses Valores estão dentro e fora do Intervalo [10,20]!
Fora = 0
Intervalo = 0

for X in range(10):
    Num = int(input("Digite um Número: "))
    if Num < 10 or Num > 20:
        Fora =+ 1

Intervalo = 10 - Fora 
