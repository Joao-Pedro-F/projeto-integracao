from flask import jsonify, render_template, request

from database.database import conectar


class DisciplinaController:
    # INDEX - Exibir pagina de listagem
    def index(self):
        return render_template("disciplina/index.html")

    # CREATE - Exibir formulario de cadastro
    def create(self):
        return render_template("disciplina/create.html")

    # STORE - Salvar nova disciplina no banco
    def store(self):
        banco = None
        try:
            dados = request.get_json()
            banco = conectar()
            cursor = banco.cursor()

            sql = """INSERT INTO disciplina
                     (nome, carga_horaria, descricao)
                     VALUES (%s, %s, %s)"""
            valores = (
                dados.get("nome"),
                dados.get("carga_horaria"),
                dados.get("descricao"),
            )

            cursor.execute(sql, valores)
            banco.commit()
            cursor.close()
            return jsonify({"mensagem": "Disciplina criada com sucesso!"}), 201
        except Exception as e:
            if banco:
                banco.rollback()
            return jsonify({"erro": str(e)}), 500
        finally:
            if banco:
                banco.close()

    # SHOW - Exibir detalhes de uma disciplina
    def show(self, id):
        return render_template("disciplina/show.html")

    # EDIT - Exibir formulario de edicao
    def edit(self, id):
        return render_template("disciplina/edit.html")

    # UPDATE - Atualizar disciplina no banco
    def update(self, id):
        banco = None
        try:
            dados = request.get_json()
            banco = conectar()
            cursor = banco.cursor()

            sql = """UPDATE disciplina
                     SET nome=%s, carga_horaria=%s, descricao=%s
                     WHERE id=%s"""
            valores = (
                dados.get("nome"),
                dados.get("carga_horaria"),
                dados.get("descricao"),
                id,
            )

            cursor.execute(sql, valores)
            banco.commit()
            cursor.close()
            return jsonify({"mensagem": "Disciplina atualizada com sucesso!"})
        except Exception as e:
            if banco:
                banco.rollback()
            return jsonify({"erro": str(e)}), 500
        finally:
            if banco:
                banco.close()

    # DESTROY - Deletar disciplina do banco
    def destroy(self, id):
        banco = None
        try:
            banco = conectar()
            cursor = banco.cursor()
            cursor.execute("DELETE FROM disciplina WHERE id=%s", (id,))
            banco.commit()
            cursor.close()
            return jsonify({"mensagem": "Disciplina deletada com sucesso!"})
        except Exception as e:
            if banco:
                banco.rollback()
            return jsonify({"erro": str(e)}), 500
        finally:
            if banco:
                banco.close()

    # API - Listar todas as disciplinas
    def listar(self):
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM disciplina")
        colunas = [desc[0] for desc in cursor.description]
        resultados = cursor.fetchall()
        disciplinas = [dict(zip(colunas, row)) for row in resultados]

        cursor.close()
        banco.close()
        return jsonify(disciplinas)

    # API - Buscar uma disciplina especifica
    def buscar(self, id):
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM disciplina WHERE id=%s", (id,))
        resultado = cursor.fetchone()

        if resultado:
            colunas = [desc[0] for desc in cursor.description]
            disciplina = dict(zip(colunas, resultado))
        else:
            disciplina = None

        cursor.close()
        banco.close()
        return jsonify(disciplina)
