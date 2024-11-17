from tkinter import *
from functions import *
from tkinter import ttk
import sys

# criacao e ajuste da janela
win_main = Tk()
win_main.title("Gerenciador de compromissos")
win_main.resizable(False,False)
win_main.configure(bg="white")
win_main.iconbitmap(sys.executable)

centralizar_janela(win_main,500,500)

tv = ttk.Treeview(win_main, columns=('id'), show='headings')
tv.column('id',minwidth=0,width=100)
tv.heading('id',text='ID')
tv.pack()

tv.insert("","end",values=("10"))





# inicializa a janela principal
win_main.mainloop()

