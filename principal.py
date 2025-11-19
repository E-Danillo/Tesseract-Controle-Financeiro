import customtkinter as ctk
from datetime import datetime
from PIL import Image

# Cores
Azul = "#27AAE1"
Preto = "#282828"
Branco = "#DEDEE0"
Verde = "#257C0D"

# Janela Principal 
janela = ctk.CTk()
janela.title("Tesseract Finance")
janela.geometry("1400x900")
janela.resizable(False, False)
ctk.set_appearance_mode("dark")

# Grid da Janela Principal
janela.grid_rowconfigure(1, weight=1) 
janela.grid_columnconfigure(1, weight=1)

# ------------------------
# IFRAMES ( "DIVS" DO PYTHON )
# ------------------------
# FRAME DO TOPO
frame_topo = ctk.CTkFrame(janela, height=80, fg_color=Azul)
frame_topo.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Label do horário no topo
label_horario = ctk.CTkLabel(frame_topo, text="", font=("Arial", 14))
label_horario.place(relx=1.0, rely=0.5, anchor="e", x=-20)

# Ícone no topo
icon = Image.open("icon.jpeg")
icon_ctk = ctk.CTkImage(icon, size=(40, 40))
label_icon = ctk.CTkLabel(frame_topo, image=icon_ctk, text="")
label_icon.place(relx=0.0, rely=0.5, anchor="w", x=20)

# Título no topo
titulo = ctk.CTkLabel(frame_topo, text="Tesseract", font=("Arial", 30, "bold"))
titulo.pack(pady=20)

# FRAME DO MENU LATERAL
frame_menu = ctk.CTkFrame(janela, width=250, fg_color=Preto, border_color=Azul, border_width=3)
frame_menu.grid(row=1, column=0, sticky="nsew")

# FRAME DO CORPO DO APP
frame_app = ctk.CTkFrame(janela, fg_color=Preto, border_color=Azul, border_width=3)
frame_app.grid(row=1, column=1, sticky="nsew")

numero_salvo = ctk.StringVar()
label_contas = ctk.CTkLabel(frame_app, textvariable=numero_salvo)
label_contas.pack(padx=20, pady=20)

# FRAME DO RODAPÉ 
frame_log = ctk.CTkFrame(janela, height=80, fg_color=Azul)
frame_log.grid(row=2, column=0, columnspan=2, sticky="nsew")

# ------------------------
# FUNÇÕES
# ------------------------
def horario():
    agora = datetime.now().strftime("%Y-%m-%d / %H:%M:%S")
    label_horario.configure(text=agora)
    janela.after(1000, horario)

def adicionar_receita():
    entrada_receita.grid(row=1, column=0, padx=20, pady=10)

def salvar_numero_receitas():
    valor = entrada_receita.get()
    numero_salvo.set(valor)
    entrada_receita.delete(0, ctk.END)

def salvar_numero_despesas():
    valor = entrada_despesa.get()
    numero_salvo.set(valor)
    entrada_despesa.delete(0, ctk.END)

def adicionar_despesa():
    entrada_despesa.grid(row=4, column=0, padx=20, pady=10)

# ------------------------
# BOTOES DO MENU LATERAL
# ------------------------
botao_receita = ctk.CTkButton(frame_menu, 
    text="Receitas",
    command=adicionar_receita, 
    width=200, height=50, corner_radius=10, fg_color=Verde)
botao_receita.grid(row=0, column=0, padx=20, pady=20)

botao_salvar_receita = ctk.CTkButton(frame_menu, text="Salvar Receita", command=salvar_numero_receitas, width=100, height=25, corner_radius=10, fg_color=Verde)
botao_salvar_receita.grid(row=2, column=0, padx=20, pady=20)

botao_despesa = ctk.CTkButton(frame_menu, 
    text="Despesas",
    command=adicionar_despesa, 
    width=200, height=50, corner_radius=10, fg_color=Verde)
botao_despesa.grid(row=3, column=0, padx=20, pady=20)

botao_salvar_despesa = ctk.CTkButton(frame_menu, text="Salvar Despesa", command=salvar_numero_despesas, width=100, height=25, corner_radius=10, fg_color=Verde)
botao_salvar_despesa.grid(row=5, column=0, padx=20, pady=20)

# Entradas dos botões de receitas/despesas e demais relacionados
entrada_receita = ctk.CTkEntry(frame_menu, placeholder_text="Digite sua receita", width=200)
entrada_despesa = ctk.CTkEntry(frame_menu, placeholder_text="Digite sua despesa", width=200)

# Log no rodapé
log_label = ctk.CTkLabel(frame_log, text="Talvez o histórico apareça aqui...")
log_label.pack(pady=20)

horario() 
janela.mainloop()