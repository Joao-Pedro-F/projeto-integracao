# Controller de Professores (PARA OS ALUNOS DESENVOLVEREM)
from flask import render_template, request, jsonify
from database.database import conectar

class ProfessorController:
    
    # INDEX - Exibir página de listagem
    def index(self):
        return render_template('professores/index.html')
        
    
    # CREATE - Exibir formulário de cadastro
    def create(self):
        return render_template('professores/create.html')
    
   # STORE - Salvar novo professor no banco
    def store(self):
        banco = None  # Define a variável antes do try para evitar erro de "não definido"
        try:
            dados = request.get_json()
            banco = conectar()
            cursor = banco.cursor()
            
            # SQL ajustado para as colunas reais da sua tabela no Neon
            sql = '''INSERT INTO professor 
                     (nome, cpf, email, telefone, especialidade) 
                     VALUES (%s, %s, %s, %s, %s)'''
            
            valores = (
                dados.get('nome'),
                dados.get('cpf'),
                dados.get('email'),
                dados.get('telefone'),
                dados.get('especialidade')
            )
            
            cursor.execute(sql, valores)
            banco.commit()
            cursor.close()
            
            return jsonify({'mensagem': 'Professor criado com sucesso!'}), 201
            
        except Exception as e:
            if banco:
                banco.rollback()
            print(f"Erro : {e}")
            return jsonify({'erro': str(e)}), 500
            
        finally:
            if banco:
                banco.close()
    
   

    
   
    
    
    
    # SHOW - Exibir detalhes de um professor
    def show(self, id):
        return render_template('professores/show.html')
    
    # EDIT - Exibir formulário de edição
    def edit(self, id):
        return render_template("professores/edit.html")
    
    # UPDATE - Atualizar professor no banco
    def update(self, id):
        dados=request.get_json
        banco=None

        try:
            banco=conectar()
            cursor=banco.cursors()
            sql='''UPDATE professor
                    SET nome=%s,cpf=%s,email=%s,telefone=%s,especialidade=%s
                    WHERE id=%s'''
            valores=(
                dados['nome'],
                dados['cpf'],
                dados['email'],
                dados['telefone'],
                dados['especialidade'],
                id)
                
            cursor.execute(sql,valores)
            banco.commit()
            cursor.close()
            return jsonify({'mensagem':'Professor atualizado com sucesso!'})
        except Exception as e:
            if banco:
                banco.rollback()
            print(f"Erro : {e}")
            return jsonify({'erro':str(e)}),500
        finally:
            if banco:
                banco.close()
        
                
    
    
    # DESTROY - Deletar professor do banco
    def destroy(self, id):
        banco= None
        try:
            banco=conectar()
            cursor=banco.cursor()
            cursor.execute('DELETE FROM professor WHERE id=%s',(id,))
            banco.commit()
            cursor.close()
            return jsonify({'mensagem':'Professor deletado com sucesso!'})
        
        except Exception as e:
            if banco:
                banco.rollback()
                return jsonify({'erro':str(e)}),500
        finally:
            if banco:
                banco.close()
    
    # API - Listar todos os professores
    def listar(self):
        banco=conectar()
        cursor=banco.cursor()

        cursor.execute('SELECT * FROM professor')
        colunas=[desc[0] for desc in cursor.description]
        resultados=cursor.fetchall()
        professores=[dict(zip(colunas,row))for row in resultados]
        cursor.close()
        banco.close()
        return jsonify(professores)
    

       

    
    # API - Buscar um professor específico
    def buscar(self, id):
        banco=conectar()
        cursor=banco.cursor()

        cursor.execute('SELECT * FROM professor WHERE id=%s',(id,))
        resultado=cursor.fetchall

        if resultado:
            colunas=[desc[0] for desc in cursor.description]
            professores= dict(zip(colunas,resultado))
        
        else:
            professores= None

        cursor.close()
        banco.close()   
        return jsonify(professores)

     
