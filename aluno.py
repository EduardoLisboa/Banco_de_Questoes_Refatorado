from usuarios import Usuario, TodosUsuarios
from getpass import getpass
from hashing import hashing
from entrada import func_entrada
import login

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
    

    def editar_usuario(self):
        print(f'1 - Nome: {self.nome}')
        print(f'2 - Instituição: {self.instituicao}')
        print(f'3 - Idade: {self.idade}')
        print(f'4 - Login: {self.login}')
        print('5 - Senha')
        print('6 - Retornar')
        opc = func_entrada(int, '--> ', True, 6)

        if opc == 1:
            self.nome = func_entrada(str, 'Novo Nome: ')
            print('\nNome alterado com sucesso!')
            input()
        elif opc == 2:
            self.instituicao = func_entrada(str, 'Nova Instituição: ')
            print('\nInstituição alterada com sucesso!')
            input()
        elif opc == 3:
            self.idade = func_entrada(str, 'Nova Idade: ')
            print('\nIdade alterada com sucesso!')
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
            pass


aluno = Aluno(0, 'Eduardo Lisboa', 'UFAL', 24, 'eduardo', '123', Aluno.indice_atual_alunos + 1001, 1, True)
TodosUsuarios.quantidade_usuarios += 1
TodosUsuarios.usuarios.append(aluno)
Aluno.indice_atual_alunos += 1
Aluno.alunos.append(aluno)