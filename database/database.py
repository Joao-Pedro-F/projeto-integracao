# Arquivo de configuração e conexão com banco de dados
import psycopg

# String de conexão Neon PostgreSQL
DATABASE_URL = 'postgresql://neondb_owner:npg_m0ZpALNQ5Rct@ep-quiet-king-ac16a4rs-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

# Função para conectar ao banco
def conectar():
    conexao = psycopg.connect(DATABASE_URL)
    return conexao
