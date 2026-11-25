from connect_db import start_connection



def criar_aluno(numero_aluno, nome, email, turma):
    mydb = start_connection()
    mycursor = mydb.cursor()

    sql = """
        insert into alunos (numero_aluno, nome, email, turma)
        values (%s, %s, %s, %s)
    """
    valores = (numero_aluno, nome, email, turma)

    mycursor.execute(sql, valores)
    mydb.commit()
    novo_id = mycursor.lastrowid

    mycursor.close()
    mydb.close()
    return novo_id


def listar_alunos(turma=None):
    mydb = start_connection()
    mycursor = mydb.cursor(dictionary=True)

    if turma:
        mycursor.execute("select * from alunos where turma = %s", (turma))
    else:
        mycursor.execute("select * from alunos")

    resultado = mycursor.fetchall()

    mycursor.close()
    mydb.close()
    return resultado


def buscar_aluno(aluno_id):
    mydb = start_connection()
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("select * from alunos where id = %s", (aluno_id))
    resultado = mycursor.fetchone()

    mycursor.close()
    mydb.close()
    return resultado



def criar_submissao(exame_id, aluno_id, data_submissao, pontuacao_total=0, estado="em_andamento"):
    mydb = start_connection()
    mycursor = mydb.cursor()

    sql = """
        insert into submissoes_exames
        (exame_id, aluno_id, data_submissao, pontuacao_total, estado)
        values (%s, %s, %s, %s, %s)
    """
    valores = (exame_id, aluno_id, data_submissao, pontuacao_total, estado)

    mycursor.execute(sql, valores)
    mydb.commit()
    novo_id = mycursor.lastrowid

    mycursor.close()
    mydb.close()
    return novo_id


def atualizar_submissao(submissao_id, pontuacao_total, estado):
    mydb = start_connection()
    mycursor = mydb.cursor()

    sql = """
        update submissoes_exames
        set pontuacao_total = %s, estado = %s where id = %s
    """
    valores = (submissao_id, pontuacao_total, estado)
    mycursor.execute(sql, valores)
    mydb.commit()

    mycursor.close()
    mydb.close()

def buscar_submissao(submissao_id):
    mydb = start_connection()
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("select * from submissoes_exames where id = %s", (submissao_id))
    resultado = mycursor.fetchone()

    mycursor.close()
    mydb.close()
    return resultado


def registar_resposta(submissao_id, questao_id, resposta_dada, pontuacao_atribuida=0):
    mydb = start_connection()
    mycursor = mydb.cursor()

    sql = """
        insert into respostas (submissao_id, questao_id, resposta_dada, pontuacao_atribuida=0)
        values (%s, %s, %s, %s)
    """
    valores = (submissao_id, questao_id, resposta_dada, pontuacao_atribuida)

    mycursor.execute(sql, valores)
    mydb.commit()
    novo_id = mycursor.lastrowid

    mycursor.close()
    mydb.close()
    return novo_id


def listar_respostas_da_submissao(submissao_id):
    mydb = start_connection()
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("select * from respostas where submissao_id = %s", (submissao_id))
    resultado = mycursor.fetchall()

    mycursor.close()
    mydb.close()
    return resultado

