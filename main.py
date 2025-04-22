# main.py
from data import obter_dataset
from model import criar_modelo
from sklearn.model_selection import train_test_split

# Caminho para o CSV com os dados
CAMINHO_CSV = "dataset/dados.csv"

# Carrega e prepara os dados
X, y, encoder_x, encoder_y = obter_dataset(CAMINHO_CSV)

# Divide os dados para treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Redimensiona entrada para ter uma dimensão adicional (necessário para Keras)
import numpy as np
X_train = np.array(X_train).reshape(-1, 1)
X_test = np.array(X_test).reshape(-1, 1)

# Cria o modelo
modelo = criar_modelo(input_dim=1, output_dim=len(set(y)))

# Treina o modelo
modelo.fit(X_train, y_train, epochs=20, batch_size=4, validation_data=(X_test, y_test))

# Testa uma previsão
entrada_exemplo = X[0]  # Já está codificado
entrada_exemplo = np.array([[entrada_exemplo]])
pred = modelo.predict(entrada_exemplo)
saida_prevista = encoder_y.inverse_transform([pred.argmax()])[0]

print(f"Saída prevista para 'abc': {saida_prevista}")
