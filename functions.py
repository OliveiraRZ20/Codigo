from tkinter import *
from tkinter import ttk

def centralizar_janela(janela, largura: int, altura: int) -> None:
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    soma_x = ((tela_largura - largura) // 2) - 8
    soma_y = ((tela_altura - altura) // 2) - 40
    janela.geometry(f"{largura}x{altura}+{soma_x}+{soma_y}")
    # print("centralizar_janela = OK")

def criar_coluna_ttk(dominio, nome: str, minwidth: int, width: int, titulo: str) -> None:
    dominio.column(nome,minwidth=minwidth,width=width)
    dominio.heading(nome,text=titulo)