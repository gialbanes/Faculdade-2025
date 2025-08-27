from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Combobox")
janela.geometry("250x250")

combo = ttk.Combobox(janela) 
combo['values'] = ("Iguape", "Ilha Comprida", "Cananéia", "Registro")
combo.current(1) # define o item que será mostrado no combobox ao iniciar
combo.pack()

janela.mainloop()