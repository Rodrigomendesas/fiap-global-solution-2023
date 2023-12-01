def cadastrarPaciente():
    novoPaciente = {}
    nomePaciente = input("Primeiro nome do paciente: ")
    sobrenomePaciente = input("Sobrenome do paciente: ")
    emailPaciente = input("Email do paciente: ")
    cpfPaciente = input("CPF do paciente: ")
    sexoPaciente = input("Sexo biológico do paciente: ")
    dataNascimento = input("Data de nascimento do paciente: ")
    novoPaciente.update({
        "Nome": nomePaciente,
        "Sobrenome": sobrenomePaciente,
        "E-mail": emailPaciente,
        "CPF": cpfPaciente,
        "Sexo biológico": sexoPaciente,
        "Data de nascimento": dataNascimento    
    })
    print("Paciente adicionado com sucesso: ")
    print(f'Nome: {nomePaciente} {sobrenomePaciente}')
    print(f'E-mail: {emailPaciente}')
    print(f'CPF: {cpfPaciente}')
    print(f'Sexo biológico: {sexoPaciente}')
    print(f'Data de nascimento: {dataNascimento}')

    