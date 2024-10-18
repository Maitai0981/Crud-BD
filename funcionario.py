from datetime import datetime

class Pessoa:
    def __init__(self, ID, nome):
        self.ID = ID
        self.nome = nome

    def get_id(self):
        return self.ID

    def get_nome(self):
        return self.nome

    def get_timeinc(self):
        data_atual = datetime.now()
        data_formatada = data_atual.strftime('%Y-%m-%d')

        return data_formatada

class Docente(Pessoa):
    def __init__(self, ID, nome, disciplina, titulacao, departamento):
        super().__init__(ID, nome)
        self.disciplina = disciplina
        self.titulacao = titulacao
        self.departamento = departamento

    def get_disciplina(self):
        return self.disciplina

    def get_titulacao(self):
        return self.titulacao

    def get_departamento(self):
        return self.departamento

class Aluno(Pessoa):
    def __init__(self, ID, nome, curso, email, data_nascimento):
        super().__init__(ID, nome)
        
        self.curso = curso
        self.email = email
        self.data_nascimento = data_nascimento  

    def get_curso(self):
        return self.curso

    def get_email(self):
        return self.email

    def get_data_nascimento(self):
        return self.data_nascimento  