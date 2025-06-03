from tkinter import * 
from tkinter.ttk import * 
import pymongo 

tela = Tk()
tela.title("Cadastro de clientes")
tela.geometry("800x800")

conexao = pymongo.MongoClient("mongodb://localhost:27017/")
banco = conexao["sistema"]
conexao = banco["clientes"]

lbl_nome = Label(tela, text="Nome: ", font="Arial 12").place(x=10, y=10)
txt_nome = Entry(tela, width=20, background="white")
txt_nome.place(x=80, y=10)

# radiobutton para o sexo
var = StringVar()
var.set("m")
lbl_sexo = Label(tela, text="Sexo: ", font="Arial 12").place(x=10, y=40)
radiom = Radiobutton(tela, text="M", variable=var, value="m").place(x=60, y=40)
rafiof = Radiobutton(tela, text="F", variable=var, value="f").place(x=100, y=40)

# combobox para cidade 
lbl_cidade = Label(tela, text="Cidade: ", font="Arial 12").place(x=10, y=70)

combo = Combobox(tela)
combo['values'] = ['Cananéia', 'Iguape', 'Registro']
combo.current(0)
combo.place(x=80, y=70)


tela.mainloop()