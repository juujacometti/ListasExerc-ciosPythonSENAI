# O usuário tem 3 tentativas para acertar a senha. Se errar todas, o acesso é bloqueado. Use while.

# Limite de quantidade de tentativas
tentativa = 3

# Solicitação da senha para o usuário
while True:
    senha = input("Digite sua senha:\n")

    # Condição para verificar se a senha está correta
    if senha == "julya":
        print("A senha está correta!")
        break

    # Caso a senha não esteja correta, o número de tentativas diminui, e ao chegar em zero, o programa acaba
    else:
        tentativa = tentativa - 1
        print(f"A senha está incorreta. Você possui {tentativa} tentativas!")

        if tentativa == 0:
            print("Acabaram as suas chances!")
            break