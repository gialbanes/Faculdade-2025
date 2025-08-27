from tkinter import *
from tkinter import ttk
import tkinter as tk
import pymongo

tela = Tk()
tela.title("Exemplo Mongo DB")
tela.geometry("800x600")
tela.resizable(True, True)
tela.configure(bg="#fff")

exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db = exemplo["exemplo"]
collection = db["clientes"]

lbl_codigo = Label(tela, text="Cadastro de clientes", bg="#fff").place(x=130,  y=80)
lbl_codigo = Label(tela, text="Código:", bg="#fff").place(x=130, y=140)
txt_codigo = Entry(tela, width=20, borderwidth=2, fg="black")
txt_codigo.place(x=190, y=140)

lbl_nome = Label(tela, text="Nome:", bg="#fff").place(x=130, y=170)
txt_nome = Entry(tela, width=20, borderwidth=2, fg="black")
txt_nome.place(x=190, y=170)

lbl_cpf = Label(tela, text="CPF:", bg="#fff").place(x=450, y=170)
txt_cpf = Entry(tela, width=20, borderwidth=2, fg="black")
txt_cpf.place(x=480, y=170)

lbl_idade = Label(tela, text="Idade:", bg="#fff").place(x=130, y=200)
txt_idade = Entry(tela, width=20, borderwidth=2, fg="black")
txt_idade.place(x=190, y=200)
txt_idade.insert(0, "")

lbl_end = Label(tela, text="Rua:", bg="#fff").place(x=450, y=200)
txt_end = Entry(tela, width=20, borderwidth=2, fg="black")
txt_end.place(x=480, y=200)
txt_end.insert(0, "")

lbl_bairro = Label(tela, text="Bairro:", bg="#fff").place(x=130, y=230)
txt_bairro = Entry(tela, width=20, borderwidth=2, fg="black")
txt_bairro.place(x=190, y=230)
txt_bairro.insert(0, "")

lbl_estado = Label(tela, text="Estado:", bg="#fff").place(x=330, y=230)
comboestado = ttk.Combobox(tela,
                           values=[
                               "São Paulo", 
                               "Rio de Janeiro", 
                               "Minas Gerais", 
                               "Espírito Santo"])
comboestado.grid(row=1, column=0)
comboestado.place(x=380, y=230)

lbl_cidade = Label(tela, text="Cidade:", bg="#fff").place(x=530, y=230)
txt_cidade = Entry(tela, width=20, borderwidth=2, fg="black")
txt_cidade.place(x=580, y=230)
txt_cidade.insert(0, "")

def salvar():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    cpf = txt_cpf.get()
    idade = txt_idade.get()
    rua = txt_end.get()
    bairro = txt_bairro.get()
    estado = comboestado.get()
    cidade = txt_cidade.get()

    txt_codigo.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_cpf.delete(0, tk.END)
    txt_idade.delete(0, tk.END)
    txt_end.delete(0, tk.END)
    txt_bairro.delete(0, tk.END)
    comboestado.set("")
    txt_cidade.delete(0, tk.END)

    cliente = {
        "codigo": codigo,
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "rua": rua,
        "bairro": bairro,
        "estado": estado,
        "cidade": cidade
    }

    collection.insert_one(cliente)

def atualizar():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = txt_idade.get()
    cpf = txt_cpf.get()
    rua = txt_end.get()
    bairro = txt_bairro.get()
    cidade = txt_cidade.get()
    estado = comboestado.get()

    collection.update_one({"codigo": codigo}, {"$set": {"codigo": codigo, "nome": nome, "idade": idade,  "cpf": cpf, "rua": rua, "bairro": bairro, "estado": estado, "cidade": cidade}})

def excluir():
    codigo = txt_codigo.get()
    collection.delete_one({"codigo": codigo})
    txt_codigo.delete(0, tk.END)

def consultar():
    codigo = txt_codigo.get()
    resultado = collection.find_one({"codigo": codigo})

    if resultado:
        txt_nome.insert(END, f"{resultado['nome']}")
        txt_cidade.insert(END, f"{resultado['cidade']}")
        txt_idade.insert(END, f"{resultado['idade']}")
        txt_end.insert(END, f"{resultado['rua']}")
        txt_cpf.insert(END, f"{resultado['cpf']}")
        txt_bairro.insert(END, f"{resultado['bairro']}")
        comboestado.insert(END, f"{resultado['estado']}")
    else: 
        lbl_resultado.config(text="Nenhum resultado encontrado")

lbl_resultado = Label(tela, text="", bg="#ffffff")
lbl_resultado.place(x=490, y=310)

btn_salvar = Button(tela, text="Salvar", command=salvar, bg="#4CAF50", fg="white")
btn_salvar.place(x=130, y=300)
btn_atualizar = Button(tela, text="Atualizar", command=atualizar, bg="#2196F3", fg="white")
btn_atualizar.place(x=200, y=300)
btn_excluir = Button(tela, text="Excluir", command=excluir, bg="#f44336", fg="white")
btn_excluir.place(x=270, y=300)
btn_fechar = Button(tela, text="Fechar", command=tela.quit, bg="#f44336", fg="white")
btn_fechar.place(x=350, y=300)
btn_consultar = Button(tela, text="Consultar", command=consultar, bg="#2196F3", fg="white").place(x=490, y=280)

tela.mainloop()