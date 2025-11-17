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

# Grid da Janela Principal
janela.grid_rowconfigure(1, weight=1) 
janela.grid_columnconfigure(1, weight=1)

# --- FRAMES ---
# Frame do Topo
frame_topo = ctk.CTkFrame(janela, height=80, fg_color=Azul)
frame_topo.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Frame do Menu lateral
frame_menu = ctk.CTkFrame(janela, width=250, fg_color=Preto, border_color=Azul, border_width=3)
frame_menu.grid(row=1, column=0, sticky="nsew")

# Frame do Corpo do app
frame_app = ctk.CTkFrame(janela, fg_color=Preto, border_color=Azul, border_width=3)
label_texto = ctk.CTkLabel(frame_app, text="Talvez um gráfico e estatísticas apareçam aqui...")
label_texto.pack(padx=20, pady=20)
frame_app.grid(row=1, column=1, sticky="nsew")

# Frame do Rodapé 
frame_log = ctk.CTkFrame(janela, height=80, fg_color=Azul)
frame_log.grid(row=2, column=0, columnspan=2, sticky="nsew")

# Entradas 
entradaReceita = ctk.CTkEntry(frame_menu, placeholder_text="Digite sua receita", width=200)
entradaDespesa = ctk.CTkEntry(frame_menu, placeholder_text="Digite sua despesa", width=200)

# Funções
def adicionarReceita():
    entradaReceita.grid(row=1, column=0, padx=20, pady=10)

def adicionarDespesa():
    entradaDespesa.grid(row=1, column=1, padx=20, pady=10)

# Botões de adicionar receita e despesa
botaoDeReceita = ctk.CTkButton(frame_menu, 
    text="Digite sua receita",
    command=adicionarReceita, 
    width=200, height=50, corner_radius=10, fg_color=Verde)
botaoDeReceita.grid(row=0, column=0, padx=20, pady=20)

botaoDeDespesa = ctk.CTkButton(frame_menu, 
    text="Digite sua despesa",
    command=adicionarDespesa, 
    width=200, height=50, corner_radius=10, fg_color=Verde)
botaoDeDespesa.grid(row=0, column=1, padx=20, pady=20)

# Título no topo
titulo = ctk.CTkLabel(frame_topo, text="Tesseract", font=("Arial", 30, "bold"))
titulo.pack(pady=20)

# Log no rodapé
log_label = ctk.CTkLabel(frame_log, text="Talvez o histórico apareça aqui...")
log_label.pack(pady=20)

janela.mainloop()