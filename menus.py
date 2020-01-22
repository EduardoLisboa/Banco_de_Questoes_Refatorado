def cabecalho():
    print('-=' * 19, end='-\n')
    print('BANCO DE QUESTÕES'.center(40))
    print('-=' * 19, end='-\n')


def banco_professor():
    print('''Bem-vindo, professor!
1 - Adicionar Professor
2 - Alunos
3 - Listar usuários
4 - Editar Perfil
5 - Questões
6 - Gerar Prova
7 - Sair
8 - Encerrar
--> ''', end='')


def banco_aluno():
    print('''Bem-vindo, caro aluno!
1 - Editar Perfil
2 - Exibir Questões
3 - Gerar Simulado
4 - Sair
5 - Encerrar
--> ''', end='')


def menu_questoes():
    print('''1 - Exibir Questões
2 - Adicionar questão
3 - Remover questão
4 - Retornar
--> ''', end='')


def menu_exibir_questoes():
    print('''1 - Todas
2 - Selecionar matéria
3 - Retornar
--> ''', end='')


def menu_alunos():
    print('''1 - Listar Alunos
2 - Adicionar Aluno
3 - Remover Aluno
4 - Retornar
--> ''', end='')


menus_bancos = [banco_aluno, banco_professor] # 0 pra aluno, 1 pra professor

menus_questoes = [menu_questoes, menu_exibir_questoes]
