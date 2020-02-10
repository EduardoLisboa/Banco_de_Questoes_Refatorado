from usuarios import Usuario, TodosUsuarios
from getpass import getpass
from hashing import hashing
from entrada import func_entrada
import login

class Professor(Usuario):
    professores = []
    indice_atual_professores = 0

    def __init__(self, is_prof, nome, instituicao, materia, login, senha, id_usuario, ativo):
        self.is_prof = is_prof
        self.nome = nome
        self.instituicao = instituicao
        self.login = login
        self.senha = hashing(senha)
        self.id_usuario = id_usuario
        self.ativo = ativo
        self.materia = materia

    
    def remover(self):
        self.ativo = False


    @staticmethod
    def adicionar_professor():
        print('Adicionar Professor')
        nome = func_entrada(str, 'Nome: ')
        instituicao = func_entrada(str, 'Instituição: ')
        materia = func_entrada(str, 'Matéria que leciona: ')
        login = func_entrada(str, 'Login: ')
        senha = func_entrada(getpass, 'Senha: ')
        novo_prof = Professor(1, nome, instituicao, materia, login, senha, Professor.indice_atual_professores + 1, True)

        Professor.indice_atual_professores += 1
        Professor.professores.append(novo_prof)
        TodosUsuarios.quantidade_usuarios += 1
        TodosUsuarios.usuarios.append(novo_prof)

        print('\nProfessor cadastrado com sucesso!\n')
        input()
    
    
    def editar_usuario(self):
        print(f'1 - Nome: {self.nome}')
        print(f'2 - Instituição: {self.instituicao}')
        print(f'3 - Matéria que leciona: {self.materia}')
        print(f'4 - Login: {self.login}')
        print('5 - Senha')
        print('6 - Desativar conta')
        print('7 - Retornar')
        opc = func_entrada(int, '--> ', True, 7)

        if opc == 1:
            self.nome = func_entrada(str, 'Novo Nome: ')
            print('\nNome alterado com sucesso!')
            input()
        elif opc == 2:
            self.instituicao = func_entrada(str, 'Nova Instituição: ')
            print('\nInstituição alterada com sucesso!')
            input()
        elif opc == 3:
            self.materia = func_entrada(str, 'Nova Matéria: ')
            print('\nMatéria alterada com sucesso!')
            input()
        elif opc == 4:
            self.login = func_entrada(str, 'Novo Login: ')
            print('\nLogin alterado com sucesso!')
            input()
        elif opc == 5:
            senha_atual = hashing(func_entrada(getpass, 'Senha atual: '))
            if senha_atual == self.senha:
                nova_senha = func_entrada(getpass, 'Nova senha: ')
                confirmar = func_entrada(getpass, 'Confirmar a nova senha: ')
                if nova_senha == confirmar:
                    self.senha = hashing(nova_senha)
                    print('\nSenha alterada com sucesso!')
                    input()
                else:
                    print('As senhas estão diferentes!')
                    input()
            else:
                print('Senha incorreta!')
                input()
        elif opc == 6:
            confirmar = func_entrada(str, '\nConfirmar exclusão da conta? (s/n)\n--> ').lower()
            if confirmar == 's':
                self.ativo = False
                print('\nConta excluída com sucesso!')
                input()
                login.login()
        elif opc == 7:
            pass


admin = Professor(1, 'admin', 'admin', 'todas', 'admin', 'admin', Professor.indice_atual_professores + 1, True)
TodosUsuarios.quantidade_usuarios += 1
TodosUsuarios.usuarios.append(admin)
Professor.indice_atual_professores += 1
Professor.professores.append(admin)