#import tkinter
#
#janela = tkinter.Tk()
#janela.geometry("500x300")
#
#def clique():
#    print("Fazer login")

#texto = tkinter.Label(janela, text="Fazer login")
#texto.pack(padx=10, pady=10)

#botao = tkinter.Button(janela,text="Login", command=clique)
#botao.pack(padx=10,pady=10)

#janela.mainloop()

import time
import customtkinter

def abrir_janela():
    janela2 = customtkinter.CTk()
    janela2.geometry("500x300")
    janela2.title('Janela nova')

    # Criação do texto de login
    texto = customtkinter.CTkLabel(janela2, text="Fazer login")
    texto.pack(padx=10, pady=10)

    # Criação do campo para colocar o email
    email = customtkinter.CTkEntry(janela2, placeholder_text="Seu e-mail")
    email.pack(padx=10, pady=10)

    # Criação do campo para colocar a senha
    senha = customtkinter.CTkEntry(janela2, placeholder_text="Sua senha", show="*")
    senha.pack(padx=10, pady=10)

    # Criação da caixa de lembrar login
    checkbox = customtkinter.CTkCheckBox(janela2, text="Lembrar Login")
    checkbox.pack(padx=10, pady=10)

    # Criação do botão login
    botao = customtkinter.CTkButton(janela2, text="Login", command=clique)
    botao.pack(padx=10, pady=10)

    janela2.mainloop()


def clique():
    print("Fazer login")


def realizar_cadastro():
    # Simulando o processo de cadastro
    for i in range(5):
        time.sleep(1)  # Simula uma operação demorada
        progressbar['value'] += 20  # Atualiza o valor da barra de progresso
        janela.update_idletasks()  # Atualiza a janela


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Criando janela
janela = customtkinter.CTk()
janela.geometry("500x500")

# Criação do texto de cadastro
texto = customtkinter.CTkLabel(janela, text="Fazer cadastro")
texto.pack(padx=10, pady=10)

# Criação do campo para nome completo
nome = customtkinter.CTkEntry(janela, placeholder_text="Seu nome completo")
nome.pack(padx=10, pady=10)

# Criação do campo para colocar o email
email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

# Criação do campo para colocar a senha
senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

# Criação do campo para a confirmação da senha
confirmar_senha = customtkinter.CTkEntry(janela, placeholder_text="Confirme sua senha", show="*")
confirmar_senha.pack(padx=10, pady=10)

# Criação do campo para o telefone
telefone = customtkinter.CTkEntry(janela, placeholder_text="Digite seu telefone")
telefone.pack(padx=10, pady=10)

# Criação do botão de cadastro
botao_cadastrar = customtkinter.CTkButton(janela, text="Cadastrar", command=abrir_janela)
botao_cadastrar.pack(padx=10, pady=10)

# Criação da barra de progressão
progressbar = customtkinter.CTkProgressBar(janela, width=400, height=10, corner_radius=30, fg_color="#002")
progress_color = "#090"
progressbar.pack(pady=10)
progressbar.start()

janela.mainloop()
