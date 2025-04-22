# utils.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def carregar_dados(caminho_csv):
    """
    Carrega os dados do arquivo CSV e retorna X, y.
    """
    df = pd.read_csv(caminho_csv)

    # Verifica se há colunas 'entrada' e 'saida'
    if 'entrada' not in df.columns or 'saida' not in df.columns:
        raise ValueError("CSV deve conter colunas 'entrada' e 'saida'")

    X = df['entrada'].values
    y = df['saida'].values
    return X, y

def codificar_dados(X, y):
    """
    Codifica strings em números com LabelEncoder para uso na rede neural.
    """
    encoder_x = LabelEncoder()
    encoder_y = LabelEncoder()

    X_encoded = encoder_x.fit_transform(X)
    y_encoded = encoder_y.fit_transform(y)

    return X_encoded, y_encoded, encoder_x, encoder_y
