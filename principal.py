from alunos import Aluno

# Criando a instância da classe Aluno e garantindo que a tabela seja criada
aluno_instancia = Aluno()

# Menu de opções
while True:
    print("\n <------ Menu da Academia ------>")
    print("\n1. Cadastrar aluno")
    print("2. Consultar todos os alunos")
    print("3. Consultar aluno por código")
    print("4. Atualizar aluno")
    print("5. Deletar aluno")
    print("6. Atualizar plano de um aluno")
    print("7. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        # Cadastrar aluno
        nome = input("Nome do aluno: ")
        idade = int(input("Idade do aluno: "))
        plano = input("Plano do aluno: ")
        data_inicio = input("Data de início (YYYY-MM-DD): ")
        aluno_instancia.cadastrarAluno(nome, idade, plano, data_inicio)

    elif opcao == 2:
        # Consultar todos os alunos
        print("\nLista de todos os alunos cadastrados:")
        aluno_instancia.consultarAlunos()

    elif opcao == 3:
        # Consultar um aluno pelo código
        codigo = int(input("Informe o código do aluno: "))
        aluno_instancia.consultarAlunoIndividual(codigo)

    elif opcao == 4:
        # Atualizar os dados de um aluno
        codigo = int(input("Informe o código do aluno a ser atualizado: "))
        nome = input("Novo nome do aluno: ")
        idade = int(input("Nova idade do aluno: "))
        plano = input("Novo plano do aluno: ")
        data_inicio = input("Nova data de início (YYYY-MM-DD): ")
        aluno_instancia.atualizarAluno(nome, idade, plano, data_inicio, codigo)

    elif opcao == 5:
        # Deletar aluno pelo código
        codigo = int(input("Informe o código do aluno a ser deletado: "))
        aluno_instancia.deletarAluno(codigo)

    elif opcao == 6:
        # Atualizar o plano de um aluno
        codigo = int(input("Informe o código do aluno: "))
        novo_plano = input("Informe o novo plano do aluno: ")
        aluno_instancia.atualizarPlano(novo_plano, codigo)

    elif opcao == 7:
        # Sair do programa
        print("Encerrando o programa...")
        aluno_instancia.fechar_conexao()  # Fechar a conexão ao sair
        break

    else:
        print("Opção inválida! Escolha uma opção válida.")
