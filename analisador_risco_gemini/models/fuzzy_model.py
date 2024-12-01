import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

###### DEFINIÇÃO DAS VARIÁVEIS ######

# Variáveis de entrada (antecedentes)
experiencia = ctrl.Antecedent(np.arange(1, 11, 1), 'experiencia')
entrosamento = ctrl.Antecedent(np.arange(0, 11, 1), 'entrosamento')
rotatividade = ctrl.Antecedent(np.arange(0, 101, 1), 'rotatividade')
definicao_requisitos = ctrl.Antecedent(np.arange(0, 11, 1), 'definicao_requisitos')
mudancas_requisitos = ctrl.Antecedent(np.arange(0, 101, 1), 'mudancas_requisitos')
complexidade_tecnica = ctrl.Antecedent(np.arange(0, 11, 1), 'complexidade_tecnica')
tamanho_projeto = ctrl.Antecedent(np.arange(0, 101, 1), 'tamanho_projeto')
prazo = ctrl.Antecedent(np.arange(1, 37, 1), 'prazo')
comunicacao = ctrl.Antecedent(np.arange(0, 11, 1), 'comunicacao')
maturidade_ferramentas = ctrl.Antecedent(np.arange(0, 11, 1), 'maturidade_ferramentas')
impacto_ambiente_externo = ctrl.Antecedent(np.arange(0, 11, 1), 'impacto_ambiente_externo')
orcamento = ctrl.Antecedent(np.arange(5000, 100001, 1), 'orcamento')

# Variável de saída (consequente)
risco = ctrl.Consequent(np.arange(0, 11, 1), 'risco')


###### DEFINIÇÃO DAS FUNÇÕES DE PERTINÊNCIA ######

# Definindo os conjuntos fuzzy
# Experiência
experiencia['baixa'] = fuzz.trimf(experiencia.universe, [1, 1, 4])
experiencia['media'] = fuzz.trimf(experiencia.universe, [3, 5, 7])
experiencia['alta'] = fuzz.trimf(experiencia.universe, [6, 10, 10])

# Entrosamento
entrosamento['baixo'] = fuzz.trimf(entrosamento.universe, [0, 0, 3])
entrosamento['medio'] = fuzz.trapmf(entrosamento.universe, [2, 4, 6, 8])
entrosamento['alto'] = fuzz.trimf(entrosamento.universe, [6, 10, 10])

# Rotatividade (com interseção)
rotatividade['baixa'] = fuzz.trimf(rotatividade.universe, [0, 0, 20])
rotatividade['moderada'] = fuzz.trapmf(rotatividade.universe, [15, 25, 45, 50])
rotatividade['alta'] = fuzz.trimf(rotatividade.universe, [40, 100, 100])

# Definição de requisitos (com gaussiana)
definicao_requisitos['mal_definida'] = fuzz.gaussmf(definicao_requisitos.universe, 2, 1.5)
definicao_requisitos['moderada'] = fuzz.gaussmf(definicao_requisitos.universe, 5, 2)
definicao_requisitos['bem_definida'] = fuzz.gaussmf(definicao_requisitos.universe, 8, 1.5)

# Mudanças nos requisitos (com sigmoide)
mudancas_requisitos['baixas'] = fuzz.zmf(mudancas_requisitos.universe, 20, 5)
mudancas_requisitos['moderadas'] = fuzz.smf(mudancas_requisitos.universe, 30, 20)
mudancas_requisitos['altas'] = fuzz.smf(mudancas_requisitos.universe, 70, 10)

# Complexidade Técnica
complexidade_tecnica['baixa'] = fuzz.trimf(complexidade_tecnica.universe, [0, 0, 3])
complexidade_tecnica['media'] = fuzz.trapmf(complexidade_tecnica.universe, [2, 4, 6, 8])
complexidade_tecnica['alta'] = fuzz.trimf(complexidade_tecnica.universe, [6, 10, 10])

