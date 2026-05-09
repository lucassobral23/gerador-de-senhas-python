import random
import string

print("=== GERADOR DE SENHAS ===")

try:
    tamanho = int(input("Digite o tamanho da senha: "))

    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = ""

    for i in range(tamanho):
        senha += random.choice(caracteres)

    print("\nSenha gerada:")
    print(senha)

except:
    print("Digite apenas números!")
