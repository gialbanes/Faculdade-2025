from tkinter import * 
from tkinter.ttk import * 
import pymongo 

tela = Tk()
tela.title("Cadastro de clientes")
tela.geometry("400x400")

# conexão com o banco 
conexao = pymongo.MongoClient("mongodb://localhost:27017/")
banco = conexao["sistema"]
colecao = banco["clientes"]

# nome do cliente
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

# função para salvar um cliente
def salvar():
    nome = txt_nome.get()
    sexo = var.get()
    cidade = combo.get()

    txt_nome.delete(0, END)
    var.set("m")
    combo.current(0)

    cliente = {"nome": nome, "sexo": sexo, "cidade": cidade}
    conexao.insert_one(cliente)


btn_salvar = Button(tela, text="Salvar", command=salvar)
btn_salvar.place(x=10, y=100)

# função para ler um cliente
def listar():
    clientes = conexao.find()
    for client in clientes:
        print(f"Nome: {client['nome']}, Sexo: {client['sexo']}, Cidade: {client['cidade']}")

btn_listar = Button(tela, text="Listar", command=listar)
btn_listar.place(x=80, y=100)

# função para atualizar um cliente
def update():
    nome = txt_nome.get()
    sexo = var.get()
    cidade = combo.get()

    colecao.update_one({"nome": nome}, {"$set": {"sexo": sexo, "cidade": cidade}})

btn_update = Button(tela, text="Atualizar", command=update)
btn_update.place(x=150, y=100)

def delete():
    nome = txt_nome.get()
    colecao.delete_one({"nome": nome})

btn_deletar = Button (tela, text="Deletar", command=delete)
btn_deletar.place(x=220, y=100)
tela.mainloop()