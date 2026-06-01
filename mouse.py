import customtkinter as ctk
import pyautogui
import time
import threading

ctk.set_appearance_mode("dark")

class MouseCapture(ctk.CTkToplevel):

    def __init__(self, master):

        super().__init__(master)

        self.title("FireCoords")
        self.geometry("450x450")
        self.resizable(False, False)

        titulo = ctk.CTkLabel(
            self,
            text="Captura de Coordenadas",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=10)

        self.status = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 14)
        )
        self.status.pack()

        # CAIXA DE TEXTO
        self.textbox = ctk.CTkTextbox(
            self,
            width=380,
            height=200,
            font=("Consolas", 16)
        )
        self.textbox.pack(pady=10)

        # BOTÃO CAPTURA
        self.botao = ctk.CTkButton(
            self,
            text="Capturar Coordenada",
            command=self.iniciar_captura
        )
        self.botao.pack(pady=10)

        # BOTÃO SALVAR PLAYERS
        self.botao_salvar_players = ctk.CTkButton(
            self,
            text="Salvar Players",
            command=self.salvar_txt_players
        )
        self.botao_salvar_players.pack(pady=5)

    # BOTÃO SALVAR REPORTS
        self.botao_salvar_reports = ctk.CTkButton(
                self,
                text="Salvar Motivos",
                command=self.salvar_txt_motivos
            )
        self.botao_salvar_reports.pack(pady=5)

    def iniciar_captura(self):

        thread = threading.Thread(target=self.capturar)
        thread.daemon = True
        thread.start()

    def capturar(self):

        self.botao.configure(state="disabled")

        # CONTAGEM
        for i in range(3, 0, -1):

            self.status.configure(
                text=f"Capturando em {i}..."
            )

            time.sleep(1)

        # PEGA POSIÇÃO
        x, y = pyautogui.position()

        coordenada = f"{x},{y}\n"

        # ESCREVE NA CAIXA
        self.textbox.insert("end", coordenada)

        # AUTO SCROLL
        self.textbox.see("end")

        # COPIA
        self.clipboard_clear()
        self.clipboard_append(f"{x}, {y}")

        self.status.configure(
            text="Coordenada capturada!"
        )

        self.botao.configure(state="normal")

    def salvar_txt_players(self): #PLAYERS

        conteudo = self.textbox.get("1.0", "end").strip()

        if not conteudo:

            self.status.configure(
                text="Nenhuma coordenada para salvar!"
            )

            return

        with open("report_players.txt", "w", encoding="utf-8") as arquivo_txt:

            arquivo_txt.write(conteudo)

        self.status.configure(
            text="Arquivo salvo: report_players.txt"
        )
    def salvar_txt_motivos(self): #REPORTS

        conteudo = self.textbox.get("1.0", "end").strip()

        if not conteudo:

            self.status.configure(
                text="Nenhuma coordenada para salvar!"
            )

            return

        with open("report_motivos.txt", "w", encoding="utf-8") as arquivo_txt:

            arquivo_txt.write(conteudo)

        self.status.configure(
            text="Arquivo salvo: report_motivos.txt"
        )