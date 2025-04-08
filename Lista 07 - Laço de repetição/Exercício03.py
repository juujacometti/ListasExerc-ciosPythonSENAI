# Monte um sistema que repita um menu até o usuário escolher sair. Use while e break.

while True:
    # Criação do menu e solicitação de opção
    print("====================\n    CALCULADORA     \n( + ) Soma\n( - ) Subtração\n( * ) Multiplicação\n( / ) Divisão\n( X ) Sair\n====================\n")
    opcao = input("Escolha o símbolo da operação que deseja realizar de acordo com o menu acima:\n")

    # Condição para verificar se o usuário escolheu finalizar o programa
    if opcao == "X" or opcao == "x":
        print("Saindo do programa...")
        break


