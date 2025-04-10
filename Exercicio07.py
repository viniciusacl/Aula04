#Ler 5 Valores, Calcular e Escrever a Média Aritmética desses Valores lidos.
Media = 0
for X in range(5):
    Nota = int(input("Digite os Valores: "))
    Media += Nota
Media /= 5
print(Media)
