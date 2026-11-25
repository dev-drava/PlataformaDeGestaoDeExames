from connect_db import start_connection



def criar_questao(texto, tipo, opcoes_json, resposta_correta, dificuldade, disciplina):
    mydb = start_connection()
    mycursor = mydb.cursor()

    sql = """
        insert into questoes
        (texto, tipo, opcoes_json, resposta_correta, dificuldade, disciplina)
        values (%s, %s, %s, %s, %s, %s)
    """
    valores = (texto, tipo, opcoes_json, resposta_correta, dificuldade, disciplina)

    mycursor.execute(sql, valores)
    mydb.commit()
    novo_id = mycursor.lastrowid

    mycursor.close()
    mydb.close()
    return novo_id


def listar_questoes():
    mydb = start_connection()
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("select * from questoes")
    resultado = mycursor.fetchall()

    mycursor.close()
    mydb.close()
    return resultado


def buscar_questao(questao_id):
    mydb = start_connection()
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("select * from questoes where id %s", (questao_id))
    resultado = mycursor.fetchone()

    mycursor.close()
    mydb.close()
    return resultado


def atualizar_questao(texto, tipo, opcoes_json, resposta_correta, dificuldade, disciplina, questao_id):
    mydb = start_connection()
    mycursor = mydb.cursor()

    sql = """
        set texto = %s, tipo = %s, opcoes_json = %s, resposta_correta = %s,
            dificuldade = %s, disciplina = %s
        where id = %s
    """
    valores = (texto, tipo, opcoes_json, resposta_correta, dificuldade, disciplina, questao_id)

    mycursor.execute(sql, valores)
    mydb.commit()

    mycursor.close()
    mydb.close()

def apagar_questao(questao_id):
    mydb = start_connection()
    mycursor = mydb.cursor()

    mycursor.execute("delete from questoes where id = %s", (questao_id))
    mydb.commit()

    mycursor.close()
    mydb.close()


def criar_exame(titulo, data_hora_inicio, duracao_minutos, criado_por):
    mydb = start_connection()
    mycursor = mydb.cursor()

    sql = """
        insert into exames (titulo, data_hora_inicio, duracao_minutos, criado_por)
        values (%s, %s, %s, %s)
    """
    valores = (titulo, data_hora_inicio, duracao_minutos, criado_por)

    mycursor.execute(sql, valores)
    mydb.commit()
    novo_id = mycursor.lastrowid

    mycursor.close()
    mydb.close()
    return novo_id

def listar_exames():
    mydb = start_connection()
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("select * from exames")
    resultado = mycursor.fetchall()

    mycursor.close()
    mydb.close()
    return resultado


def buscar_exame(exame_id):
    mydb = start_connection()
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("select * from exames where id = %s", (exame_id,))
    resultado = mycursor.fetchone()

    mycursor.close()
    mydb.close()
    return resultado


def atualizar_exame(exame_id, titulo, data_hora_inicio, duracao_minutos, criado_por):
    mydb = start_connection()
    mycursor = mydb.cursor()

    sql = """
        update exames
        set titulo = %s, data_hora_inicio = %s, duracao_minutos = %s, criado_por = %s
        where id = %s
    """
    valores = (titulo, data_hora_inicio, duracao_minutos, criado_por, exame_id)

    mycursor.execute(sql, valores)
    mydb.commit()

    mycursor.close()
    mydb.close()


def apagar_exame(exame_id):
    mydb = start_connection()
    mycursor = mydb.cursor()

    mycursor.execute("delete from exames where id = %s", (exame_id,))
    mydb.commit()

    mycursor.close()
    mydb.close()




def adicionar_questao_ao_exame(exame_id, questao_id, pontuacao, ordem):
    mydb = start_connection()
    mycursor = mydb.cursor()

    sql = """
        insert into exame_questoes (exame_id, questao_id, pontuacao, ordem)
        values (%s, %s, %s, %s)
    """
    valores = (exame_id, questao_id, pontuacao, ordem)

    mycursor.execute(sql, valores)
    mydb.commit()

    mycursor.close()
    mydb.close()


def listar_questoes_do_exame(exame_id):
    mydb = start_connection()
    mycursor = mydb.cursor(dictionary=True)

    sql = """
        select exame_questoes.*, questoes.texto, questoes.tipo, questoes.opcoes_json, questoes.resposta_correta
        from exame_questoes
        join questoes on exame_questoes.questao_id = questoes.id
        where exame_questoes.exame_id = %s
        order by exame_questoes.ordem asc
    """
    mycursor.execute(sql, (exame_id,))
    resultado = mycursor.fetchall()

    mycursor.close()
    mydb.close()
    return resultado


def remover_questao_do_exame(exame_id, questao_id):
    mydb = start_connection()
    mycursor = mydb.cursor()

    mycursor.execute(
        "delete from exame_questoes where exame_id = %s and questao_id = %s", (exame_id, questao_id)
    )
    mydb.commit()

    mycursor.close()
    mydb.close()

