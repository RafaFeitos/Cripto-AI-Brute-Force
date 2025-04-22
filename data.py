# data.py
from utils import carregar_dados, codificar_dados

def obter_dataset(caminho_csv):
    """
    Retorna X, y e os encoders a partir de um CSV.
    """
    X, y = carregar_dados(caminho_csv)
    X_enc, y_enc, enc_x, enc_y = codificar_dados(X, y)
    return X_enc, y_enc, enc_x, enc_y
