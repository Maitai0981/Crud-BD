import os
from funcionario import *

class BD:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.dados = []
        self.leitura()

    def leitura(self):
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, "w") as inicia:
                inicia.write("")
        else:
            with open(self.arquivo, "r") as dados_leitura:
                self.dados = dados_leitura.read().splitlines()

    def pesquisar(self, ID):
        for registro in self.dados:
            partes = registro.split('|')
            if partes[0] == ID:
                return partes
        return None

    def atualizar(self, ID, novo_registro):
        self.dados = [novo_registro if reg.startswith(f"{ID}|") else reg for reg in self.dados]
        self._salvar()

    def deletar(self, ID):
        temp = [reg for reg in self.dados if not reg.startswith(f"{ID}|")]
        if temp == self.dados:
            print("ID {ID} não encntrado")
        else:
            self.dados = temp
            print("Deletado com sucesso!")
        self._salvar()

    def inserir(self, registro):
        id = registro.split('|')[0]
        if not self.pesquisar(id):
            self.dados.append(registro)
            self._salvar()
            return True
        else:
            print(f"Registro com ID {id} já existe.")
            return False

    def _salvar(self):
        with open(self.arquivo, "w") as W:
            W.write("\n".join(self.dados))

class BD_Docente(BD):
    def __init__(self):
        super().__init__("docentes.txt")

class BD_Aluno(BD):
    def __init__(self):
        super().__init__("alunos.txt")