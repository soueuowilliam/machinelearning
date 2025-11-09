import pandas as pd
import numpy as np
from sklearn.compose import make_column_transformer
from sklearn.dummy import DummyClassifier
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import plotly.express as px

#DEFININDO A VARIÁVEL DADOS COM AS INFORMAÇÕES DO DOCUMENTO.
dados = pd.read_csv('/content/marketing_investimentoI.csv')


x = dados.drop('aderencia_investimento', axis = 1) #DEFININDO A VARIÁVEL X COMO FEATURES PARA CLASSIFICAÇÃO.
y = dados['aderencia_investimento'] #DEFININDO A VARIÁVEL Y COM VARIÁVEL DE RESPOSTA.

colunas = x.columns #RESERVANDO AS INFORMAÇÕES DAS FEATURES.
features = ['estado_civil', 'escolaridade', 'fez_emprestimo', 'inadimplencia'] #DEFININDO AS CARACTERÍSTICAS PARA CLASSIFICAÇÃO

# NESTE BLOCO, VAMOS UTILIZAR ONE HOT ENCODER PARA TRANSFORMAR AS COLUNAS NÃO NUMÉRICAS PARA BINÁRIO.
# EM PARALELO A ISSO, AS COLUNAS COM MAIS DE DUAS CARACTERÍSTICA, VAMOS SEPARAR ESSAS INFORMAÇÕES POR COLUNAS.
# EX: ESTADO CIVIL EXISTEM 3 INFORMAÇÕES ( CASADO, SOLTEIRO E DIVORCIADO )
# CADA CARACTERÍSTICA TERÁ SUA PRÓPRIA COLUNA, COM DADOS BINÁRIOS, PARA QUE SEJA MELHOR ENTENDIDO EM NOSSO MODELO.
encoder = (OneHotEncoder(drop = 'if_binary', sparse_output = False), features)
one_hot = make_column_transformer(encoder, remainder = 'passthrough', sparse_threshold = 0)
x = one_hot.fit_transform(x)
novas_colunas = one_hot.get_feature_names_out(colunas)

# TRANSFORMANDO AS VARIÁVEIS DE RESPOSTA PARA BINÁRIO.
label = LabelEncoder()
y = label.fit_transform(y)


SEED = 42 #DEFININDO UM NÚMERO PARA SER UTILIZADO NO RANDOM_STATE PARA QUE NÃO ALTERE O RESULTADO DO MODELO.
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, random_state = SEED, stratify = y) #DEFININDO OS DADOS DE TREINO E TESTE.

#DUMMY SERÁ NOSSO MODELO BASE PARA ENTENDER O QUÃO ACERTIVO OS OUTROS MODELOS DEVEM SER.
#SÓ UTILIZAREMOS DOIS MODELOS PARA REALIZAR A CLASSIFICAÇÃO, MAS PODERÍAMOS UTILIZAR MAIS OUTROS MODELOS PARA COMPARAÇÃO E BUSCAR O MELHOR RESULTADO.
dummy = DummyClassifier()
dummy.fit(treino_x, treino_y)
previsao = dummy.predict(teste_x)
dummy_acc = f'DummyClassifier: {accuracy_score(teste_y, previsao) * 100:.2f}%'
teste_dummy = dummy.score(treino_x, treino_y) #VERIFICANDO SE O MODELO ESTÁ DECORANDO OU APRENDENDO COM O TREINAMENTO.

arvore = DecisionTreeClassifier(max_depth = 3, random_state = SEED)
arvore.fit(treino_x, treino_y)
previsao = arvore.predict(teste_x)
arvore_acc = f'Árvore de Decisão: {accuracy_score(teste_y, previsao) * 100:.2f}%'
teste_arvore = arvore.score(treino_x, treino_y) #VERIFICANDO SE O MODELO ESTÁ DECORANDO OU APRENDENDO COM O TREINAMENTO.

#SALVANDO OS MODELOS EM UM DOCUMENTO PARA SEREM UTILIZADOS EM PRODUÇÃO.
with open('modelo_onehot.pkl', 'wb') as arquivo:
  pickle.dump(one_hot, arquivo)
  
with open('modelo_arvore.pkl', 'wb') as arquivo:
  pickle.dump(arvore, arquivo)
