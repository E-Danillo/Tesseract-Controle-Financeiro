import tkinter as tk
from collections import deque


class LogFrame(tk.Frame):
    """
    Frame de mensagens rápidas (rodapé) para sistemas de controle financeiro.

    Recursos:
    ✔ Fila de mensagens (não perde alertas)
    ✔ Limpeza automática por tempo
    ✔ Estilos padronizados (erro, sucesso, aviso, info)
    ✔ Tema claro/escuro configurável
    ✔ API simples: log.sucesso("..."), log.erro("..."), log.info("..."), etc.
    """

    def init(self, master, theme="dark", auto_clear=True, clear_after=3000):
        bg_dark = "#1c1c1c"
        bg_light = "#f2f2f2"

        self.themes = {
            "dark":  {"bg": bg_dark, "fg": "white"},
            "light": {"bg": bg_light, "fg": "black"}, }

        super().init(master,
                     bg=self.themes.get(theme, self.themes["dark"])["bg"],
                     height=30
                     )

        self.pack_propagate(False)

        self.theme = theme
        self.auto_clear = auto_clear
        self.clear_after = clear_after

        self.clear_job = None
        self.queue = deque()
        self.is_displaying = False

        self.label = tk.Label(
            self,
            text="",
            anchor="w",
            padx=10,
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"],
            font=("Segoe UI", 10)
        )
        self.label.pack(fill="both", expand=True)

        # Cores padrão para mensagens
        self.colors = {
            "info":    "#5dade2",
            "sucesso": "#00ff88",
            "erro":    "#ff5555",
            "aviso":   "#f1c40f",
        }

    # ------------------------------------------------------
    # SISTEMA DE FILA (para não perder mensagens)
    # ------------------------------------------------------
    def _process_queue(self):
        if self.is_displaying or not self.queue:
            return

        msg, color = self.queue.popleft()
        self._display_message(msg, color)

    # ------------------------------------------------------
    # Mostra a mensagem na tela
    # ------------------------------------------------------
    def _display_message(self, msg, color):
        self.is_displaying = True
        self.label.config(text=msg, fg=color)

        if self.clear_job:
            self.after_cancel(self.clear_job)

        if self.auto_clear:
            self.clear_job = self.after(self.clear_after, self._finish_display)

    def _finish_display(self):
        self.label.config(text="")
        self.is_displaying = False
        self._process_queue()

    # ------------------------------------------------------
    # API PÚBLICA
    # ------------------------------------------------------
    def send(self, msg, color="white"):
        """Envia mensagem à fila."""
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
