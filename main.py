from data import gerar_dataset
from model import treinar_modelo, testar_modelo

def menu():
    while True:
        print("\n=== CriptoIA - Menu Principal ===")
        print("1. Gerar dataset e treinar IA")
        print("2. Testar uma entrada manual")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            qtd = input("Quantas amostras deseja gerar para o dataset? (padrão: 1000): ")
            qtd = int(qtd) if qtd.isdigit() else 1000
            gerar_dataset(qtd)
            treinar_modelo()

        elif opcao == '2':
            mensagem = input("Digite a MENSAGEM (8 letras MAIÚSCULAS): ").strip().upper()
            chave = input("Digite a CHAVE (4 letras MAIÚSCULAS): ").strip().upper()
            salt = input("Digite o SALT (4 letras MAIÚSCULAS): ").strip().upper()

            if not (len(mensagem) == 8 and mensagem.isalpha()):
                print("Mensagem inválida. Deve ter exatamente 8 letras MAIÚSCULAS.")
                continue
            if not (len(chave) == 4 and chave.isalpha()):
                print("Chave inválida. Deve ter exatamente 4 letras MAIÚSCULAS.")
                continue
            if not (len(salt) == 4 and salt.isalpha()):
                print("Salt inválido. Deve ter exatamente 4 letras MAIÚSCULAS.")
                continue

            testar_modelo(mensagem, chave, salt)

        elif opcao == '3':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()