# Tamanho do Projeto
tamanho_projeto['pequeno'] = fuzz.trimf(tamanho_projeto.universe, [0, 0, 30])
tamanho_projeto['medio'] = fuzz.trapmf(tamanho_projeto.universe, [20, 40, 60, 80])
tamanho_projeto['grande'] = fuzz.trimf(tamanho_projeto.universe, [60, 100, 100])

# Prazo
prazo['curto'] = fuzz.trimf(prazo.universe, [1, 1, 6])
prazo['moderado'] = fuzz.trapmf(prazo.universe, [5, 10, 15, 20])
prazo['longo'] = fuzz.trimf(prazo.universe, [16, 36, 36])

# Comunicação
comunicacao['ruim'] = fuzz.trimf(comunicacao.universe, [0, 0, 3])
comunicacao['boa'] = fuzz.trapmf(comunicacao.universe, [2, 4, 6, 8])
comunicacao['otima'] = fuzz.trimf(comunicacao.universe, [6, 10, 10])

# Maturidade das Ferramentas
maturidade_ferramentas['imatura'] = fuzz.zmf(maturidade_ferramentas.universe, 3, 1)
maturidade_ferramentas['moderada'] = fuzz.smf(maturidade_ferramentas.universe, 4, 3)
maturidade_ferramentas['alta'] = fuzz.smf(maturidade_ferramentas.universe, 7, 3)

# Impacto do Ambiente Externo
impacto_ambiente_externo['baixo'] = fuzz.gaussmf(impacto_ambiente_externo.universe, 1, 1)
impacto_ambiente_externo['moderado'] = fuzz.gaussmf(impacto_ambiente_externo.universe, 5, 2)
impacto_ambiente_externo['alto'] = fuzz.gaussmf(impacto_ambiente_externo.universe, 9, 1.5)

# Orçamento Disponível
orcamento['baixo'] = fuzz.trimf(orcamento.universe, [5000, 5000, 20000])
orcamento['adequado'] = fuzz.trapmf(orcamento.universe, [20000, 30000, 70000, 80000])
orcamento['excedente'] = fuzz.trimf(orcamento.universe, [70000, 100000, 100000])


# Risco
risco['baixo'] = fuzz.trimf(risco.universe, [0, 0, 25])
risco['moderado'] = fuzz.trimf(risco.universe, [25, 50, 75])
risco['alto'] = fuzz.trimf(risco.universe, [50, 75, 100])
risco['critico'] = fuzz.trimf(risco.universe, [75, 100, 100])

###### DEFININDO AS REGRAS ######

rule1 = ctrl.Rule(experiencia['baixa'] & complexidade_tecnica['alta'], risco['alto'])
rule2 = ctrl.Rule(entrosamento['baixo'] | rotatividade['alta'], risco['critico'])
rule3 = ctrl.Rule(definicao_requisitos['mal_definida'] & mudancas_requisitos['altas'], risco['critico'])
rule4 = ctrl.Rule(complexidade_tecnica['media'] & tamanho_projeto['grande'], risco['alto'])
rule5 = ctrl.Rule(prazo['curto'] & mudancas_requisitos['altas'], risco['critico'])
rule6 = ctrl.Rule(orcamento['baixo'] & prazo['curto'], risco['alto'])
rule7 = ctrl.Rule(comunicacao['ruim'] | impacto_ambiente_externo['alto'], risco['critico'])
rule8 = ctrl.Rule(maturidade_ferramentas['baixa'] & complexidade_tecnica['alta'], risco['alto'])
rule9 = ctrl.Rule(orcamento['adequado'] & prazo['moderado'] & comunicacao['boa'], risco['moderado'])
rule10 = ctrl.Rule(definicao_requisitos['bem_definida'] & experiencia['alta'] & entrosamento['alta'], risco['baixo'])
rule11 = ctrl.Rule(impacto_ambiente_externo['baixo'] & tamanho_projeto['pequeno'] & prazo['longo'], risco['baixo'])
rule12 = ctrl.Rule(mudancas_requisitos['baixas'] & comunicacao['otima'] & orcamento['excedente'], risco['baixo'])

# Criando o sistema de controle fuzzy
ctrl_sys = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6,
                               rule7, rule8, rule9, rule10, rule11, rule12])

