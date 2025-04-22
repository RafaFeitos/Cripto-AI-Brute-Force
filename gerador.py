from utils import gerar_chave_16bits, criptografar_mensagem, salvar_dataset

mensagem = "HELLO WORLD"
chave = gerar_chave_16bits()
criptografada = criptografar_mensagem(mensagem, chave)

print("Chave:", chave)
print("Mensagem criptografada:", criptografada)

salvar_dataset(mensagem, chave, criptografada)