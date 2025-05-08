# utils.py
import pandas as pd
import numpy as np
from data import DATASET_PATH

def carregar_dados(caminho_csv):
    df = pd.read_csv(caminho_csv)

    # Verifica se as colunas esperadas estão presentes
    colunas_esperadas = {'mensagem', 'chave', 'salt', 'mensagem_criptografada'}
    if not colunas_esperadas.issubset(df.columns):
        raise ValueError(f"CSV deve conter as colunas {colunas_esperadas}")

    # Concatena mensagem, chave e salt como string de entrada para o modelo
    X = df['mensagem'] + df['chave'] + df['salt']
    y = df['mensagem_criptografada']

    return X, y

def codificar_palavra(palavra):
    """
    Codifica uma palavra de 8 letras em vetor de inteiros normalizados.
    Cada letra é convertida para (ord(char) - 65) / 25 → entre 0 e 1 (A-Z)
    """
    return np.array([(ord(c) - 65) / 25 for c in palavra])  # A=0.0, Z=1.0