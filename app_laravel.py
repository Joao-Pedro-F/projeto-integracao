import os
import time
from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine 
from routes.web import registrar_rotas

# func para ativar o NEONDB 
def aguardar_banco():
    url = os.getenv("DATABASE_URL")
    if not url:
        return
    
    print("Verificando se o NeonDB está on")
    for i in range(5):  # Tenta por até 20 segundos (5 vezes x 4 segundos)
        try:
            #  testar conexao
            engine = create_engine(url)
            with engine.connect() as conn:
                print("NeonDB está online!")
                return
        except Exception:
            print(f" Banco off (tentativa {i+1}/5)... esperando 4s")
            time.sleep(4)
    print(" Prosseguindo mesmo sem confirmação do banco...")

# Chama a função antes de carregar as rotas
aguardar_banco()
# ------------------------------------

# Criar aplicacao Flask
app = Flask(__name__)

CORS(app)

# Registrar todas as rotas
registrar_rotas(app)

# Executar aplicacao
if __name__ == '__main__':
    port = int(os.getenv("PORT", "5000"))
    # No Render, é melhor deixar o debug como False em produção
    debug = os.getenv("FLASK_DEBUG", "").strip().lower() in ("1", "true", "yes")
    app.run(host="0.0.0.0", port=port, debug=debug)