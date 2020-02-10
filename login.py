from getpass import getpass
from os import system
from hashing import hashing
from usuarios import TodosUsuarios
from questoes import Questao, atualizar_questoes
from banco_de_questoes import banco_de_questoes, limpar_tela
from entrada import func_entrada


usuarios_dict = dict()
def ler_usuarios():
    usuarios_dict.clear()
    for usuario in TodosUsuarios.usuarios:
        if usuario.ativo:
            usuarios_dict[usuario.login] = [usuario.senha, usuario.is_prof, usuario.id_usuario]


def login():
    while(True):
        limpar_tela()
        ler_usuarios()
        atualizar_questoes()
        try:
            login = func_entrada(str, 'Login: ')
            senha = func_entrada(getpass, 'Senha: ')

            if usuarios_dict[login][0] == hashing(senha):
                print('\nLogin realizado com sucesso!\n')
                input()
                banco_de_questoes(usuarios_dict[login][1], usuarios_dict[login][2])
                exit()
            else:
                print('\nSenha incorreta!\n')
                input()
                system('clear')
        except KeyboardInterrupt:
            print('\nAté logo!\n')
            exit()
        except KeyError:
            print('\nUsuário não cadastrado!\n')
            input()
