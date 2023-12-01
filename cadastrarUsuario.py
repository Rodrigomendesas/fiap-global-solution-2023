import cadastrarPaciente
import cadastrarCuidador
import cadastrarResponsavel
import cadastrarMedico

def cadastrarUsuario():
    while True:
        print("""
---Menu de cadastro---            
Insira quem você quer cadastrar:         
""")
        try: 
            opcaoDeCadastro = int(input("""
1 - Paciente
2 - Cuidador
3 - Responsável
4 - Médico
5 - Retornar
"""))
            if opcaoDeCadastro == 1:
                print("Vamos pedir agora algumas informações do paciente.")
                cadastrarPaciente.cadastrarPaciente()
            elif opcaoDeCadastro == 2:
                print("Vamos pedir agora algumas informações do cuidador.")
                cadastrarCuidador.cadastrarCuidador()
            elif opcaoDeCadastro == 3:
                print("Vamos pedir agora algumas informações do responsável.")
                cadastrarResponsavel.cadastrarResponsavel()
            elif opcaoDeCadastro == 4:
                print("Vamos pedir agora algumas informações do médico.")
                cadastrarMedico.cadastrarMedico()
            elif opcaoDeCadastro == 5:
                break
            else:
                print("Desculpe, opção inválida. ")
        except ValueError: 
            print("Erro: por favor, insira uma das opções válidas.")