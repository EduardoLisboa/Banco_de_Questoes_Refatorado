from getpass import getpass
from hashing import hashing
from entrada import func_entrada

class TodosUsuarios():
    usuarios = []
    quantidade_usuarios = 0

# Interface
# Porque todos os métodos foram  obrigatoriamente implementados
class Usuario():
    
    @staticmethod
    def remover():
        pass

    @staticmethod
    def listar():
        print('Listar Usuários')
        for usuario in TodosUsuarios.usuarios:
            if usuario.ativo:
                print(f'ID: {usuario.id_usuario}')
                print(f'Nome: {usuario.nome.title()}')
                print(f'Instituição: {usuario.instituicao.title()}\n')
        input()


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


class Aluno(Usuario):
    alunos = []
    indice_atual_alunos = 0

    def __init__(self, is_prof, nome, instituicao, idade, login, senha, id_usuario, id_professor, ativo):
        self.is_prof = is_prof
        self.nome = nome
        self.instituicao = instituicao
        self.login = login
        self.senha = hashing(senha)
        self.id_usuario = id_usuario
        self.ativo = ativo
        self.idade = idade
        self.id_professor = id_professor


    def remover(self):
        self.ativo = False


    @staticmethod
    def listar():
        print('Listar Alunos')
        for aluno in Aluno.alunos:
            if aluno.ativo:
                print(f'ID: {aluno.id_usuario}')
                print(f'Nome: {aluno.nome.title()}')
                print(f'Instituição: {aluno.instituicao.title()}')
                print(f'Idade: {aluno.idade}')
                print(f'ID Professor Resposável: {aluno.id_professor}\n')
        input()
    

    @staticmethod
    def adicionar_aluno(id_usuario_online):
        print('Adicionar Aluno')
        nome = func_entrada(str, 'Nome: ')
        instituicao = func_entrada(str, 'Instituição: ')
        idade = func_entrada(int, 'Idade: ')
        login = func_entrada(str, 'Login: ')
        senha = func_entrada(getpass, 'Senha: ')
        novo_aluno = Aluno(0, nome, instituicao, idade, login, senha, Aluno.indice_atual_alunos + 1001, id_usuario_online, True)
        
        Aluno.indice_atual_alunos += 1
        Aluno.alunos.append(novo_aluno)
        TodosUsuarios.quantidade_usuarios += 1
        TodosUsuarios.usuarios.append(novo_aluno)

        print('\nAluno cadastrado com sucesso!\n')
        input()


admin = Professor(1, 'admin', 'admin', 'todas', 'admin', 'admin', Professor.indice_atual_professores + 1, True)
TodosUsuarios.quantidade_usuarios += 1
TodosUsuarios.usuarios.append(admin)
Professor.indice_atual_professores += 1
Professor.professores.append(admin)

aluno = Aluno(0, 'Eduardo Lisboa', 'UFAL', 24, 'eduardo', '123', Aluno.indice_atual_alunos + 1001, admin.id_usuario, True)
TodosUsuarios.quantidade_usuarios += 1
TodosUsuarios.usuarios.append(aluno)
Aluno.indice_atual_alunos += 1
Aluno.alunos.append(aluno)
