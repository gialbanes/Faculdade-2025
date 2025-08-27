from tkinter import * 
from tkinter import ttk
import tkinter as tk 
import pymongo

tela = Tk()
tela.title("Cadastro de clientes")
tela.configure(background="grey")
tela.geometry("700x700")
var = StringVar()
var.set("")

# configuração do mongodb
exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db = exemplo["exemplo"]
collection = db["clientes"]

# título na janela 
lbl_titulo = Label(tela, text="Cadastro de clientes", font="Arial 20 bold italic", fg="black", bg="grey")
lbl_titulo.pack()

# Labels e Entradas
lbl_codigo = Label(tela, text="Digite o código:")
lbl_codigo.place(x=10, y=60)
txt_codigo = Entry(tela, width=20, bg="white")
txt_codigo.place(x=150, y=60)

lbl_nome = Label(tela, text="Digite seu nome:")
lbl_nome.place(x=10, y=90)
txt_nome = Entry(tela, width=20, bg="white")
txt_nome.place(x=150, y=90)

lbl_idade = Label(tela, text="Digite sua idade:")
lbl_idade.place(x=10, y=120)
txt_idade = Entry(tela, width=20, bg="white")
txt_idade.place(x=150, y=120)

lbl_sexo = Label(tela, text="Digite seu sexo:")
lbl_sexo.place(x=10, y=150)
rdb_buttonm = Radiobutton(tela, text="M", variable=var, value="m")
rdb_buttonm.place(x=150, y=150)
rdb_buttonf = Radiobutton(tela, text="F", variable=var, value="f")
rdb_buttonf.place(x=200, y=150)

lbl_cidade = Label(tela, text="Digite sua cidade:")
lbl_cidade.place(x=10, y=180)
combo = ttk.Combobox(tela)
combo['values'] = ("Iguape", "Registro", "Cananeia", "Ilha Comprida")
combo.place(x=150, y=180)
combo.current(0)  

lbl_dataNasc = Label(tela, text="Digite sua data de nascimento:")
lbl_dataNasc.place(x=10, y=210)
txt_dataNasc = Entry(tela, width=20, bg="white")
txt_dataNasc.place(x=230, y=210)

def salvar():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    sexo = var.get()
    cidade = combo.get()
    dataNasc = txt_dataNasc.get()
    
    txt_codigo.delete(0, END)
    txt_nome.delete(0, END)
    txt_idade.delete(0, END)
    combo.set("")
    txt_dataNasc.delete(0, END)
    # dicionário de clientes com chave e valor obtido de variáveis existentes no código
    cliente = {"codigo": codigo, "nome": nome, "idade": idade, "sexo": sexo, "cidade": cidade, "dataNasc": dataNasc}
    # collection é a instância do coleção do db
    # insert_one insere o dicionário cliente na coleção 
    collection.insert_one(cliente)

def consultar():
    codigo = txt_codigo.get()
    cliente = collection.find_one({"codigo": codigo})
    if cliente:
        txt_nome.delete(0, END)
        txt_nome.insert(0, cliente.get("nome", ""))

        txt_idade.delete(0, END)
        txt_idade.insert(0, cliente.get("idade", ""))

        var.set(cliente.get("sexo", ""))

        combo.set(cliente.get("cidade", ""))

        txt_dataNasc.delete(0, END)
        txt_dataNasc.insert(0, cliente.get("dataNasc", ""))
    else:
        tk.messagebox.showinfo("Consulta", f"Nenhum cliente encontrado com o código '{codigo}'")


def atualizar():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    sexo = var.get()
    cidade = combo.get()
    dataNasc = txt_dataNasc.get()
    
    # o primeiro argumento é pra filtrar o documento que eu quero atualizar 
    # o segundo argumento é um dicionário que usa o $set para especificar quais campos e valores devems er atualizados 
    collection.update_one({"codigo": codigo}, {"$set": {"código": codigo, "nome": nome, "idade": idade, "sexo": sexo, "cidade": cidade, "dataNasc": dataNasc}})
    
def deletar():
    codigo = txt_codigo.get()
    # o argumento especifica o criterio, que o campo código esteja de acordo com a variável código 
    collection.delete_one({"codigo": codigo})

# botões do crud 
btn_salvar = Button(tela, text="Salvar", command=salvar)
btn_salvar.place(x=130, y=310)

btn_consultar = Button(tela, text="Consultar", command=consultar)
btn_consultar.place(x=210, y=310)

btn_deletar = Button(tela, text="Deletar", command=deletar)
btn_deletar.place(x=300, y=310)

btn_editar = Button(tela, text="Editar", command=atualizar)
btn_editar.place(x=390, y=310)

btn_sair = Button(tela, text="Sair", command=tela.quit)
btn_sair.place(x=480, y=310)
    
tela.mainloop()
    