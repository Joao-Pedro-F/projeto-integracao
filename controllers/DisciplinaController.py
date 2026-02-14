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
        return render_template('disciplinas/show.html')
    
    # EDIT - Exibir formulário de edição
    def edit(self, id):
        return render_template('disciplinas/edit.html')
    
    # UPDATE - Atualizar disciplina no banco
    def update(self, id):
        dados= request.get_json()
        banco=None

        try:
            banco=conectar()
            cursor=banco.cursor()
            sql='''UPDATE disciplina SET nome=%s, carga_horaria=%s, descricao=%s WHERE id=%s'''
            valores=(
                dados['nome'],
                dados['carga_horaria'],
                dados['descricao'],
                id
            )
            cursor.execute(sql,valores)
            banco.commit()
            cursor.close()
            return jsonify({'mensagem':'Disciplina atualizada com sucesso'})
        
        except Exception as e:
            if banco:
                banco.rollback()
                return jsonify({'erro':str(e)}),500
        
        finally:
            if banco:
                banco.close()
    
    # DESTROY - Deletar disciplina do banco
    def destroy(self, id):
        banco=None
        try:
            banco=conectar()
            cursor=banco.cursor()
            cursor.execute('DELETE FROM disciplina WHERE id= %s',(id,))
            banco.commit()
            cursor.close()
            return jsonify({'mensagem':'Disciplina deletada com sucesso'})
        
        except Exception as e:
            if banco:
                banco.rollback()
                return jsonify({'erro':str(e)}),500
        
        finally:
            if banco:
                banco.close()
            
        
    
    # API - Listar todas as disciplinas
    def listar(self):
        banco=conectar()
        socorro=banco.cursor() #cursor para executar a consulta
        socorro.execute('SELECT * FROM disciplina') #executar a consulta
        porque_tantos_bugs=[desc[0] for desc in socorro.description] #obter os nomes das colunas
        confundi_todos_os_nomes=socorro.fetchall() #obter os dados
        disciplinas=[dict(zip(porque_tantos_bugs,row)) for row in confundi_todos_os_nomes] #combinar colunas e dados em dicionários
        socorro.close()
        banco.close()
        return jsonify(disciplinas) 


    
    # API - Buscar uma disciplina específica
    def buscar(self, id):
        banco=conectar()
        cursor=banco.cursor()
        cursor.execute('SELECT * FROM disciplina WHERE id=%s',(id,))
        resultado=cursor.fetchone()

        if resultado:
            colunas=[desc[0] for desc in cursor.description]
            disciplinas= dict(zip(colunas,resultado))
        else:
            disciplinas=None
        
        cursor.close()
        banco.close()
        return jsonify(disciplinas)
        
