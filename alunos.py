import sqlite3

class Aluno:
    def __init__(self):
        self.conexao = self.criar_conexao()

    def criar_conexao(self):
        # Estabelecendo conexão e criando tabela
        conexao = sqlite3.connect("academia.db")
        consulta = conexao.cursor()
        tabela = """
        CREATE TABLE IF NOT EXISTS alunos(
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        idade INTEGER,
        plano VARCHAR(50),
        data_inicio DATE
        );
        """
        consulta.execute(tabela)
        return conexao

    def cadastrarAluno(self, nome, idade, plano, data_inicio):
        # Inserindo novo aluno no banco de dados
        sql = "INSERT INTO alunos (nome, idade, plano, data_inicio) VALUES (?, ?, ?, ?)"
        campos = (nome, idade, plano, data_inicio)
        consulta = self.conexao.cursor()
        consulta.execute(sql, campos)
        self.conexao.commit()
        print(consulta.rowcount, "Linha(s) inserida(s) com sucesso.")

    def consultarAlunos(self):
        # Consultando todos os alunos
        sql = "SELECT * FROM alunos"
        consulta = self.conexao.cursor()
        consulta.execute(sql)
        resultado = consulta.fetchall()
        if resultado:
            for aluno in resultado:
                print(f"Código: {aluno[0]}")
                print(f"Nome: {aluno[1]}")
                print(f"Idade: {aluno[2]}")
                print(f"Plano: {aluno[3]}")
                print(f"Data de início: {aluno[4]}\n")
        else:
            print("Nenhum aluno cadastrado.")

    def deletarAluno(self, codigo):
        # Deletando aluno pelo código
        sql = "DELETE FROM alunos WHERE codigo = ?"
        consulta = self.conexao.cursor()
        consulta.execute(sql, (codigo,))
        self.conexao.commit()
        if consulta.rowcount > 0:
            print(f"Aluno com código {codigo} excluído com sucesso.")
        else:
            print(f"Aluno não encontrado.")

    def atualizarAluno(self, nome, idade, plano, data_inicio, codigo):
        # Atualizando dados de um aluno
        sql = "UPDATE alunos SET nome = ?, idade = ?, plano = ?, data_inicio = ? WHERE codigo = ?"
        campos = (nome, idade, plano, data_inicio, codigo)
        consulta = self.conexao.cursor()
        consulta.execute(sql, campos)
        self.conexao.commit()
        if consulta.rowcount > 0:
            print(f"Aluno com código {codigo} atualizado com sucesso.")
        else:
            print(f"Aluno não encontrado.")

    def consultarAlunoIndividual(self, codigo):
        # Consultando um aluno específico pelo código
        sql = "SELECT * FROM alunos WHERE codigo = ?"
        consulta = self.conexao.cursor()
        consulta.execute(sql, (codigo,))
        resultado = consulta.fetchone()
        if resultado:
            print(f"Código: {resultado[0]}")
            print(f"Nome: {resultado[1]}")
            print(f"Idade: {resultado[2]}")
            print(f"Plano: {resultado[3]}")
            print(f"Data de início: {resultado[4]}\n")
        else:
            print("Aluno não encontrado.")

    def atualizarPlano(self, plano, codigo):
        # Atualizando o plano de um aluno
        sql = "UPDATE alunos SET plano = ? WHERE codigo = ?"
        campos = (plano, codigo)
        consulta = self.conexao.cursor()
        consulta.execute(sql, campos)
        self.conexao.commit()
        if consulta.rowcount > 0:
            print(f"Aluno com código {codigo} teve seu plano alterado para {plano}.")
        else:
            print(f"Aluno não encontrado.")

    # Fechando a conexão ao final
    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()