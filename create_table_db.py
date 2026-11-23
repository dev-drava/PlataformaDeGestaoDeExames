from connect_db import start_connection

mydb = start_connection()
mycursor = mydb.cursor()

mycursor.execute("""
    create table if not exists questoes (
        id int auto_increment primary key,
        texto text not null,
        tipo varchar(50) not null,
        opcoes_json text not null,
        resposta_correta text not null,
        dificuldade text not null,
        disciplina text not null
    )
""")

mycursor.execute("""
    create table if not exists exames (
        id int auto_increment primary key,
        titulo text not null,
        data_hora_inicio date,
        duracao_minutos int not null,
        criado_por varchar(120) not null
    )
""")

mycursor.execute("""
    create table if not exists exame_questoes (
        id int auto_increment primary key,
        exame_id int not null,
        questao_id int not null,
        pontuacao decimal(6,2) not null,
        ordem int not null,
        foreign key (exame_id) references exames(id),
        foreign key (questao_id) references questoes(id)
    )
""")

mycursor.execute("""
    create table if not exists alunos (
        id int not null auto_increment primary key,
        numero_aluno int not null,
        nome varchar(120) not null,
        email varchar(50) not null,
        turma text not null
    )
""")

mycursor.execute("""
    create table if not exists submissoes_exames (
        id int not null auto_increment primary key,
        exame_id int not null,
        aluno_id int not null,
        data_submissao date not null,
        pontuacao_total decimal(6,2) not null,
        estado text not null,
        foreign key (exame_id) references exames(id),
        foreign key (aluno_id) references alunos(id)
    )
""")

mycursor.execute("""
    create table if not exists respostas (
        id int not null auto_increment primary key,
        submissao_id int not null,
        questao_id int not null,
        resposta_dada text not null,
        pontuacao_atribuida decimal(6,2) not null,
        foreign key (submissao_id) references submissoes_exames(id),
        foreign key (questao_id) references questoes(id)
    )
""")

mydb.commit()
mycursor.close()
mydb.close()