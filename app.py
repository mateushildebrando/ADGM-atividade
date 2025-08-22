from config import *
from model import *

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar_pais")
def listar_pais():
    with db_session:
        # obtém as pessoas
        paises = Nacao.select() 
        return render_template("listar_pais.html", paises=paises)

@app.route("/form_adicionar_pais")
def form_adicionar_pais():
    return render_template("form_adicionar_pais.html")

@app.route("/adicionar_pais")
def adicionar_pais():
    # obter os parâmetros
    nome = request.args.get("nome")
    populacao = request.args.get("populacao")
    pib = request.args.get("pib")
    pib_per_capita = request.args.get("pib_per_capita")
    continente = request.args.get("continente")
    idiomas = request.args.get("idiomas")
    moeda = request.args.get("moeda")
    area = request.args.get("area")
    capital = request.args.get("capital")
    governo = request.args.get("governo")
    # salvar
    with db_session:
        # criar a pessoa
        p = Nacao(**request.args)
        # salvar
        commit()
        # encaminhar de volta para a listagem
        return redirect("listar_pais") 

'''
run:
$ flask run
'''