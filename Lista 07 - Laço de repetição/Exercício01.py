# Peça 10 números e conte quantos são múltiplos de 3. Use for.

# Variável para armazenar quantos números digitados são múltiplos de três
multiplos_de_tres = 0

# Looping (solicitação de 10 valores e contagem de números múltiplos)
for numero in range(1, 11):

    valor = int(input(f"Digite o {numero} numero:\n"))
    numero = numero + 1

    if valor % 3 == 0:
        multiplos_de_tres = multiplos_de_tres + 1
        print(f"Você digitou {multiplos_de_tres} números que são múltiplos de três.")


