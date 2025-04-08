# Crie um programa que simule o uso de senha com tentativas infinitas até digitar a senha correta (use while True).

while True:
    senha = input("Digite sua senha:\n")

    if senha == "julya":
        print("A senha digitada está correta!")
        break

    else:
        print("A senha digitada está incorreta. Tente novamente:\n")
