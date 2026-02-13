# Controller de Disciplinas (PARA OS ALUNOS DESENVOLVEREM)
from flask import render_template, request, jsonify
from database.database import conectar

class DisciplinaController:
    
    # INDEX - Exibir página de listagem
    def index(self):
        return render_template('disciplinas/index.html')
    
    # CREATE - Exibir formulário de cadastro
    def create(self):
        return render_template('disciplinas/create.html')  
    
    # STORE - Salvar nova disciplina no banco
    def store(self):
        dados=request.get_json
        banco=None

        try:
            banco.conectar()
            cursor=banco.cursor()
            sql='''INSERT INTO disciplina
                    (nome,carga_horaria,descricao) VALUES (%s,%s,%s)'''
            
            valores=(
                dados['nome'],
                dados['carga_horaria'],
                dados['descricao']

            )
            cursor.execute(sql,valores)
            banco.commit()
            cursor.close()

            return jsonify({'mensagem':'Disciplina criada com sucesso'}),201
        except Exception as e:
            if banco:
                banco.rollback()
            return jsonify({'erro':str(e)}),500
        finally:
            if banco:
                banco.close()
    
    # SHOW - Exibir detalhes de uma disciplina
    def show(self, id):
        pass
    
    # EDIT - Exibir formulário de edição
    def edit(self, id):
        pass
    
    # UPDATE - Atualizar disciplina no banco
    def update(self, id):
        pass
    
    # DESTROY - Deletar disciplina do banco
    def destroy(self, id):
        pass
    
    # API - Listar todas as disciplinas
    def listar(self):
        pass
    
    # API - Buscar uma disciplina específica
    def buscar(self, id):
        pass
