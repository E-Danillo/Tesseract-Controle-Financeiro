import customtkinter as ctk
from datetime import datetime
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque
import os # Importação adicionada para verificar a imagem

# --- 1. CONFIGURAÇÃO GLOBAL ---
# Cores
AZUL = "#27AAE1"
PRETO = "#282828"
BRANCO = "#DEDEE0"
VERDE = "#257C0D"

# ------------------------------------------------------------
# 2. CLASSE DO LOG (MANTIDA - JÁ ESTAVA BEM ESTRUTURADA)
# ------------------------------------------------------------
class CTkLogFrame(ctk.CTkFrame):
    """
    Rodapé de mensagens rápidas para sistemas em CustomTkinter.
    """

    def __init__(self, master, theme="dark", auto_clear=True, clear_after=3000):
        self._set_appearance(theme)
        super().__init__(master, height=32, fg_color=self.bg_color)

        self.pack_propagate(False)

        self.theme = theme
        self.auto_clear = auto_clear
        self.clear_after = clear_after

        self.clear_job = None
        self.queue = deque()
        self.is_displaying = False

        self.label = ctk.CTkLabel(
            self,
            text="",
            anchor="w",
            padx=10,
            text_color=self.text_color,
            font=ctk.CTkFont("Segoe UI", 13),
        )
        self.label.pack(fill="both", expand=True)

        # Cores para mensagens
        self.colors = {
            "info":     "#5dade2",
            "sucesso": "#00ff88",
            "erro":     "#ff5555",
            "aviso":   "#f1c40f",
        }

    # Tema claro/escuro
    def _set_appearance(self, theme):
        if theme == "light":
            self.bg_color = "#f2f2f2"
            self.text_color = "black"
        else:
            self.bg_color = "#1c1c1c"
            self.text_color = "white"

    # Sistema de fila
    def _process_queue(self):
        if self.is_displaying or not self.queue:
            return

        msg, color = self.queue.popleft()
        self._display_message(msg, color)

    def _display_message(self, msg, color):
        self.is_displaying = True
        self.label.configure(text=msg, text_color=color)

        if self.clear_job:
            self.after_cancel(self.clear_job)

        if self.auto_clear:
            self.clear_job = self.after(self.clear_after, self._finish_display)

    def _finish_display(self):
        self.label.configure(text="")
        self.label.configure(text_color=self.text_color)
        self.is_displaying = False
        self._process_queue()

    # API pública
    def send(self, msg, color="white"):
        self.queue.append((msg, color))
        self._process_queue()

    def info(self, msg):
        self.send(msg, self.colors["info"])

    def sucesso(self, msg):
        self.send(msg, self.colors["sucesso"])

    def erro(self, msg):
        self.send(msg, self.colors["erro"])

    def aviso(self, msg):
        self.send(msg, self.colors["aviso"])

