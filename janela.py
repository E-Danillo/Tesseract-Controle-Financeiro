import customtkinter as ctk

# Cores
Azul = "#27AAE1"
Preto = "#282828"
Branco = "#EDEDEF"
Verde = "#5BAD45"

# Janela Principal
janela = ctk.CTk()
janela.title("Tesseract")
janela.geometry("1400x900")
janela.resizable(False, False)
ctk.set_appearance_mode("dark")

# Entradas
entradaReceita = ctk.CTkEntry(janela, placeholder_text="Digite sua receita")
entradaDespesa = ctk.CTkEntry(janela, placeholder_text="Digite sua despesa")

# Funções
def adicionarReceita():
    entradaReceita.grid(row=1, column=0, padx=20, pady=10)

def adicionarDespesa():
    entradaDespesa.grid(row=1, column=1, padx=20, pady=10)

# Botões
botaoDeReceita = ctk.CTkButton(janela, text="Digite sua receita", command=adicionarReceita, width=200, height=50, corner_radius=10)
botaoDeDespesa = ctk.CTkButton(janela, text="Digite sua despesa", command=adicionarDespesa, width=200, height=50, corner_radius=10)

# Posicionando botões
botaoDeReceita.grid(row=0, column=0, padx=50, pady=20)
botaoDeDespesa.grid(row=0, column=1, padx=50, pady=20)

janela.mainloop()