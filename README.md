**Disciplina: Projeto de Software**

**Professor: Baldoino Fonseca dos Santos Neto**

**Refatoramento do Projeto em Python com OO para a disciplina de Projeto de Software.**

Para rodar o programa (no terminal): `python main.py`


# Sistema Banco de Questões

O objetivo do projeto é construir um sistema de banco de questões.

O sistema consiste de um banco de dados contendo diversas questões nível Enem além de seus dados associados, como matéria à qual a questão pertence e palavras-chave. O banco de questões deverá ter um cadastro de professores e alunos, assim como um sistema de login com opções específicas de cada um.

- Os professores podem visualizar todas as questões, assim como cadastrar e remover questões do banco, podendo também gerar provas com um número pré-selecionado de questões de um número pré-selecionado de matérias (ex.: 3 questões de biologia e 5 de física), recebendo dois arquivos, um com as questões e suas alternativas sendo ambas em ordem aleatória e outro com as respostas, na mesma ordem das questões.

- Os alunos podem visualizar todas as questões, mas não podem ver as respostas. Alunos só podem ser cadastrados no sistema por um professor. Eles podem também gerar simulados que serão gerados semelhante à prova, porém devem ser respondidos no próprio sistema e as respostas só devem ser exibidas no final, junto com o percentual de acerto.


Func. | Título da funcionalidade | Breve Descrição
:------:|:--------|:-----------------
1 | Adicionar um professor | Um novo professor é adicionado ao sistema. Os seguintes atributos são fornecidos: Nome completo, Instituição de Ensino à qual o professor pertence, matéria que leciona, login e a senha de acesso ao sistema (a senha poderá ser alterada pelo professor posteriormente). Um código único para o professor deverá ser gerado automaticamente pelo sistema.
2 | Remover um professor | O próprio professor poderá remover seu cadastro do sistema.
3 | Adicionar um aluno | Um novo aluno é adicionado ao sistema somente por um professor, ficando o cadastro do aluno atrelado ao do professor. Os seguintes atributos são fornecidos: Nome completo, Instituição de Ensino do aluno, idade, login e senha de acesso (a senha poderá ser alterada pelo aluno posteriormente). O sistema também deverá gerar um código único para o aluno automaticamente.
4 | Remover um aluno | O professor ao qual o aluno está atrelado pode removê-lo do sistema.
5 | Adicionar uma questão | Um professor pode adicionar uma nova questão ao banco. Os seguintes atributos são fornecidos: Matéria, Palavra-chave (referente ao assunto da questão), texto da questão e uma resposta correta e quatro alternativas erradas.
6 | Remover uma questão | Um professor pode remover uma questão do sistema.
7 | Exibir questões | Qualquer usuário pode exibir todas as questões cadastradas, mas as respostas deverão aparecer apenas para os professores. As questões podem ser exibidas por matéria, por palavra-chave ou todas de uma vez.
8 | Gerar prova | Um professor pode gerar uma prova, entrando as matérias e o número de questões de cada matéria. Deverão ser retornados dois arquivos, um com as questões em ordem aleatória, assim como suas respectivas alternativas, e outro com as respostas, na mesma ordem que as questões da prova.
9 | Gerar simulado | Um aluno pode gerar um simulado, entrando as matérias e o número de questões de cada matéria. Esse simulado deverá ser respondido no próprio sistema, sendo as questões em ordem aleatória, assim como suas respectivas alternativas. Ao final do simulado, deverá ser apresentado o percentual de acerto e as respostas corretas de todas as questões.
10 | Acesso ao sistema | Alunos e professores poderão acessar o sistema através de login e senha escolhidos no momento do cadastro, sendo exibidas apenas suas opções permitidas.

### TASKLIST
- [X] ACESSO DO SISTEMA
- [X] ADICIONAR PROFESSOR
- [X] REMOVER PROFESSOR
- [X] ADICIONAR ALUNO
- [X] REMOVER ALUNO
- [X] ADICIONAR QUESTÃO
- [X] REMOVER QUESTÃO
- [X] EXIBIR QUESTÕES
- [X] GERAR PROVA
- [X] GERAR SIMULADO
