from customtkinter import *
from tkinter import ttk
from functions import *
# retirar depois pois não serve de nada, so pra limpar o terminal
import os
os.system("cls")

# configurações iniciais da janela principal
set_appearance_mode("System")
set_default_color_theme("blue")
win_main = CTk()
win_main.title("Gerenciador de tarefas")
win_main.resizable(False,False)
win_main.iconbitmap(sys.executable)

centralizar_janela(win_main,750,450)

# criando e definindo parametros da planilha de tarefas
style = ttk.Style(win_main)
style.theme_use("clam")
style.configure("Treeview", background="#242424", fieldbackground="#242424", foreground="white")

tv = ttk.Treeview(win_main, columns=('titulo','data','prioridade','categoria','status'), show='headings')
criar_coluna_ttk(tv,'titulo',0,110,'Título')
criar_coluna_ttk(tv,'data',0,110,'Data')
criar_coluna_ttk(tv,'prioridade',0,110,'Prioridade')
criar_coluna_ttk(tv,'categoria',0,110,'Categoria')
criar_coluna_ttk(tv,'status',0,110,'Status')
tv.place(x=100,y=0)

# criando e localizando os botões de funcionalidade
posicao_butts = 100

butt_insere = criar_botao_ttk(win_main,100,"Inserir",20,inserir_tarefa)
butt_insere.place(x=posicao_butts,y=250)

butt_atualiza = criar_botao_ttk(win_main,100,"Atualizar",20,inserir_tarefa)
butt_atualiza.place(x=posicao_butts+150,y=250)

butt_exibe = criar_botao_ttk(win_main,100,"Exibir",20,inserir_tarefa)
butt_exibe.place(x=posicao_butts+300,y=250)

butt_deleta = criar_botao_ttk(win_main,100,"Deletar",20,inserir_tarefa)
butt_deleta.place(x=posicao_butts+450,y=250)

# tv.insert("","end",values=["Dever de casa","17/10/2024","ALTA","Escola","Em andamento"])
# tv.insert("","end",values=["Fazer o jantar","25/10/2024","MEDIA","Casa","Não iniciada"])


win_main.mainloop()