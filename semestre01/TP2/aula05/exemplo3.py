# importa o tkinter
from tkinter import * 

# variável da tela
tela = Tk()

# título da janela 
tela.title("fatec registro")
# cor de fundo da janela 
tela.configure(background="grey")
# tamanho da tela
tela.geometry("700x600")
# permite o reajuste do tamanho da janela
tela.resizable(True, True)
# tamanho máximo da tela
tela.maxsize(width=800, height=800)
# tamanho mínimo da tela
tela.minsize(width=400, height=400)

tela.mainloop