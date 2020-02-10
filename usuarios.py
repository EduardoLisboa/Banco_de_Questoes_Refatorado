from getpass import getpass
from hashing import hashing
from entrada import func_entrada
import login

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
    def editar_usuario():
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
