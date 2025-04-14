# Crie um programa que peça dois números inteiros e exiba todos os números entre eles que são primos. Use for.

numero1 = int(input("Digite um número inteiro:\n"))
numero2 = int(input("Digite um outro número inteiro:\n"))

# Realiza a verificação de qual número é menor e maior, para ajustar a ordem
inicio = min(numero1, numero2)
fim = max(numero1, numero2)

print(f"\nOs números primos entre {inicio} e {fim} são:\n")

# Lopping para verificar entre os dois números, quais valores são primos
for primo in range(inicio, fim + 1):
    if primo >= 1:
        for i in range(2, primo):
            if (primo % i) == 0:
                break
            
        else:
            print(primo)



