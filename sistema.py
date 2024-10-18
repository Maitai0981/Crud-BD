from BD import *
import platform

class Sistema:
    def __init__(self):
        self.banco_docente = BD_Docente()
        self.banco_aluno = BD_Aluno()

    def inserir(self, funcionario):
        if isinstance(funcionario, Docente):
            registro = f"{funcionario.get_id()}|{funcionario.get_nome()}|{funcionario.get_disciplina()}|{funcionario.get_titulacao()}|{funcionario.get_departamento()}|{funcionario.get_timeinc()}"
            return self.banco_docente.inserir(registro)
        elif isinstance(funcionario, Aluno):
            registro = f"{funcionario.get_id()}|{funcionario.get_nome()}|{funcionario.get_curso()}|{funcionario.get_email()}|{funcionario.get_data_nascimento()}|{funcionario.get_timeinc()}"
            return self.banco_aluno.inserir(registro)
        else:
            return False  

    def deletar(self, ID, tipo):
        if tipo.lower() == "docente":
            self.banco_docente.deletar(ID)
        elif tipo.lower() == "aluno":
            self.banco_aluno.deletar(ID)
        else:
            invalid()  

    def pesquisar(self, ID, tipo):
        if tipo.lower() == "docente":
            return self.banco_docente.pesquisar(ID)
        elif tipo.lower() == "aluno":
            return self.banco_aluno.pesquisar(ID)
        else:
            invalid() 

    def atualizar(self, ID, novo_registro, tipo):
        if tipo.lower() == "docente":
            self.banco_docente.atualizar(ID, novo_registro)
        elif tipo.lower() == "aluno":
            self.banco_aluno.atualizar(ID, novo_registro)
        else:
            invalid()  




    def main(self):
        while True:
            limpar_terminal()

            print("-------- Sistema de cadastro --------")
            print("========= Selecione a opção =========")
            print("1 - Inserir")
            print("2 - Atualizar")
            print("3 - Deletar")
            print("4 - Pesquisar")
            print("0 - Sair")

            try:
                opc = int(input("Digite a opção: "))
            except ValueError:
                print("Opção inválida! Por favor, insira um número.")
                espra()
                continue

            try:
                if opc == 1:
                    tipo = input("Digite o tipo (Docente/Aluno): ")
                    if tipo.lower() == "docente":
                        ID = input("Digite o ID do docente: ")
                        nome = input("Digite o nome do docente: ")
                        disciplina = input("Digite a disciplina do docente: ")
                        titulacao = input("Digite a titulação do docente: ")
                        departamento = input("Digite o departamento do docente: ")
                        if len(ID) == 4:
                            funcionario = Docente(ID, nome, disciplina, titulacao, departamento)
                        else:
                            invalid()
                            espra()
                            continue

                    elif tipo.lower() == "aluno":
                        ID = input("Digite o ID/matricula do aluno: ")
                        nome = input("Digite o nome do aluno: ")
                        curso = input("Digite o curso do aluno: ")
                        email = input("Digite o email do aluno: ")
                        data_nascimento = input("Digite a data de nascimento do aluno (AAAA-MM-DD): ")
                        if validar_data(data_nascimento) and len(ID) == 4 and len(email.split("@")[0]) >= 1:
                            funcionario = Aluno(ID, nome, curso, email, data_nascimento)
                        else:
                            invalid()
                            espra()
                            continue

                    else:
                        print("Tipo inválido! Por favor, insira 'Docente' ou 'Aluno'.")
                        espra()
                        continue

                    temp = self.inserir(funcionario)
                    if temp:
                        print("Inserido com sucesso!")
                    else:
                        print("Erro ao inserir o registro.")

                elif opc == 2:
                    tipo = input("Digite o tipo (Docente/Aluno): ")
                    ID = input("Digite o ID para atualizar: ")
                    registro = self.pesquisar(ID, tipo)
                    
                    if registro:
                        temp = "| "+" | ".join(registro)+" |"
                        print(f"Registro encontrado: {temp}")
                        
                        novo_registro = input("Digite o novo registro (ID|Nome|...): ")
                        self.atualizar(ID, novo_registro, tipo)
                        print("Registro atualizado com sucesso!")
                    else:
                        print("Registro não encontrado.")

                elif opc == 3:
                    tipo = input("Digite o tipo de funcionário (Docente/Aluno): ")
                    ID = input("Digite o ID do funcionário para deletar: ")
                    self.deletar(ID, tipo)
                    

                elif opc == 4:
                    tipo = input("Digite o tipo (Docente/Aluno): ")
                    if tipo.lower() in ["docente", "aluno"]:
                        ID = input("Digite o ID para pesquisar: ")
                        registro = self.pesquisar(ID, tipo)
                        
                        if registro:
                            temp = "| "+" | ".join(registro)+" |"
                            print(f"Registro encontrado: {temp}")
                        else:
                            print("Registro não encontrado.")
                    else:
                        print("Tipo inválido! Por favor, insira 'Docente' ou 'Aluno'.")

                elif opc == 0:
                    limpar_terminal()
                    print("Obrigado")
                    break

                else:
                    print("Opção inválida!")

            except Exception as e:
                print(f"Ocorreu um erro: {str(e)}")

            espra()

def limpar_terminal():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')  
    else:
        os.system('clear')

def validar_data(data_str):
        try:
            datetime.strptime(data_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False
def espra():
    input("\nPressione Enter para continuar...")

def invalid():
    print("Tipo inválido!")

if __name__ == "__main__":
    S = Sistema()
    S.main()