import customtkinter as ctk, random, pyautogui as pag, time
from mouse import MouseCapture
import keyboard
import os


def emergencia():
    os._exit(0)

keyboard.add_hotkey('f11', emergencia) #caso queria trocar a tecla de emergencia é só substituir o F11 pela tecla desejada

fudido = 0
num_reports = 0
num_reports = int(num_reports)

def report(alvo):
    with open('report_players.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    escomungado = linhas[(alvo - 1)].strip()
    x,y = escomungado.split(',')
    x = int(x)
    y = int(y)

    with open('report_motivos.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    motivo = linhas[random.randint(1,3)].strip()
    q,w = motivo.split(',')
    q = int(q)
    w = int(w)    

    with open('report_motivos.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    motivo = linhas[4].strip()
    e,r = motivo.split(',')
    e = int(e)
    r = int(r)

    
    pag.moveTo(x,y, duration=0.05)
    pag.click(x,y)
    pag.moveTo(q,w, duration=0.05)
    pag.click(q,w)
    pag.moveTo(e,r, duration=0.05)
    pag.click(e,r)
    time.sleep(0.5)

def abrir_mouse():
    MouseCapture(janela)

def target():
    contador = 0
    fudido = int(selecao.get())
    while contador <= num_reports:
        report(fudido)
        contador +=1



janela = ctk.CTk()
janela.title('Adestrador de cadelas!')
janela.geometry('450x150')
janela.minsize(450,150)
janela.resizable(False, False)



tela1 = ctk.CTkFrame(janela)
tela1.pack(fill ='both', expand= True)




texto1 = ctk.CTkLabel(tela1, text='Selecione o alvo:')
texto1.grid(row=2, column=0, padx=5,pady=10)

selecao = ctk.CTkEntry(tela1)
selecao.grid(row=2, column=1)

texto2 = ctk.CTkLabel(tela1, text='Numero de reports:')
texto2.grid(row=3, column=0, padx=5,pady=10)

selecao2 = ctk.CTkEntry(tela1)
selecao2.grid(row=3, column=1)

btn_iniciar = ctk.CTkButton(tela1, text='Começar', command=target)
btn_iniciar.grid(row=4, column=0, padx=5,pady=10, columnspan=2)

btn_mouse = ctk.CTkButton(tela1, text='Configurar', command=abrir_mouse)
btn_mouse.grid(row=4, column=3, padx=5,pady=10, columnspan=2)


janela.mainloop()