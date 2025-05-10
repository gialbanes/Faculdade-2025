from tkinter import * 

tela = Tk()
tela.title("teste")
tela.configure(background="grey")
tela.geometry("600x600")
tela.resizable(True, True)
tela.maxsize(width=400, height=400)
tela.minsize(width=800, height=800)

lbl_nome = Label(tela, text="Nome").place(x=10, y=10)
lbl_cpd = Label(tela, text="CPF").place(x=10, y=50)

tela.mainloop