from flask import current_app as app
from flask import render_template, request

from .utils import simulate_risk_analysis


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # Capturando todos os dados do formulário em um dicionário
        dados_form = dict(request.form)

        # Passando o dicionário para a função de processamento
        result, image_base64 = simulate_risk_analysis(dados_form)

        return render_template("resultado.html", result=result, image_base64=image_base64)
    return render_template("index.html")
