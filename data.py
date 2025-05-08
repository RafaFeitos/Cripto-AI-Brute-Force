import random
import pandas as pd
import os
import hashlib

DATASET_PATH = 'dataset/dados.csv'
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def gerar_string_aleatoria(tamanho=8):
    return ''.join(random.choices(ALFABETO, k=tamanho))

def criptografar(mensagem, chave, salt):
    """
    Gera hash criptografado (SHA-256) com salt individual.
    Retorna um número inteiro (primeiros 4 bytes do digest SHA-256).
    """
    combinado = mensagem + chave + salt
    hash_obj = hashlib.sha256(combinado.encode())
    hash_digest = hash_obj.digest()
    numero = int.from_bytes(hash_digest[:4], 'big')  # 32 bits
    return numero

def gerar_dataset(qtd_amostras=1000, caminho_saida=DATASET_PATH):
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

    mensagens = []
    chaves = []
    salts = []
    criptografadas = []

    for _ in range(qtd_amostras):
        mensagem = gerar_string_aleatoria(8)
        chave = gerar_string_aleatoria(6)
        salt = gerar_string_aleatoria(4)

        hash_numerico = criptografar(mensagem, chave, salt)

        mensagens.append(mensagem)
        chaves.append(chave)
        salts.append(salt)
        criptografadas.append(hash_numerico)

    df = pd.DataFrame({
        'mensagem': mensagens,
        'chave': chaves,
        'salt': salts,
        'mensagem_criptografada': criptografadas
    })

    df.to_csv(caminho_saida, index=False)
    print(f"[✓] Dataset salvo em {caminho_saida} com {qtd_amostras} entradas.")

if __name__ == '__main__':
    gerar_dataset()
