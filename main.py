import cadastrarUsuario
import menuSistema

def menuInicial():
    global continuar 
    continuar = True
    while continuar:
        print("Olá, você está no Hora Do Remédio")
        print("Por favor, digite a sua opção:")
        opcao = int(input(
"""
1 - Cadastrar novo usuário
2 - Acessar sistema
0 - Encerrar programa
Opção desejada: 
"""
        ))
        if opcao == 1:
            cadastrarUsuario.cadastrarUsuario()
        elif opcao == 2:
            menuSistema.menuSistema()
        elif opcao == 0:
            print("---Encerrando o programa---")
            continuar = False
            break
        else:
            print("Opção inválida. Por favor, selecione 1, 2 ou 0.")

menuInicial()
