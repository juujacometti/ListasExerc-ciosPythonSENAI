# Crie um programa que leia uma sequência de números e determine o segundo maior número.

# Criação de uma lista para armazenar os números digitados pelo usuário
lista_numeros = []

# Solicita a quantidade de elementos que a lista irá conter
quantidade = int(input("Digite a quantidade que você deseja que a sua lista de números contenha:\n"))

# Solicita os elementos e os adiciona na lista conforme a quantidade escolhida
for lista in range(quantidade):
    numero = int(input("\nDigite um número inteiro:\n"))
    lista_numeros.append(numero)
    quantidade -= 1
    
# Mostra ao usuário quais foram os números adicionados na lista
print(f"\nOs números que foram adicionados na lista são: {lista_numeros}")
    
# Encontra o maior número presente na lista
maior = max(lista_numeros)

# Remove o maior número encontrado na lista 
lista_numeros.remove(maior)    

# Utiliza a função max( ) para novamente encontrar o maior número, porém com o primeiro maior número removido
segundo_maior = max(lista_numeros)
print(f"O segundo maior número presente na lista é: {segundo_maior}")


    
    
    