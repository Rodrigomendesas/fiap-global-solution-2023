def menuSistema():
    global continuar 
    continuar = True
    print("Escolha o perfil de acesso ao sistema: ")
    opcaoDeAcesso = int(input("""
1. Acessar como paciente
2. Acessar como médico
3. Acessar como cuidador
4. Acessar como responsável
0. Voltar
"""))
    if opcaoDeAcesso == 1:        
        print("---Acesso de paciente---")
        while continuar:
            opcaoDeAcessoPaciente = int(input("""
1. Acessar tratamento
2. Acessar histórico de tratamentos
3. Confirmar uso do medicamento
0. Sair
"""))
            if opcaoDeAcessoPaciente == 1:
                while True:
                    print("""
Os seguintes tratamentos estão em curso: 
Condição: 
Medicamento:
Periodicidade: 
Prazo: 
""")
                    break
            elif opcaoDeAcessoPaciente == 2:
                while True:
                    print("""
Os seguintes tratamentos já foram encerrados: 
Condição: 
Medicamento:
Periodicidade: 
Prazo: 
""")
                    break 
            elif opcaoDeAcessoPaciente == 3:
                while True: 
                    confirmarUso = input("Confirmar o uso do medicamento XXX? ").upper()
                    if confirmarUso == "S":
                        print("Registro completo")
                        break
                    else:
                        print("Voltando ao menu anterior")
                        break
            elif opcaoDeAcessoPaciente == 0:
                continuar = False
    elif opcaoDeAcesso == 2:
        print("---Acesso de médico---")
        while continuar:
                opcaoDeAcessoMedico = int(input("""
1. Inserir novo medicamento
2. Acessar histórico de tratamentos
3. Acessar tratamento em curso
0. Sair
"""))
                if opcaoDeAcessoMedico == 1:
                    while True:
                        nomeMedicamento = input("Digite o nome do medicamento: ")
                        periodicidadeMedicamento = input("Periodicidade com que o remédio deve ser tomado: ")
                        prazoMedicamento = input("Até quando o paciente deve tomar o medicamento?")
                        print(f'Medicamento: {nomeMedicamento}')
                        print(f'Periodicidade: {periodicidadeMedicamento}')
                        print(f'Prazo: {prazoMedicamento}')
                        print("Tratamento registrado com sucesso.")
                        break
                elif opcaoDeAcessoMedico == 2:
                    while True:
                        print("""Os seguintes tratamentos já foram encerrados: 
Condição: 
Medicamento:
Periodicidade: 
Prazo: 
""")
                        break 
                elif opcaoDeAcessoMedico == 3:
                    while True:
                        print("""
Os seguintes tratamentos estão em curso: 
Condição: 
Medicamento:
Periodicidade: 
Prazo: 
""")
                        break
                elif opcaoDeAcessoMedico == 0:
                    continuar = False
    elif opcaoDeAcesso == 3:
        print("---Acesso de cuidador---")
        while continuar:
                opcaoDeAcessoCuidador = int(input("""
1. Acessar histórico de tratamentos
2. Acessar tratamento em curso
3. Confirmar uso do medicamento
0. Sair
"""))
                if opcaoDeAcessoCuidador == 1:
                    while True:
                        print("""
Os seguintes tratamentos já foram encerrados: 
Condição: 
Medicamento:
Periodicidade: 
Prazo: 
""")
                        break 
                elif opcaoDeAcessoCuidador == 2:
                    while True:
                        print("""
Os seguintes tratamentos estão em curso: 
Condição: 
Medicamento:
Periodicidade: 
Prazo: 
""")
                        break
                elif opcaoDeAcessoCuidador == 3:
                    while True: 
                        confirmarUso = input("Confirmar o uso do medicamento XXX? S/N ").upper()
                        if confirmarUso == "S":
                            print("Registro completo")
                            break
                        else:
                            print("Voltando ao menu anterior")
                            break
                elif opcaoDeAcessoCuidador == 0:
                    continuar = False
    elif opcaoDeAcesso == 4:
        print("---Acesso de responsável---")
        while continuar:
                opcaoDeAcessoResponsavel = int(input("""
1. Acessar histórico de tratamentos
2. Acessar tratamento em curso
3. Confirmar uso do medicamento
0. Sair
"""))
                if opcaoDeAcessoResponsavel == 1:
                    while True:
                        print("""
Os seguintes tratamentos já foram encerrados: 
Condição: 
Medicamento:
Periodicidade: 
Prazo: 
""")
                        break 
                elif opcaoDeAcessoResponsavel == 2:
                    while True:
                        print("""
Os seguintes tratamentos estão em curso: 
Condição: 
Medicamento:
Periodicidade: 
Prazo: 
""")
                        break
                elif opcaoDeAcessoResponsavel == 3:
                    # while True: 
                    confirmarUso = input("Confirmar o uso do medicamento XXX? S/N ").upper()
                    if confirmarUso == "S":
                        print("Registro completo")
                        break
                    else:
                        print("Voltando ao menu anterior")
                        break
                elif opcaoDeAcessoResponsavel == 0:
                    continuar = False
    
