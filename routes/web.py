from flask import render_template

from controllers.AlunoController import AlunoController
from controllers.DisciplinaController import DisciplinaController
from controllers.EscolaController import EscolaController
from controllers.ProfessorController import ProfessorController


aluno_controller = AlunoController()
professor_controller = ProfessorController()
disciplina_controller = DisciplinaController()
escola_controller = EscolaController()


def admin_index():
    return render_template("admin/index.html")


def registrar_rotas(app):
    # Dashboard/Admin
    app.add_url_rule("/", "admin.index", admin_index)
    app.add_url_rule("/admin", "admin.dashboard", admin_index)

    # Paginas de alunos
    app.add_url_rule("/alunos", "alunos.index", aluno_controller.index)
    app.add_url_rule("/alunos/create", "alunos.create", aluno_controller.create)
    app.add_url_rule("/alunos/<int:id>", "alunos.show", aluno_controller.show)
    app.add_url_rule("/alunos/<int:id>/edit", "alunos.edit", aluno_controller.edit)

    # Paginas de professores
    app.add_url_rule("/professores", "professores.index", professor_controller.index)
    app.add_url_rule("/professores/create", "professores.create", professor_controller.create)
    app.add_url_rule("/professores/<int:id>", "professores.show", professor_controller.show)
    app.add_url_rule("/professores/<int:id>/edit", "professores.edit", professor_controller.edit)

    # Paginas de disciplinas
    app.add_url_rule("/disciplinas", "disciplinas.index", disciplina_controller.index)
    app.add_url_rule("/disciplinas/create", "disciplinas.create", disciplina_controller.create)
    app.add_url_rule("/disciplinas/<int:id>", "disciplinas.show", disciplina_controller.show)
    app.add_url_rule("/disciplinas/<int:id>/edit", "disciplinas.edit", disciplina_controller.edit)

    
    app.add_url_rule("/disciplina", "disciplina.index", disciplina_controller.index)
    app.add_url_rule("/disciplina/create", "disciplina.create", disciplina_controller.create)
    app.add_url_rule("/disciplina/<int:id>", "disciplina.show", disciplina_controller.show)
    app.add_url_rule("/disciplina/<int:id>/edit", "disciplina.edit", disciplina_controller.edit)

    # Paginas de escolas
    app.add_url_rule("/escolas", "escolas.index", escola_controller.index)
    app.add_url_rule("/escolas/create", "escolas.create", escola_controller.create)
    app.add_url_rule("/escolas/<int:id>", "escolas.show", escola_controller.show)
    app.add_url_rule("/escolas/<int:id>/edit", "escolas.edit", escola_controller.edit)

   
    app.add_url_rule("/escola", "escola.index", escola_controller.index)
    app.add_url_rule("/escola/create", "escola.create", escola_controller.create)
    app.add_url_rule("/escola/<int:id>", "escola.show", escola_controller.show)
    app.add_url_rule("/escola/<int:id>/edit", "escola.edit", escola_controller.edit)

    # API de alunos
    app.add_url_rule("/api/alunos", "api.alunos.index", aluno_controller.listar, methods=["GET"])
    app.add_url_rule("/api/alunos", "api.alunos.store", aluno_controller.store, methods=["POST"])
    app.add_url_rule("/api/alunos/<int:id>", "api.alunos.show", aluno_controller.buscar, methods=["GET"])
    app.add_url_rule("/api/alunos/<int:id>", "api.alunos.update", aluno_controller.update, methods=["PUT"])
    app.add_url_rule("/api/alunos/<int:id>", "api.alunos.destroy", aluno_controller.destroy, methods=["DELETE"])

    # API de professores
    app.add_url_rule("/api/professores", "api.professores.index", professor_controller.listar, methods=["GET"])
    app.add_url_rule("/api/professores", "api.professores.store", professor_controller.store, methods=["POST"])
    app.add_url_rule("/api/professores/<int:id>", "api.professores.show", professor_controller.buscar, methods=["GET"])
    app.add_url_rule("/api/professores/<int:id>", "api.professores.update", professor_controller.update, methods=["PUT"])
    app.add_url_rule("/api/professores/<int:id>", "api.professores.destroy", professor_controller.destroy, methods=["DELETE"])

    # API de disciplinas 
    app.add_url_rule("/api/disciplinas", "api.disciplinas.index", disciplina_controller.listar, methods=["GET"])
    app.add_url_rule("/api/disciplinas", "api.disciplinas.store", disciplina_controller.store, methods=["POST"])
    app.add_url_rule("/api/disciplinas/<int:id>", "api.disciplinas.show", disciplina_controller.buscar, methods=["GET"])
    app.add_url_rule("/api/disciplinas/<int:id>", "api.disciplinas.update", disciplina_controller.update, methods=["PUT"])
    app.add_url_rule("/api/disciplinas/<int:id>", "api.disciplinas.destroy", disciplina_controller.destroy, methods=["DELETE"])

    # API de disciplinas 
    app.add_url_rule("/api/disciplina", "api.disciplina.index", disciplina_controller.listar, methods=["GET"])
    app.add_url_rule("/api/disciplina", "api.disciplina.store", disciplina_controller.store, methods=["POST"])
    app.add_url_rule("/api/disciplina/<int:id>", "api.disciplina.show", disciplina_controller.buscar, methods=["GET"])
    app.add_url_rule("/api/disciplina/<int:id>", "api.disciplina.update", disciplina_controller.update, methods=["PUT"])
    app.add_url_rule("/api/disciplina/<int:id>", "api.disciplina.destroy", disciplina_controller.destroy, methods=["DELETE"])

    # API de escolas 
    app.add_url_rule("/api/escolas", "api.escolas.index", escola_controller.listar, methods=["GET"])
    app.add_url_rule("/api/escolas", "api.escolas.store", escola_controller.store, methods=["POST"])
    app.add_url_rule("/api/escolas/<int:id>", "api.escolas.show", escola_controller.buscar, methods=["GET"])
    app.add_url_rule("/api/escolas/<int:id>", "api.escolas.update", escola_controller.update, methods=["PUT"])
    app.add_url_rule("/api/escolas/<int:id>", "api.escolas.destroy", escola_controller.destroy, methods=["DELETE"])

    # API de escolas 
    app.add_url_rule("/api/escola", "api.escola.index", escola_controller.listar, methods=["GET"])
    app.add_url_rule("/api/escola", "api.escola.store", escola_controller.store, methods=["POST"])
    app.add_url_rule("/api/escola/<int:id>", "api.escola.show", escola_controller.buscar, methods=["GET"])
    app.add_url_rule("/api/escola/<int:id>", "api.escola.update", escola_controller.update, methods=["PUT"])
    app.add_url_rule("/api/escola/<int:id>", "api.escola.destroy", escola_controller.destroy, methods=["DELETE"])
