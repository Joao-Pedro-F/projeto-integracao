import os

# Arquivo principal da aplicacao (tipo Laravel)
from flask import Flask
from flask_cors import CORS
from routes.web import registrar_rotas

# Criar aplicacao Flask
app = Flask(__name__)

CORS(app)

# Registrar todas as rotas
registrar_rotas(app)

# Executar aplicacao
if __name__ == '__main__':
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "").strip().lower() in ("1", "true", "yes")
    app.run(host="0.0.0.0", port=port, debug=debug)