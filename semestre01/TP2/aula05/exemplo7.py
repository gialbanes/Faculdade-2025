from tkinter import * 

tela = Tk()
tela.title("teste")
tela.configure(background="grey")
tela.geometry("600x600")
tela.resizable(True, True)
tela.maxsize(width=400, height=400)
tela.minsize(width=800, height=800)

# objetivo: formatar labels

lbl_nome = Label(tela, text="Nome", font="Arial 20 bold italic", fg="red").place(x=10, y=10)
lbl_cof = Label(tela, text="CPF", font="Arial 15 bold", fg="green").place(x=10, y=50)

tela.mainloop()
