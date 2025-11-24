import customtkinter as ctk
from datetime import datetime
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Cores
Azul = "#27AAE1"
Preto = "#282828"
Branco = "#DEDEE0"
Verde = "#257C0D"

#Controle de Variáveis
lista_receitas = []
lista_despesas = []

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
# IFRAMES
# ------------------------
frame_topo = ctk.CTkFrame(janela, height=80, fg_color=Azul)
frame_topo.grid(row=0, column=0, columnspan=2, sticky="nsew")

frame_menu = ctk.CTkFrame(janela, width=250, fg_color=Preto, border_color=Azul, border_width=3)
frame_menu.grid(row=1, column=0, sticky="nsew")

frame_app = ctk.CTkFrame(janela, fg_color=Preto, border_color=Azul, border_width=3)
frame_app.grid(row=1, column=1, sticky="nsew")

frame_log = ctk.CTkFrame(janela, height=80, fg_color=Azul)
frame_log.grid(row=2, column=0, columnspan=2, sticky="nsew")

# ------------------------
# ELEMENTOS DO TOPO
# ------------------------
label_horario = ctk.CTkLabel(frame_topo, text="", font=("Arial", 14))
label_horario.place(relx=1.0, rely=0.5, anchor="e", x=-20)

icon = Image.open("icon.jpeg")
icon_ctk = ctk.CTkImage(icon, size=(40, 40))
label_icon = ctk.CTkLabel(frame_topo, image=icon_ctk, text="")
label_icon.place(relx=0.0, rely=0.5, anchor="w", x=20)

titulo = ctk.CTkLabel(frame_topo, text="Tesseract", font=("Arial", 40, "bold"))
titulo.pack(pady=20)

# ------------------------
# LABEL DE EXIBIÇÃO
# ------------------------
numero_salvo = ctk.StringVar()
label_contas = ctk.CTkLabel(frame_app, textvariable=numero_salvo, font=("Arial", 20))
label_contas.grid(row=10, column=0, padx=20, pady=40)

# ------------------------
# FUNÇÕES
# ------------------------
def horario():
    agora = datetime.now().strftime("• %d/%m/%Y | %H:%M:%S •")
    label_horario.configure(text=agora, font=("Segoe UI Symbol", 14, "bold")) 
    janela.after(1000, horario)

def adicionar_receita():
    limpar_frame_app()
    entrada_receita.grid(row=0, column=0, padx=20, pady=20)
    botao_salvar_receita.grid(row=1, column=0, padx=20, pady=20)

def adicionar_despesa():
    limpar_frame_app()
    entrada_despesa.grid(row=0, column=0, padx=20, pady=20)
    botao_salvar_despesa.grid(row=1, column=0, padx=20, pady=20)

def salvar_numero_receitas():
    valor = entrada_receita.get()
    if valor.strip() != "":
        valor = float(valor)
        lista_receitas.append(valor)
        historico.insert("end", f"[RECEITA] R$ {valor:.2f}\n")
        historico.see("end")
        entrada_receita.delete(0, ctk.END)
        atualizar_status()

def salvar_numero_despesas():
    valor = entrada_despesa.get()
    if valor.strip() != "":
        valor = float(valor)
        lista_despesas.append(valor)
        historico.insert("end", f"[DESPESA] R$ {valor:.2f}\n")
        historico.see("end")
        entrada_despesa.delete(0, ctk.END)
        atualizar_status()

def limpar_frame_app():
    for widget in frame_app.grid_slaves():
        if widget not in [label_contas, historico]:
            widget.grid_forget()

def atualizar_status():
    total_r = sum(lista_receitas)
    total_d = sum(lista_despesas)
    saldo = total_r - total_d
    
    if saldo > 0:
        status = f"Lucro de R$ {saldo:.2f}"
    elif saldo < 0:
        status = f"Prejuízo de R$ {abs(saldo):.2f}"
    else:
        status = "Equilíbrio financeiro"
    
    numero_salvo.set(
        f"Total Receitas: R$ {total_r:.2f} | Total Despesas: R$ {total_d:.2f}\n{status}"
    )

def mostrar_grafico():
    limpar_frame_app()
    for widget in frame_app.grid_slaves():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()

    fig, ax = plt.subplots(figsize=(5, 4))
    categorias = ["Receitas", "Despesas"]
    valores = [sum(lista_receitas), sum(lista_despesas)]

    ax.bar(categorias, valores)
    ax.set_title("Gráfico Financeiro")
    ax.set_ylabel("Valores (R$)")

    canvas = FigureCanvasTkAgg(fig, master=frame_app)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=20, pady=20)

# ------------------------
# ELEMENTOS DO FRAME APP
# ------------------------
# Entrada de Receita e Despesa no Frame App
entrada_receita = ctk.CTkEntry(frame_app, placeholder_text="Digite sua receita", width=300)
entrada_despesa = ctk.CTkEntry(frame_app, placeholder_text="Digite sua despesa", width=300)

# Botões de Salvar 
botao_salvar_receita = ctk.CTkButton(
    frame_app,
    text="Salvar Receita",
    command=lambda: salvar_numero_receitas(),
    width=150,
    height=40,
    fg_color=Verde
)

botao_salvar_despesa = ctk.CTkButton(
    frame_app,
    text="Salvar Despesa",
    command=lambda: salvar_numero_despesas(),
    width=150,
    height=40,
    fg_color=Verde
)

# Caixa de histórico
historico = ctk.CTkTextbox(frame_app, width=400, height=320)
historico.grid(row=0, column=1, padx=20, pady=20)

# ------------------------
# MENU LATERAL
# ------------------------
# Botão de Receita
botao_receita = ctk.CTkButton(
    frame_menu, 
    text="Receitas",
    command=adicionar_receita, 
    width=200, height=50, corner_radius=10, fg_color=Verde
)
botao_receita.grid(row=0, column=0, padx=20, pady=20)

# Botão de Despesa
botao_despesa = ctk.CTkButton(
    frame_menu, 
    text="Despesas",
    command=adicionar_despesa, 
    width=200, height=50, corner_radius=10, fg_color=Verde
)
botao_despesa.grid(row=1, column=0, padx=20, pady=20)

# Botão de Gráfico
botao_grafico = ctk.CTkButton(
    frame_menu, 
    text="Gráfico",
    command=mostrar_grafico, 
    width=200, height=50, corner_radius=10, fg_color=Verde
)
botao_grafico.grid(row=2, column=0, padx=20, pady=20)

# ------------------------
# LOG
# ------------------------
log_label = ctk.CTkLabel(frame_log, text="Talvez as ações do usuário apareçam aqui...")
log_label.pack(pady=20)

# ------------------------
# LOOP
# ------------------------
horario()
janela.mainloop()