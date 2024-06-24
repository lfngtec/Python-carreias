from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

VAGAS = [{
    'id': 1,
    'titulo': 'Analista de dados',
    'localidade': 'Rio de Janeiro',
    'salario': 'R$3.000'
}, {
    'id': 2,
    'titulo': 'Analista de Infra',
    'localidade': 'São Paulo',
    'salario': 'R$5.000'
}, {
    'id': 3,
    'titulo': 'Analista de Sistemas',
    'localidade': 'Aracajú',
    'salario': 'R$6.000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", vagas=VAGAS)


@app.route("/vagas")
def lista_vagas():
  return jsonify(VAGAS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
