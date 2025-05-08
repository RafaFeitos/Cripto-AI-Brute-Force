from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.feature_extraction.text import CountVectorizer
from data import DATASET_PATH
from utils import carregar_dados
import numpy as np
import joblib
import os

VECTORIZER_PATH = 'model/vectorizer.pkl'
MODEL_PATH = 'model/modelo.keras'

def treinar_modelo():
    X, y = carregar_dados(DATASET_PATH)

    vectorizer = CountVectorizer(analyzer='char', ngram_range=(1, 2))
    X_vect = vectorizer.fit_transform(X)

    # Salvar o vetorizer para usar no teste
    os.makedirs('model', exist_ok=True)
    joblib.dump(vectorizer, VECTORIZER_PATH)

    model = Sequential()
    model.add(Dense(128, activation='relu', input_shape=(X_vect.shape[1],)))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1))  # Saída numérica

    model.compile(optimizer=Adam(0.001), loss='mse')
    model.fit(X_vect.toarray(), y, epochs=10, batch_size=32, verbose=1)

    model.save(MODEL_PATH)
    print("[✓] Modelo treinado e salvo com sucesso!")

def testar_modelo(mensagem, chave, salt):
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        print("[!] Modelo ou vetorizador não encontrados. Treine o modelo primeiro.")
        return

    model = load_model(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    entrada = mensagem.upper() + chave.upper() + salt.upper()
    entrada_vect = vectorizer.transform([entrada])
    pred = model.predict(entrada_vect.toarray())
    resultado = int(round(pred[0][0]))

    print(f"[→] Resultado da criptografia prevista: {resultado}")