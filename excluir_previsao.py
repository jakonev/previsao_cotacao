import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor

# Carregar os dados
dados = pd.read_csv('data.csv')

# Converter a coluna 'data_compra' para datetime
dados['DATA_PREGAO'] = pd.to_datetime(dados['DATA_PREGAO'])

# Calcular o número de dias desde a data mais antiga até cada data de compra
DIF_PRECO = dados['PRE-ABE']
dados['DIF_COTACAO'] = (dados['PRE-ABE'].max() - dados['PRE-ULT'].min())

# Codificar variáveis categóricas
label_encoder = LabelEncoder()
dados['CODNEG'] = label_encoder.fit_transform(dados['CODNEG'])

# Selecionar variáveis relevantes
variaveis = ['VOLT-TOTAL', 'PREMED', 'PRE-OFV', 'PRE-ULT', 'PRE-ABE']

# Dividir os dados em conjunto de treinamento e teste
X = dados[variaveis]
y = dados['PREMED']
X['PREMED'] += dados['PRE-ULT'].min()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de classificação
# modelo = RandomForestClassifier(n_estimators=100, random_state=42)
# modelo.fit(X_train, y_train)
modelo = DecisionTreeRegressor(random_state=42)
modelo.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
previsoes = modelo.predict(X_test)

# Avaliar a precisão do modelo
tabela = (X, previsoes)
print(tabela)

# Calcular a correlação entre o número de dias desde a data de referência e a variável de churn
correlacao_abertura = dados['PREMED'].corr(dados['PRE-OFV'])

# Visualizar a correlação
print(f"Correlação PREMED e Oferta Venda: {correlacao_abertura:,.4f}")

print(X_train)
