from flask import jsonify, render_template, request

from database.database import conectar


class EscolaController:
    # INDEX - Exibir pagina de listagem
    def index(self):
        return render_template("escola/index.html")

    # CREATE - Exibir formulario de cadastro
    def create(self):
        return render_template("escola/create.html")

    # STORE - Salvar nova escola no banco
    def store(self):
        banco = None
        try:
            dados = request.get_json()
            banco = conectar()
            cursor = banco.cursor()

            sql = """INSERT INTO escola
                     (nome, endereco, cidade, telefone)
                     VALUES (%s, %s, %s, %s)"""
            valores = (
                dados.get("nome"),
                dados.get("endereco"),
                dados.get("cidade"),
                dados.get("telefone"),
            )

            cursor.execute(sql, valores)
            banco.commit()
            cursor.close()
            return jsonify({"mensagem": "Escola criada com sucesso!"}), 201
        except Exception as e:
            if banco:
                banco.rollback()
            return jsonify({"erro": str(e)}), 500
        finally:
            if banco:
                banco.close()

    # SHOW - Exibir detalhes de uma escola
    def show(self, id):
        return render_template("escola/show.html")

    # EDIT - Exibir formulario de edicao
    def edit(self, id):
        return render_template("escola/edit.html")

    # UPDATE - Atualizar escola no banco
    def update(self, id):
        banco = None
        try:
            dados = request.get_json()
            banco = conectar()
            cursor = banco.cursor()

            sql = """UPDATE escola
                     SET nome=%s, endereco=%s, cidade=%s, telefone=%s
                     WHERE id=%s"""
            valores = (
                dados.get("nome"),
                dados.get("endereco"),
                dados.get("cidade"),
                dados.get("telefone"),
                id,
            )

            cursor.execute(sql, valores)
            banco.commit()
            cursor.close()
            return jsonify({"mensagem": "Escola atualizada com sucesso!"})
        except Exception as e:
            if banco:
                banco.rollback()
            return jsonify({"erro": str(e)}), 500
        finally:
            if banco:
                banco.close()

    # DESTROY - Deletar escola do banco
    def destroy(self, id):
        banco = None
        try:
            banco = conectar()
            cursor = banco.cursor()
            cursor.execute("DELETE FROM escola WHERE id=%s", (id,))
            banco.commit()
            cursor.close()
            return jsonify({"mensagem": "Escola deletada com sucesso!"})
        except Exception as e:
            if banco:
                banco.rollback()
            return jsonify({"erro": str(e)}), 500
        finally:
            if banco:
                banco.close()

    # API - Listar todas as escolas
    def listar(self):
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM escola")
        colunas = [desc[0] for desc in cursor.description]
        resultados = cursor.fetchall()
        escolas = [dict(zip(colunas, row)) for row in resultados]

        cursor.close()
        banco.close()
        return jsonify(escolas)

    # API - Buscar uma escola especifica
    def buscar(self, id):
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM escola WHERE id=%s", (id,))
        resultado = cursor.fetchone()

        if resultado:
            colunas = [desc[0] for desc in cursor.description]
            escola = dict(zip(colunas, resultado))
        else:
            escola = None

        cursor.close()
        banco.close()
        return jsonify(escola)
