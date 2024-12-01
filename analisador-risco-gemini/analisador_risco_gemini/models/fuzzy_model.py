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
risco = ctrl.Consequent(np.arange(0, 100, 1), 'risco')


###### DEFINIÇÃO DAS FUNÇÕES DE PERTINÊNCIA ######
# Experiência
experiencia['baixa'] = fuzz.zmf(experiencia.universe, 1, 4)
experiencia['media'] = fuzz.trimf(experiencia.universe, [3, 5, 7])
experiencia['alta'] = fuzz.smf(experiencia.universe, 6, 10)

# Entrosamento
entrosamento['baixo'] = fuzz.zmf(entrosamento.universe, 0, 3)
entrosamento['medio'] = fuzz.trapmf(entrosamento.universe, [2, 4, 6, 8])
entrosamento['alto'] = fuzz.smf(entrosamento.universe, 6, 10)

# Rotatividade (com interseção)
rotatividade['baixa'] = fuzz.zmf(rotatividade.universe, 0, 20)
rotatividade['moderada'] = fuzz.trapmf(rotatividade.universe, [15, 25, 45, 50])
rotatividade['alta'] = fuzz.smf(rotatividade.universe, 40, 100)

# Definição de requisitos (com gaussiana)
definicao_requisitos['mal_definida'] = fuzz.zmf(definicao_requisitos.universe, 0, 4)
definicao_requisitos['moderada'] = fuzz.trapmf(definicao_requisitos.universe, [3, 5, 7, 8])
definicao_requisitos['bem_definida'] = fuzz.smf(definicao_requisitos.universe, 7, 10)

# Mudanças nos requisitos (com sigmoide)
mudancas_requisitos['baixas'] = fuzz.zmf(mudancas_requisitos.universe, 0, 20)
mudancas_requisitos['moderadas'] = fuzz.trimf(mudancas_requisitos.universe, [15, 35, 70])
mudancas_requisitos['altas'] = fuzz.smf(mudancas_requisitos.universe, 60, 100)

# Complexidade Técnica
complexidade_tecnica['baixa'] = fuzz.zmf(complexidade_tecnica.universe, 0, 3)
complexidade_tecnica['media'] = fuzz.trapmf(complexidade_tecnica.universe, [2, 4, 6, 8])
complexidade_tecnica['alta'] = fuzz.smf(complexidade_tecnica.universe, 6, 10)

# Tamanho do Projeto
tamanho_projeto['pequeno'] = fuzz.zmf(tamanho_projeto.universe, 0, 30)
tamanho_projeto['medio'] = fuzz.trapmf(tamanho_projeto.universe, [20, 40, 60, 80])
tamanho_projeto['grande'] = fuzz.smf(tamanho_projeto.universe, 60, 100)

# Prazo
prazo['curto'] = fuzz.zmf(prazo.universe, 1, 6)
prazo['moderado'] = fuzz.trapmf(prazo.universe, [5, 10, 15, 20])
prazo['longo'] = fuzz.smf(prazo.universe, 16, 36)

# Comunicação
comunicacao['ruim'] = fuzz.zmf(comunicacao.universe, 0, 3)
comunicacao['boa'] = fuzz.trapmf(comunicacao.universe, [2, 4, 6, 8])
comunicacao['otima'] = fuzz.smf(comunicacao.universe, 6, 10)

# Maturidade das Ferramentas
maturidade_ferramentas['imatura'] = fuzz.zmf(maturidade_ferramentas.universe,0, 3)
maturidade_ferramentas['moderada'] = fuzz.trimf(maturidade_ferramentas.universe, [2, 5, 7])
maturidade_ferramentas['alta'] = fuzz.smf(maturidade_ferramentas.universe, 6, 10)

# Impacto do Ambiente Externo
impacto_ambiente_externo['baixo'] = fuzz.zmf(impacto_ambiente_externo.universe, 0, 1)
impacto_ambiente_externo['moderado'] = fuzz.trapmf(impacto_ambiente_externo.universe, [2, 4, 6, 7])
impacto_ambiente_externo['alto'] = fuzz.smf(impacto_ambiente_externo.universe, 6, 10)

# Orçamento Disponível
orcamento['baixo'] = fuzz.zmf(orcamento.universe, 5000, 20000)
orcamento['adequado'] = fuzz.trapmf(orcamento.universe, [20000, 30000, 70000, 80000])
orcamento['excedente'] = fuzz.smf(orcamento.universe, 70000, 100000)

