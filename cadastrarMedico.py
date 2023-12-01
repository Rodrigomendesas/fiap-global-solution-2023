def cadastrarMedico():
    novoMedico = {}
    nomeMedico = input("Primeiro nome do médico: ")
    sobrenomeMedico = input("Sobrenome do médico: ")
    emailMedico = input("Email do médico: ")
    crmMedico = input("CRM do médico: ")
    especialidadeMedico = input("Especialidade do médico: ")
    novoMedico.update({
        "Nome": nomeMedico,
        "Sobrenome": sobrenomeMedico,
        "E-mail": emailMedico,
        "CPF": crmMedico,
        "Especialidade": especialidadeMedico,
    })
    print("Médico adicionado com sucesso: ")
    print(f'Nome: {nomeMedico} {sobrenomeMedico}')
    print(f'E-mail: {emailMedico}')
    print(f'CPF: {crmMedico}')
    print(f'Especialização: {especialidadeMedico}')