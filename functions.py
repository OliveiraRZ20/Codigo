from customtkinter import *
import tkinter.messagebox as msgbox
from datetime import datetime

def centralizar_janela(janela, largura: int, altura: int) -> None:
    # centralizar qualquer janela criada pelo app em qualquer tela com um principio matemático
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    soma_x = ((tela_largura - largura) // 2) - 8
    soma_y = ((tela_altura - altura) // 2) - 40
    janela.geometry(f"{largura}x{altura}+{soma_x}+{soma_y}")

def criar_coluna_ttk(dominio, nome: str, minwidth: int, width: int, titulo: str) -> None:
    # cria uma coluna no ttk de maneira menos trabalhosa
    dominio.column(nome,minwidth=minwidth,width=width)
    dominio.heading(nome,text=titulo)

def criar_botao_ttk(dominio, width: int, text: str, tamanho_fonte: int, command ,e_negrito: bool = True) -> None:
    # cria um botão ttk de maneira menos trabalhosa
    if e_negrito:
        butt = CTkButton(dominio, width=width, text=text, font=("arial",tamanho_fonte,"bold"), command=command)
    else:
        butt = CTkButton(dominio,width=width, text=text, font=("arial",tamanho_fonte), command=command)
    return butt

main_x = 750
main_y = 450

class Gerenciador():
    # classe principal que vai gerenciar todas as funções do app em si
    def __init__(self) -> None:
        # método de criação e atribuição de variáveis importantes
        self.tem_janela_aberta: bool = False

    def inserir_tarefa(self, treeview) -> None:
        # janela para inserção de tarefas com funcionalidade implementada
        if self.tem_janela_aberta:
            msgbox.showinfo("Aviso", "Já há uma janela aberta.")
        else:
            self.tem_janela_aberta = True
            win_insere = CTkToplevel()
            win_insere.title("Inserir nova tarefa")
            # win_insere.resizable(False,False)
            centralizar_janela(win_insere,main_x,main_y)
            win_insere.geometry("810x300")
            # comando para dar foco na janela Devido a bug do CTk
            win_insere.after(100, win_insere.lift)
            win_insere.protocol("WM_DELETE_WINDOW",lambda: self.gatilhar_fechamento(win_insere))
            
            # criar como inserir tarefa
            label_intro = CTkLabel(win_insere,text="Por favor preencha todos os campos para cadastro da nova tarefa", font=("Arial",20))
            label_intro.place(x=10,y=0)
            
            label_titulo = CTkLabel(win_insere,text="Título:",font=("Arial",15))
            label_titulo.place(x=10,y=70)
            box_entry_titulo = CTkTextbox(win_insere,width=150,height=10)
            box_entry_titulo.place(x=10,y=100)
            
            label_data = CTkLabel(win_insere,text="Data:",font=("Arial",15))
            label_data.place(x=170,y=70)
            box_entry_data = CTkTextbox(win_insere,width=150,height=10)
            box_entry_data.place(x=170,y=100)
            
            label_prioridade = CTkLabel(win_insere,text="Prioridade:",font=("Arial",15))
            label_prioridade.place(x=330,y=70)
            box_entry_prioridade = CTkOptionMenu(win_insere,values=["Baixa","Média","Alta"])
            box_entry_prioridade.place(x=330,y=100)
            
            label_categoria = CTkLabel(win_insere,text="Categoria:",font=("Arial",15))
            label_categoria.place(x=490,y=70)
            box_entry_categoria = CTkTextbox(win_insere,width=150,height=10)
            box_entry_categoria.place(x=490,y=100)
            
            label_status = CTkLabel(win_insere,text="Status:",font=("Arial",15))
            label_status.place(x=650,y=70)
            box_entry_status = CTkOptionMenu(win_insere,values=["Não iniciada","Em andamento","Concluída"])
            box_entry_status.place(x=650,y=100)
            
            label_obs = CTkLabel(win_insere,text="Observações:",font=("Arial",15))
            label_obs.place(x=10,y=150)
            box_entry_obs = CTkTextbox(win_insere,width=790,height=110)
            box_entry_obs.place(x=10,y=180)
            
            butt_confirm = criar_botao_ttk(win_insere,100,"Confirmar",20,lambda: self.inserir_treeview(win_insere,treeview,box_entry_titulo,box_entry_data,box_entry_prioridade,box_entry_categoria,box_entry_status,box_entry_obs))
            butt_confirm.place(x=695,y=10)
            
    def atualizar_tarefa(self, treeview) -> None:
        # janela para atualização de alguma tarefa já existente no programa
        item_selecionado = treeview.selection()
        if self.tem_janela_aberta:
            msgbox.showinfo("Aviso", "Já há uma janela aberta.")
        elif not item_selecionado:
            msgbox.showerror("Erro: seleção inválida","Nenhum item foi selecionado, clique no item desejado...")
        else:
            self.tem_janela_aberta = True
            win_atualiza = CTkToplevel()
            win_atualiza.title("Atualizar Tarefa")
            # win_atualiza.resizable(False,False)
            centralizar_janela(win_atualiza,main_x,main_y)
            win_atualiza.geometry("810x300")
            # comando para dar foco na janela Devido a bug do CTk
            win_atualiza.after(100, win_atualiza.lift)
            win_atualiza.protocol("WM_DELETE_WINDOW",lambda: self.gatilhar_fechamento(win_atualiza))
            
            items = treeview.item(item_selecionado, "values")
            print([i for i in items])
            
            label_titulo = CTkLabel(win_atualiza,text="Título:",font=("Arial",15))
            label_titulo.place(x=10,y=70)
            box_entry_titulo = CTkTextbox(win_atualiza,width=150,height=10)
            box_entry_titulo.insert("0.0",items[0])
            box_entry_titulo.place(x=10,y=100)
            
            label_data = CTkLabel(win_atualiza,text="Data:",font=("Arial",15))
            label_data.place(x=170,y=70)
            box_entry_data = CTkTextbox(win_atualiza,width=150,height=10)
            box_entry_data.insert("0.0",items[1])
            box_entry_data.place(x=170,y=100)
            
            label_prioridade = CTkLabel(win_atualiza,text="Prioridade:",font=("Arial",15))
            label_prioridade.place(x=330,y=70)
            box_entry_prioridade = CTkOptionMenu(win_atualiza,values=["Baixa","Média","Alta"])
            box_entry_prioridade.set(items[2])
            box_entry_prioridade.place(x=330,y=100)
            
            label_categoria = CTkLabel(win_atualiza,text="Categoria:",font=("Arial",15))
            label_categoria.place(x=490,y=70)
            box_entry_categoria = CTkTextbox(win_atualiza,width=150,height=10)
            box_entry_categoria.insert("0.0",items[3])
            box_entry_categoria.place(x=490,y=100)
            
            label_status = CTkLabel(win_atualiza,text="Status:",font=("Arial",15))
            label_status.place(x=650,y=70)
            box_entry_status = CTkOptionMenu(win_atualiza,values=["Não iniciada","Em andamento","Concluída"])
            box_entry_status.set(items[4])
            box_entry_status.place(x=650,y=100)
            
            label_obs = CTkLabel(win_atualiza,text="Observações:",font=("Arial",15))
            label_obs.place(x=10,y=150)
            box_entry_obs = CTkTextbox(win_atualiza,width=790,height=110)
            box_entry_obs.insert("0.0",items[5])
            box_entry_obs.place(x=10,y=180)
            
            butt_confirm = criar_botao_ttk(win_atualiza,100,"Confirmar",20,lambda: self.atualizar_treeview(win_atualiza,item_selecionado,treeview,box_entry_titulo,box_entry_data,box_entry_prioridade,box_entry_categoria,box_entry_status,box_entry_obs))
            butt_confirm.place(x=695,y=10)
            

    def exibir_tarefa(self,treeview) -> None:
        # janela para exibição completa de alguma tarefa já existente incluindo as observações
        if self.tem_janela_aberta:
            msgbox.showinfo("Aviso", "Já há uma janela aberta.")
        else:
            item_selecionado = treeview.selection()
            if item_selecionado:
                self.tem_janela_aberta = True
                win_exibe = CTkToplevel()
                win_exibe.title("Exibir Tarefa")
                # # win_exibe.resizable(False,False)
                centralizar_janela(win_exibe,main_x,main_y)
                win_exibe.geometry("810x300")
                # comando para dar foco na janela Devido a bug do CTk
                win_exibe.after(100, win_exibe.lift)
                win_exibe.protocol("WM_DELETE_WINDOW",lambda: self.gatilhar_fechamento(win_exibe))
                
                items = treeview.item(item_selecionado, "values")
                
                label_titulo = CTkLabel(win_exibe,text="Título:",font=("Arial",15))
                label_titulo.place(x=10,y=70)
                text_titulo = CTkLabel(win_exibe,text=items[0],font=("Arial",15),bg_color="#1d1e1e",width=150)
                text_titulo.place(x=10,y=100)
                
                label_data = CTkLabel(win_exibe,text="Data:",font=("Arial",15))
                label_data.place(x=170,y=70)
                text_data = CTkLabel(win_exibe,text=items[1],font=("Arial",15),bg_color="#1d1e1e",width=150)
                text_data.place(x=170,y=100)
                
                label_prioridade = CTkLabel(win_exibe,text="Prioridade:",font=("Arial",15))
                label_prioridade.place(x=330,y=70)
                text_prioridade = CTkLabel(win_exibe,text=items[2],font=("Arial",15),bg_color="#1d1e1e",width=150)
                text_prioridade.place(x=330,y=100)
                
                label_categoria = CTkLabel(win_exibe,text="Categoria:",font=("Arial",15))
                label_categoria.place(x=490,y=70)
                text_categoria = CTkLabel(win_exibe,text=items[3],font=("Arial",15),bg_color="#1d1e1e",width=150)
                text_categoria.place(x=490,y=100)
                
                label_status = CTkLabel(win_exibe,text="Status:",font=("Arial",15))
                label_status.place(x=650,y=70)
                text_status = CTkLabel(win_exibe,text=items[4],font=("Arial",15),bg_color="#1d1e1e",width=150)
                text_status.place(x=650,y=100)
                
                label_obs = CTkLabel(win_exibe,text="Observações:",font=("Arial",15))
                label_obs.place(x=10,y=150)
                box_entry_obs = CTkTextbox(win_exibe,width=790,height=110,font=("Arial",15))
                box_entry_obs.insert("0.0",items[5])
                box_entry_obs.configure(state="disabled")
                box_entry_obs.place(x=10,y=180)  
            else:
                msgbox.showerror("Erro: seleção inválida","Nenhum item foi selecionado, clique no item desejado...")
            

    def deletar_tarefa(self,treeview) -> None:
        # funcionalidade para deletar uma tarefa já existente
        if self.tem_janela_aberta:
            msgbox.showinfo("Aviso", "Já há uma janela aberta.")
        else:
            item_selecionado = treeview.selection()
            if item_selecionado:
                answer = msgbox.askyesno("Confirmação","Você realmente deseja deletar essa tarefa?")
                if answer:
                    treeview.delete(item_selecionado)
            else:
                msgbox.showerror("Erro: seleção inválida","Nenhum item foi selecionado, clique no item desejado...")
    
    def gatilhar_fechamento(self, dominio):
        # função utilizada como gatilho para notificar ao programa que não tem nenhuma
        # janela aberta no momento
        self.tem_janela_aberta = False
        dominio.destroy()
    
    def capturar_e_validar_campos(self,box_entry_titulo,box_entry_data,box_entry_prioridade,box_entry_categoria,box_entry_status,box_entry_obs) -> list:
        # atribuição de variaveis
        titulo = box_entry_titulo.get("1.0","end").strip()
        data = box_entry_data.get("1.0","end").strip()
        prioridade = box_entry_prioridade.get()
        categoria = box_entry_categoria.get("1.0","end").strip()
        status = box_entry_status.get()
        obs = box_entry_obs.get("1.0","end").strip()
        
        # validação de campos vazios
        if not titulo or not data or not categoria:
            msgbox.showerror("ERRO: Campo vazio","Todos os campos precisam estar preenchidos, por favor tente novamente")
            return
        # validação de data
        try:
            datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            msgbox.showerror("ERRO: Formato de data inválido", "Formato de data inválido. Use DD/MM/AAAA.")
            return
        
        # criação da lista de campos validados
        insert = [titulo,data,prioridade,categoria,status,obs]
        return insert
        
    def inserir_treeview(self,dominio,treeview,box_entry_titulo,box_entry_data,box_entry_prioridade,box_entry_categoria,box_entry_status,box_entry_obs) -> None:
        # função utilizada para captar os campos da janela de inserção e atribuir eles
        # a uma linha do treeview principal na win_main
        insert = self.capturar_e_validar_campos(box_entry_titulo,box_entry_data,box_entry_prioridade,box_entry_categoria,box_entry_status,box_entry_obs)
        # verificando funcionamento da função capturar_e_valida_campos
        if insert:
            treeview.insert("","end",values=insert)
            self.gatilhar_fechamento(dominio)
    
    def atualizar_treeview(self,dominio,item_selecionado,treeview,box_entry_titulo,box_entry_data,box_entry_prioridade,box_entry_categoria,box_entry_status,box_entry_obs) -> None:
        # função utilizada para captar os campos da janela de atualização e atribuir eles
        # a linha selecionada anteriormente na win_main
        insert = self.capturar_e_validar_campos(box_entry_titulo,box_entry_data,box_entry_prioridade,box_entry_categoria,box_entry_status,box_entry_obs)
        # verificando funcionamento da função capturar_e_valida_campos
        if insert:
            treeview.item(item_selecionado, values=insert)
            self.gatilhar_fechamento(dominio)
        

gerenciador = Gerenciador()