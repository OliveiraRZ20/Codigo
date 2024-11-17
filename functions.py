from tkinter import Button, Label, StringVar, ttk


def centralizar_janela(janela, largura: int, altura: int) -> None:
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    soma_x = ((tela_largura - largura) // 2) - 8
    soma_y = ((tela_altura - altura) // 2) - 40
    janela.geometry(f"{largura}x{altura}+{soma_x}+{soma_y}")
    # print("centralizar_janela = OK")