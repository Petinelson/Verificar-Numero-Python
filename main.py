from click import clear

while(True):
    clear()
    numero = int(input("informe um numero: "))

    if numero > 0:
        print("numero é positivo")
        input("Pressione ENTER para continuar")

    elif numero < 0:
        print("numero é negativo")
        input("Pressione ENTER para continuar")

    else:
        print("numero é zero")
        input("Pressione ENTER para continuar")


    verificar = input("Deseja continuar no sistema (S/N)")
    if verificar == "N":
        break
