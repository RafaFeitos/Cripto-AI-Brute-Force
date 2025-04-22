# model.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

def criar_modelo(input_dim, output_dim):
    """
    Cria e compila um modelo simples de rede neural densa.
    """
    modelo = Sequential([
        Dense(64, activation='relu', input_dim=input_dim),
        Dense(64, activation='relu'),
        Dense(output_dim, activation='softmax')  # saída categórica
    ])

    modelo.compile(optimizer=Adam(learning_rate=0.001),
                   loss='sparse_categorical_crossentropy',
                   metrics=['accuracy'])

    return modelo