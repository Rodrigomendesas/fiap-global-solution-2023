def cadastrarResponsavel():
    novoResponsavel = {}
    nomeResponsavel = input("Primeiro nome do responsável: ")
    sobrenomeResponsavel = input("Sobrenome do responsável: ")
    emailResponsavel = input("Email do responsável: ")
    cpfResponsavel = input("CPF do responsável: ")
    relacaoResponsavel = input("Relação do responsável com o paciente: ")
    novoResponsavel.update({
        "Nome": nomeResponsavel,
        "Sobrenome": sobrenomeResponsavel,
        "E-mail": emailResponsavel,
        "CPF": cpfResponsavel,
        "Formação": relacaoResponsavel,
    })
    print("Responsável adicionado com sucesso: ")
    print(f'Nome: {nomeResponsavel} {sobrenomeResponsavel}')
    print(f'E-mail: {emailResponsavel}')
    print(f'CPF: {cpfResponsavel}')
    print(f'Relação com paciente: {relacaoResponsavel}')