# ------------------------------------------------------------
# 3. CLASSE PRINCIPAL DA APLICAÇÃO
# ------------------------------------------------------------
class AppTesseractFinanceiro(ctk.CTk):
    
    def __init__(self):
        # Inicializa a Janela (ctk.CTk)
        super().__init__()
        self.title("Tesseract Finance")
        self.geometry("1400x900")
        self.resizable(True, True)
        ctk.set_appearance_mode("dark")
        
        # Controle de Variáveis de Estado (Membros da Classe)
        self.lista_receitas = []
        self.lista_despesas = []
        self.numero_salvo = ctk.StringVar()
        
        # Chama os métodos para construir a UI
        self._configurar_grid()
        self._criar_iframes()
        self._criar_widgets_topo()
        self._criar_log()
        self._criar_widgets_app()
        self._criar_menu()
        
        # Inicia o loop de horário e status
        self._atualizar_horario()
        self._atualizar_status()


    def _configurar_grid(self):
        """ Configura o grid da janela principal. """
        self.grid_rowconfigure(1, weight=1) 
        self.grid_columnconfigure(1, weight=1)

    def _criar_iframes(self):
        """ Cria e posiciona os frames da interface (topo, menu, app, log). """
        self.frame_topo = ctk.CTkFrame(self, height=80, fg_color=AZUL)
        self.frame_topo.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.frame_menu = ctk.CTkFrame(self, width=250, fg_color=PRETO, border_color=AZUL, border_width=3)
        self.frame_menu.grid(row=1, column=0, sticky="nsew")

        self.frame_app = ctk.CTkFrame(self, fg_color=PRETO, border_color=AZUL, border_width=3)
        self.frame_app.grid(row=1, column=1, sticky="nsew")
        self.frame_app.grid_columnconfigure(0, weight=1) # Permite que widgets dentro de frame_app se expandam

        self.frame_log = ctk.CTkFrame(self, height=80, fg_color=AZUL)
        self.frame_log.grid(row=2, column=0, columnspan=2, sticky="nsew")

    def _criar_log(self):
        """ Cria a instância do CTkLogFrame e a empacota no frame_log. """
        self.log = CTkLogFrame(self.frame_log, theme="dark", auto_clear=True, clear_after=3000)
        self.log.pack(fill="both", expand=True, padx=10, pady=10)

    def _criar_widgets_topo(self):
        """ Cria e posiciona os widgets do frame superior (horário, ícone, título). """
        self.label_horario = ctk.CTkLabel(self.frame_topo, text="", font=("Arial", 14))
        self.label_horario.place(relx=1.0, rely=0.5, anchor="e", x=-20)

        # Trata a imagem de ícone (assumindo que "icon.jpeg" está disponível)
        try:
            icon_path = "icon.jpeg"
            if os.path.exists(icon_path):
                icon = Image.open(icon_path)
                icon_ctk = ctk.CTkImage(icon, size=(40, 40))
                self.label_icon = ctk.CTkLabel(self.frame_topo, image=icon_ctk, text="")
                self.label_icon.place(relx=0.0, rely=0.5, anchor="w", x=20)
            else:
                print(f"Aviso: Arquivo de imagem '{icon_path}' não encontrado.")
                
        except Exception as e:
            print(f"Erro ao carregar ícone: {e}")

        titulo = ctk.CTkLabel(self.frame_topo, text="Tesseract", font=("Arial", 40, "bold"))
        titulo.pack(pady=20)

    def _criar_widgets_app(self):
        """ Cria os widgets que serão exibidos dinamicamente no frame_app. """
        # Label de Exibição de Status
        self.label_contas = ctk.CTkLabel(self.frame_app, textvariable=self.numero_salvo, font=("Arial", 20))
        # O posicionamento inicial é feito no método de configuração (não pode ser no init)
        
        # Histórico
        self.historico = ctk.CTkTextbox(self.frame_app, width=400, height=320)
        self.historico.grid(row=0, column=1, padx=20, pady=20, sticky="nsew") # Posicionamento fixo

        # Posiciona o Label de Contas (Fixo)
        self.label_contas.grid(row=10, column=0, columnspan=2, padx=20, pady=40)

    def _criar_menu(self):
        """ Cria e posiciona os botões de navegação no frame_menu. """
        self.botao_receita = ctk.CTkButton(
            self.frame_menu, 
            text="Receitas",
            command=self._mostrar_adicionar_receita, 
            width=200, height=50, corner_radius=10, fg_color=VERDE
        )
        self.botao_receita.grid(row=0, column=0, padx=20, pady=20)

        self.botao_despesa = ctk.CTkButton(
            self.frame_menu, 
            text="Despesas",
            command=self._mostrar_adicionar_despesa, 
            width=200, height=50, corner_radius=10, fg_color=VERDE
        )
        self.botao_despesa.grid(row=1, column=0, padx=20, pady=20)

        self.botao_grafico = ctk.CTkButton(
            self.frame_menu, 
            text="Gráfico",
            command=self._mostrar_grafico, 
            width=200, height=50, corner_radius=10, fg_color=VERDE
        )
        self.botao_grafico.grid(row=2, column=0, padx=20, pady=20)

    # ------------------------
    # MÉTODOS DE LÓGICA / FUNÇÕES
    # ------------------------

    def _atualizar_horario(self):
        """ Atualiza o relógio no topo da janela. """
        agora = datetime.now().strftime(" %d/%m/%Y |  %H:%M:%S")
        self.label_horario.configure(text=agora, font=("Segoe UI Symbol", 14, "bold")) 
        self.after(1000, self._atualizar_horario)

    def _limpar_frame_app(self):
        """ Remove todos os widgets dinâmicos do frame_app. """
        # Remove todos os widgets, exceto os fixos (label_contas e historico)
        widgets_fixos = [self.label_contas, self.historico]
        
        for widget in self.frame_app.winfo_children():
            if widget not in widgets_fixos:
                # Se o widget tiver o método destroy (todos os widgets têm)
                # e não for um dos fixos, simplesmente destrua-o.
                widget.destroy()

    def _mostrar_adicionar_receita(self):
        """ Exibe os widgets para adicionar receita, recriando-os. """
        self._limpar_frame_app()
        self.log.info("Inserindo nova receita...")
        
        # 1. RECRIAR WIDGETS
        self.entrada_receita = ctk.CTkEntry(self.frame_app, placeholder_text="Digite sua receita", width=300)
        self.botao_salvar_receita = ctk.CTkButton(
            self.frame_app,
            text="Salvar Receita",
            command=self._salvar_numero_receitas,
            width=150,
            height=40,
            fg_color=VERDE
        )

        # 2. POSICIONAR NO GRID
        self.entrada_receita.grid(row=0, column=0, padx=20, pady=20)
        self.botao_salvar_receita.grid(row=1, column=0, padx=20, pady=20)

    def _mostrar_adicionar_despesa(self):
        """ Exibe os widgets para adicionar despesa, recriando-os. """
        self._limpar_frame_app()
        self.log.info("Inserindo nova despesa...")

        # 1. RECRIAR WIDGETS
        self.entrada_despesa = ctk.CTkEntry(self.frame_app, placeholder_text="Digite sua despesa", width=300)
        self.botao_salvar_despesa = ctk.CTkButton(
            self.frame_app,
            text="Salvar Despesa",
            command=self._salvar_numero_despesas,
            width=150,
            height=40,
            fg_color=VERDE
        )

        # 2. POSICIONAR NO GRID
        self.entrada_despesa.grid(row=0, column=0, padx=20, pady=20)
        self.botao_salvar_despesa.grid(row=1, column=0, padx=20, pady=20)

    def _salvar_numero_receitas(self):
        """ Processa e salva o valor da nova receita. """
        valor = self.entrada_receita.get()
        if valor.strip() != "":
            try:
                valor = float(valor)
                self.lista_receitas.append(valor)
                self.historico.insert("end", f"[RECEITA] R$ {valor:.2f}\n")
                self.historico.see("end")
                self.entrada_receita.delete(0, ctk.END)
                self._atualizar_status()
                self.log.sucesso(f"Receita adicionada: R$ {valor:.2f}")
            except ValueError:
                self.log.erro("Valor inválido para receita! Use apenas números.")
        else:
            self.log.aviso("Digite um valor para a receita!")

    def _salvar_numero_despesas(self):
        """ Processa e salva o valor da nova despesa. """
        valor = self.entrada_despesa.get()
        if valor.strip() != "":
            try:
                valor = float(valor)
                self.lista_despesas.append(valor)
                self.historico.insert("end", f"[DESPESA] R$ {valor:.2f}\n")
                self.historico.see("end")
                self.entrada_despesa.delete(0, ctk.END)
                self._atualizar_status()
                self.log.sucesso(f"Despesa adicionada: R$ {valor:.2f}")
            except ValueError:
                self.log.erro("Valor inválido para despesa! Use apenas números.")
        else:
            self.log.aviso("Digite um valor para a despesa!")

    def _atualizar_status(self):
        """ Calcula e exibe o saldo financeiro atual. """
        total_r = sum(self.lista_receitas)
        total_d = sum(self.lista_despesas)
        saldo = total_r - total_d
        
        if saldo > 0:
            status = f"Lucro de R$ {saldo:.2f}"
        elif saldo < 0:
            status = f"Prejuízo de R$ {abs(saldo):.2f}"
        else:
            status = "Equilíbrio financeiro"
        
        self.numero_salvo.set(
            f"Total Receitas: R$ {total_r:.2f} | Total Despesas: R$ {total_d:.2f}\n{status}"
        )

    def _mostrar_grafico(self):
        """ Cria e exibe o gráfico de barras no frame_app. """
        self._limpar_frame_app()
        self.log.info("Gerando gráfico...")

        total_r = sum(self.lista_receitas)
        total_d = sum(self.lista_despesas)
        
        if total_r == 0 and total_d == 0:
            self.log.aviso("Não há dados de Receitas ou Despesas para gerar o gráfico.")
            return

        # Cria a figura do Matplotlib
        fig, ax = plt.subplots(figsize=(5, 4))
        categorias = ["Receitas", "Despesas"]
        valores = [total_r, total_d]

        # Ajuste: Se houver dados, plota.
        ax.bar(categorias, valores, color=[VERDE, 'red']) 
        ax.set_title("Gráfico Financeiro", color='white')
        ax.set_ylabel("Valores (R$)", color='white')
        
        # Configurações de tema para Matplotlib no modo escuro
        ax.set_facecolor(PRETO)
        fig.patch.set_facecolor(PRETO)
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        fig.tight_layout()

        # Integra o gráfico com o CustomTkinter
        # O canvas precisa ser colocado em um FRAME para gerenciamento no CTk
        plot_frame = ctk.CTkFrame(self.frame_app, fg_color=PRETO)
        plot_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Cria o canvas e empacota DENTRO do plot_frame
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        self.log.sucesso("Gráfico exibido com sucesso!")


# ------------------------
# 4. EXECUÇÃO DA APLICAÇÃO
# ------------------------
if __name__ == "__main__":
    app = AppTesseractFinanceiro()
    app.mainloop()