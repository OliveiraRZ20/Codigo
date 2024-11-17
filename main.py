from tkinter import *
from functions import *
from tkinter import ttk
import sys

# criacao e ajuste da janela
win_main = Tk()
win_main.title("Gerenciador de tarefas")
win_main.resizable(False,False)
win_main.configure(bg="white")
win_main.iconbitmap(sys.executable)

centralizar_janela(win_main,1500,450)

# criação da visualização da tabela
tv = ttk.Treeview(win_main, columns=('titulo','data','prioridade','categoria','status'), show='headings')
criar_coluna_ttk(tv,'titulo',0,125,'Título')
criar_coluna_ttk(tv,'data',0,75,'Data')
criar_coluna_ttk(tv,'prioridade',0,100,'Prioridade')
criar_coluna_ttk(tv,'categoria',0,125,'Categoria')
criar_coluna_ttk(tv,'status',0,100,'Status')
tv.pack()

tv.insert("","end",values=["Dever de casa","17/10/2024","ALTA","Escola","Em andamento"])
sdoKODkoskdoaskdsoa


# inicializa a janela principal
win_main.mainloop()

