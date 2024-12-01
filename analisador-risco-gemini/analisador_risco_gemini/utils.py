import base64
import io

import matplotlib.pyplot as plt

from .models.fuzzy_model import risco, risk_simulator


def simulate_risk_analysis(input_data: dict):


    # Iterando sobre os dados de entrada e atribuindo os valores ao sistema fuzzy
    for key, value in input_data.items():
        if value:
            # Convertendo o valor para inteiro
            value = int(value)
            # Assumindo que o nome da variável no sistema fuzzy é o mesmo que a chave do dicionário
            risk_simulator.input[key] = value

    # Simulando o sistema fuzzy
    risk_simulator.compute()


    print(risk_simulator.output)

    # Obtendo o valor da saída
    if risk_simulator.output:
        result = round(risk_simulator.output["risco"],2)
    else:
        result = 0

    # Criando a figura e os eixos
    plt.figure()

    # Gerando o plot
    risco.view(sim=risk_simulator)

    # Convertendo a figura para um buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Codificando o buffer em base64
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close()

    return result, image_base64

