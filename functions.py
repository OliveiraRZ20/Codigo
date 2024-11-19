from tkinter import *
from customtkinter import *

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

def criar_botao_ttk(dominio, width: int, text: str, tamanho_fonte: int, command ,e_negrito: bool = True) -> None:
    if e_negrito:
        butt = CTkButton(dominio, width=width, text=text, font=("arial",tamanho_fonte,"bold"), command=command)
    else:
        butt = CTkButton(dominio,width=width, text=text, font=("arial",tamanho_fonte), command=command)
    return butt

def inserir_tarefa() -> None:
    win_inserir = CTkToplevel()
    win_inserir.title("Inserir nova tarefa")
    win_inserir.geometry("200x200")