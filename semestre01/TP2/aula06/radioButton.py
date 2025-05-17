from tkinter import *

tela = Tk()
tela.title("Radio Button")
tela.configure(background="grey")
tela.geometry("600x600")

var = StringVar() # guarda o valor selecionado dos botões de opção
var.set("m") # ao abrir o app, o padrão já vai vir com o m selecionado 

rdb_buttonm = Radiobutton(tela, text="M", variable=var, value="m").place(x=20, y=40) # var recebe o valor M se essa for a opção escolhida
rdb_buttonf = Radiobutton(tela, text="F", variable=var, value="f").place(x=20, y=60) # var recebe o valor F se essa for a opção escolhida

tela.mainloop()