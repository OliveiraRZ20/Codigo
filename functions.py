from customtkinter import *

def centralizar_janela(janela, largura: int, altura: int) -> None:
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    soma_x = ((tela_largura - largura) // 2) - 8
    soma_y = ((tela_altura - altura) // 2) - 40
    janela.geometry(f"{largura}x{altura}+{soma_x}+{soma_y}")

def criar_coluna_ttk(dominio, nome: str, minwidth: int, width: int, titulo: str) -> None:
    dominio.column(nome,minwidth=minwidth,width=width)
    dominio.heading(nome,text=titulo)

def criar_botao_ttk(dominio, width: int, text: str, tamanho_fonte: int, command ,e_negrito: bool = True) -> None:
    if e_negrito:
        butt = CTkButton(dominio, width=width, text=text, font=("arial",tamanho_fonte,"bold"), command=command)
    else:
        butt = CTkButton(dominio,width=width, text=text, font=("arial",tamanho_fonte), command=command)
    return butt

main_x = 750
main_y = 450

class Gerenciador():
    def __init__(self) -> None:
        self.tem_janela_aberta: bool = False

    def inserir_tarefa(self) -> None:
        if self.tem_janela_aberta:
            pass
        else:
            self.tem_janela_aberta = True
            win_insere = CTkToplevel()
            win_insere.title("Inserir nova tarefa")
            centralizar_janela(win_insere,main_x,main_y)
            win_insere.geometry("400x200")
            # comando para dar foco na janela Devido a bug do CTk
            win_insere.after(100, win_insere.lift)
            win_insere.protocol("WM_DELETE_WINDOW",lambda: self.gatilhar_fechamento(win_insere))

    def atualizar_tarefa(self) -> None:
        if self.tem_janela_aberta:
            pass
        else:
            self.tem_janela_aberta = True
            win_atualiza = CTkToplevel()
            win_atualiza.title("Atualizar Tarefa")
            centralizar_janela(win_atualiza,main_x,main_y)
            win_atualiza.geometry("600x300")
            # comando para dar foco na janela Devido a bug do CTk
            win_atualiza.after(100, win_atualiza.lift)
            win_atualiza.protocol("WM_DELETE_WINDOW",lambda: self.gatilhar_fechamento(win_atualiza))

    def exibir_tarefa(self) -> None:
        if self.tem_janela_aberta:
            pass
        else:
            self.tem_janela_aberta = True
            win_exibe = CTkToplevel()
            win_exibe.title("Exibir Tarefa")
            centralizar_janela(win_exibe,main_x,main_y)
            win_exibe.geometry("500x450")
            # comando para dar foco na janela Devido a bug do CTk
            win_exibe.after(100, win_exibe.lift)
            win_exibe.protocol("WM_DELETE_WINDOW",lambda: self.gatilhar_fechamento(win_exibe))

    def deletar_tarefa(self) -> None:
        if self.tem_janela_aberta:
            pass
        else:
            self.tem_janela_aberta = True
            win_deleta = CTkToplevel()
            win_deleta.title("Deletar Tarefa")
            centralizar_janela(win_deleta,main_x,main_y)
            win_deleta.geometry("400x200")
            # comando para dar foco na janela Devido a bug do CTk
            win_deleta.after(100, win_deleta.lift)
            win_deleta.protocol("WM_DELETE_WINDOW",lambda: self.gatilhar_fechamento(win_deleta))
    
    def gatilhar_fechamento(self, dominio):
        self.tem_janela_aberta = False
        dominio.destroy()
        

gerenciador = Gerenciador()