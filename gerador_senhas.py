import random
import string

def gerar_senha(tamanho, usar_numeros, usar_simbolos):

    caracteres = string.ascii_letters

    if usar_numeros:
        caracteres += string.digits

    if usar_simbolos:
        caracteres += string.punctuation

    senha = ""

    for i in range(tamanho):
        senha += random.choice(caracteres)

    return senha


print("=== GERADOR DE SENHAS ===")

tamanho = int(input("Digite o tamanho da senha: "))

numeros = input("Deseja usar números? (s/n): ").lower() == "s"

simbolos = input("Deseja usar símbolos? (s/n): ").lower() == "s"

senha_gerada = gerar_senha(tamanho, numeros, simbolos)

print("\nSenha gerada:")
print(senha_gerada)