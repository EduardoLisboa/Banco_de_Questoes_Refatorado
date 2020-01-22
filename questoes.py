from entrada import func_entrada

class Questao():
    questoes = []
    quantidade_questoes = 0
    indice_questoes = 0
    materias = []

    def __init__(self, materia, palavra_chave, texto, resposta, alternativas, id_professor, id_questao, ativa):
        self.materia = materia
        self.palavra_chave = palavra_chave
        self.texto = texto
        self.resposta = resposta
        self.alternativas = alternativas
        self.id_professor = id_professor
        self.id_questao = id_questao
        self.ativa = ativa
    

    @staticmethod
    def adicionar_questao(id_usuario_online):    
        print('Adicionar Questão')
        # materia = str(input('Matéria: '))
        materia = func_entrada(str, 'Matéria: ')
        # palavra_chave = str(input('Assunto: '))
        palavra_chave = func_entrada(str, 'Assunto: ')
        # texto = str(input('Texto: '))
        texto = func_entrada(str, 'Texto: ')
        # resposta = str(input('Resposta: '))
        resposta = func_entrada(str, 'Resposta: ')
        # alternativas = [str(input(f'Alternativa {i}: ')) for i in range(1, 5)]
        alternativas = [func_entrada(str, f'Alternativa {i}: ') for i in range(1, 5)]
        alternativas.append(resposta)
        nova_questao = Questao(materia, palavra_chave, texto, resposta, alternativas, id_usuario_online, Questao.indice_questoes, True)
        Questao.questoes.append(nova_questao)
        Questao.quantidade_questoes += 1
        Questao.indice_questoes += 1
        if materia not in Questao.materias: Questao.materias.append(materia)
        print('\nQuestão adicionada com sucesso!\n')
        input()


def atualizar_questoes():
    if Questao.quantidade_questoes > 0: return
    aux_questao = []
    cont = 0
    for linha in open('questoes.txt', 'r', encoding='utf-8'):
        if 0 <= cont < 9:
            aux_questao.append(linha.replace('\n', ''))
        elif cont >= 9:
            nova_questao = Questao(aux_questao[0], aux_questao[1], aux_questao[2], aux_questao[3], aux_questao[4:9], 1, Questao.indice_questoes, True)
            Questao.questoes.append(nova_questao)
            Questao.quantidade_questoes += 1
            Questao.indice_questoes += 1
            if nova_questao.materia not in Questao.materias: Questao.materias.append(nova_questao.materia)
            aux_questao.clear()
            cont = -1
        cont += 1

    # Insere a última questão da lista
    nova_questao = Questao(aux_questao[0], aux_questao[1], aux_questao[2], aux_questao[3], aux_questao[4:9], 1, Questao.indice_questoes, True)
    Questao.questoes.append(nova_questao)
    Questao.quantidade_questoes += 1
    Questao.indice_questoes += 1