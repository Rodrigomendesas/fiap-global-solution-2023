def cadastrarCuidador():
    novoCuidador = {}
    nomeCuidador = input("Primeiro nome do cuidador: ")
    sobrenomeCuidador = input("Sobrenome do cuidador: ")
    emailCuidador = input("Email do cuidador: ")
    cpfCuidador = input("CPF do cuidador: ")
    formacaoCuidador = input("Formação do cuidador: ")
    qualificacoesCuidador = input("Qualificações adicionais do cuidador: ")
    novoCuidador.update({
        "Nome": nomeCuidador,
        "Sobrenome": sobrenomeCuidador,
        "E-mail": emailCuidador,
        "CPF": cpfCuidador,
        "Formação": formacaoCuidador,
        "Qualificações adicionais": qualificacoesCuidador
    })
    print("Cuidador adicionado com sucesso: ")
    print(f'Nome: {nomeCuidador} {sobrenomeCuidador}')
    print(f'E-mail: {emailCuidador}')
    print(f'CPF: {cpfCuidador}')
    print(f'Formação: {formacaoCuidador}')
    print(f'Qualificações adicionais: {qualificacoesCuidador}')