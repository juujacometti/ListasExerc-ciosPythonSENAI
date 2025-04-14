# Crie um programa que leia uma sequência de números e determine quantos números são menores que a média.

# Criação de uma lista para determinar a sequência de números
lista_numeros = []

# Solicitação de quantos números a lista terá
quantidade = int(input("Quantos números você deseja adcionar a lista?\n"))
divisor_media = quantidade

# Looping para adicionar os números escolhidos na lista de acordo com a quantidade definida
for lista in range(quantidade):
    numero = int(input("\nDigite um número inteiro:\n"))
    lista_numeros.append(numero) # Adiciona os valores ao final da lista
    quantidade -= 1
    
# Mostra quais números o usuário adicionou na lista
print(f"\nOs números adicionados a lista foram: {lista_numeros}")

# Realiza o cálculo da média dos elementos dentro da lista
media = sum(lista_numeros) / divisor_media
print(f"O resultado da méda entre os valores que estão dentro da lista é: {media}\n")

# Verifica quais números dentro da lista ficaram abaixo da média da lista
print("Os números dentro da lista que são abaixo da média são:")
for numero in lista_numeros:
    if numero < media:
        print(numero)




    