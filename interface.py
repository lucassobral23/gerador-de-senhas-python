import tkinter as tk
import random
import string


def verificar_forca(senha):

    pontos = 0

    if len(senha) >= 8:
        pontos += 1

    if any(caractere.isdigit() for caractere in senha):
        pontos += 1

    if any(caractere in string.punctuation for caractere in senha):
        pontos += 1

    if pontos == 1:
        return "Senha Fraca", "red"

    elif pontos == 2:
        return "Senha Média", "orange"

    else:
        return "Senha Forte", "green"



def gerar_senha():

    tamanho = int(entrada_tamanho.get())

    caracteres = string.ascii_letters

    if usar_numeros.get():
        caracteres += string.digits

    if usar_simbolos.get():
        caracteres += string.punctuation

    senha = ""

    for i in range(tamanho):
        senha += random.choice(caracteres)

    resultado.config(text=senha)

    texto_forca, cor = verificar_forca(senha)

    forca_label.config(text=texto_forca, fg=cor)



def copiar_senha():

    senha = resultado.cget("text")

    janela.clipboard_clear()

    janela.clipboard_append(senha)


janela = tk.Tk()

janela.title("Gerador de Senhas")

janela.geometry("500x450")

janela.config(bg="#1e1e1e")


titulo = tk.Label(
    janela,
    text="Gerador de Senhas",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)
titulo.pack(pady=20)


texto_tamanho = tk.Label(
    janela,
    text="Tamanho da senha:",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)
texto_tamanho.pack()


entrada_tamanho = tk.Entry(
    janela,
    font=("Arial", 14),
    justify="center"
)
entrada_tamanho.pack(pady=10)


usar_numeros = tk.BooleanVar()

check_numeros = tk.Checkbutton(
    janela,
    text="Usar números",
    variable=usar_numeros,
    bg="#1e1e1e",
    fg="white",
    selectcolor="#1e1e1e",
    font=("Arial", 11)
)
check_numeros.pack()


usar_simbolos = tk.BooleanVar()

check_simbolos = tk.Checkbutton(
    janela,
    text="Usar símbolos",
    variable=usar_simbolos,
    bg="#1e1e1e",
    fg="white",
    selectcolor="#1e1e1e",
    font=("Arial", 11)
)
check_simbolos.pack()


botao = tk.Button(
    janela,
    text="Gerar Senha",
    command=gerar_senha,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5
)
botao.pack(pady=20)


botao_copiar = tk.Button(
    janela,
    text="Copiar Senha",
    command=copiar_senha,
    font=("Arial", 11, "bold"),
    bg="#2196F3",
    fg="white",
    padx=10,
    pady=5
)
botao_copiar.pack()


resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="#00ff88",
    wraplength=400
)
resultado.pack(pady=20)


forca_label = tk.Label(
    janela,
    text="",
    font=("Arial", 12, "bold"),
    bg="#1e1e1e"
)
forca_label.pack()

creditos = tk.Label(
    janela,
    text="Lucas Gabriel",
    font=("Arial", 9),
    bg="#1e1e1e",
    fg="gray"
)

creditos.place(
    relx=1.0,
    rely=1.0,
    anchor="se",
    x=-10,
    y=-10
)
janela.mainloop()