# Risco
risco['baixo'] = fuzz.zmf(risco.universe, 0, 25)
risco['moderado'] = fuzz.trimf(risco.universe, [25, 50, 75])
risco['alto'] = fuzz.trimf(risco.universe, [50, 75, 100])
risco['critico'] = fuzz.smf(risco.universe, 75, 100)

# Definindo os conjuntos fuzzy
###### DEFININDO AS REGRAS ######

rule1 = ctrl.Rule(experiencia['baixa'] & complexidade_tecnica['alta'], risco['alto'])
rule2 = ctrl.Rule(entrosamento['baixo'] | rotatividade['alta'], risco['critico'])
rule3 = ctrl.Rule(definicao_requisitos['mal_definida'] & mudancas_requisitos['altas'], risco['critico'])
rule4 = ctrl.Rule(complexidade_tecnica['media'] & tamanho_projeto['grande'], risco['moderado'])
rule5 = ctrl.Rule(prazo['curto'] & mudancas_requisitos['altas'], risco['critico'])
rule6 = ctrl.Rule(orcamento['baixo'] & prazo['curto'], risco['alto'])
rule7 = ctrl.Rule(comunicacao['ruim'] | impacto_ambiente_externo['alto'], risco['critico'])
rule8 = ctrl.Rule(maturidade_ferramentas['imatura'] & complexidade_tecnica['alta'], risco['alto'])
rule9 = ctrl.Rule(orcamento['adequado'] & prazo['moderado'] & comunicacao['boa'], risco['moderado'])
rule10 = ctrl.Rule(definicao_requisitos['bem_definida'] & experiencia['alta'] & entrosamento['alto'], risco['baixo'])
rule11 = ctrl.Rule(impacto_ambiente_externo['baixo'] & tamanho_projeto['pequeno'] & prazo['longo'], risco['baixo'])
rule12 = ctrl.Rule(mudancas_requisitos['baixas'] & comunicacao['otima'] & orcamento['excedente'], risco['baixo'])
rule13 = ctrl.Rule(experiencia['media'] & complexidade_tecnica['media'], risco['moderado'])

# Novas regras para cobrir os conceitos faltantes

# Experiência Média
rule13 = ctrl.Rule(experiencia['media'] & complexidade_tecnica['media'], risco['moderado'])
rule14 = ctrl.Rule(experiencia['media'] & entrosamento['alto'], risco['baixo'])

# Entrosamento Médio
rule15 = ctrl.Rule(entrosamento['medio'] & rotatividade['baixa'], risco['baixo'])
rule16 = ctrl.Rule(entrosamento['medio'] & complexidade_tecnica['baixa'], risco['baixo'])

# Rotatividade Baixa e Média
rule17 = ctrl.Rule(rotatividade['baixa'] & definicao_requisitos['moderada'], risco['moderado'])
rule18 = ctrl.Rule(rotatividade['moderada'] & mudancas_requisitos['baixas'], risco['baixo'])

# Mudanças de Requisitos Moderadas
rule19 = ctrl.Rule(mudancas_requisitos['moderadas'] & tamanho_projeto['medio'], risco['moderado'])
rule20 = ctrl.Rule(mudancas_requisitos['moderadas'] & comunicacao['boa'], risco['baixo'])

# Complexidade Baixa
rule21 = ctrl.Rule(complexidade_tecnica['baixa'] & tamanho_projeto['pequeno'], risco['baixo'])

# Definição de Requisitos Moderada
rule22 = ctrl.Rule(definicao_requisitos['moderada'] & experiencia['media'], risco['moderado'])

# Tamanho Médio
rule23 = ctrl.Rule(tamanho_projeto['medio'] & complexidade_tecnica['media'], risco['moderado'])

# Maturidade Moderada e Alta
rule24 = ctrl.Rule(maturidade_ferramentas['moderada'] & comunicacao['boa'], risco['baixo'])
rule25 = ctrl.Rule(maturidade_ferramentas['alta'] & complexidade_tecnica['baixa'], risco['baixo'])




# Criando o sistema de controle fuzzy
ctrl_sys = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12,
    rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24,
    rule25
])

risk_simulator = ctrl.ControlSystemSimulation(ctrl_sys)


