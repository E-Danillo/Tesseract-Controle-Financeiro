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
label_texto = ctk.CTkLabel(frame_app, text="Talvez um gráfico e estatísticas apareçam aqui...")
label_texto.pack(padx=20, pady=20)
frame_app.grid(row=1, column=1, sticky="nsew")

# FRAME DO RODAPÉ 
frame_log = ctk.CTkFrame(janela, height=80, fg_color=Azul)
frame_log.grid(row=2, column=0, columnspan=2, sticky="nsew")

# ------------------------
# FUNÇÕES
# ------------------------
def adicionarReceita():
    entrada_receitas.grid(row=1, column=0, padx=20, pady=10)

def adicionarDespesa():
    entrada_despesas.grid(row=3, column=0, padx=20, pady=10)

def horario():
    agora = datetime.now().strftime("%Y-%m-%d / %H:%M:%S")
    label_horario.configure(text=agora)
    janela.after(1000, horario)

# ------------------------
# BOTOES DO MENU LATERAL
# ------------------------
botao_de_receitas = ctk.CTkButton(frame_menu, 
    text="Receitas",
    command=adicionarReceita, 
    width=200, height=50, corner_radius=10, fg_color=Verde)
botao_de_receitas.grid(row=0, column=0, padx=20, pady=20)

botao_de_despesas = ctk.CTkButton(frame_menu, 
    text="Despesas",
    command=adicionarDespesa, 
    width=200, height=50, corner_radius=10, fg_color=Verde)
botao_de_despesas.grid(row=2, column=0, padx=20, pady=20)

# Entradas dos botões de receitas e despesas
entrada_receitas = ctk.CTkEntry(frame_menu, placeholder_text="Digite sua receita", width=200)
entrada_despesas = ctk.CTkEntry(frame_menu, placeholder_text="Digite sua despesa", width=200)

# Log no rodapé
log_label = ctk.CTkLabel(frame_log, text="Talvez o histórico apareça aqui...")
log_label.pack(pady=20)

horario() 
janela.mainloop()