from tkinter import *
from tkinter import ttk
import tkinter as tk
import pymongo

# configuração da tela 
tela = Tk()
tela.title("Exemplo Mongo DB")
tela.geometry("800x600")
tela.resizable("true, true")
tela.configure(background="#ffffff")

# configuração do banco de dados
exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db = exemplo["exemplo"]
collection = db["clientes"]

# cadastro de clientes
lbl_codigo = Label(tela, text="Código:", bg="#ffffff").place(x=130, y=140)
txt_codigo = Entry(tela, width=20, borderwith=2, fg="black", bg="white").place(x=190, y=140)

lbl_nome = Label(tela, text="Nome:", bg="#ffffff").place(x=130, y=170)
txt_nome = Entry(tela, width=40, borderwidth=2, fg="black", bg="white").place(x=190, y=170).inser(0, "")

lbl_cpf = Label(tela, text="CPF:", bg="#ffffff").place(x=450, y=170)
txt_cpf = Entry(tela, width=20, borderwidth=2, fg="black", bg="white").place(x=480, y=170).insert(0, "")

lbl_idade = Label(tela, text="Idade:", bg="#ffffff").place(x=130, y=200)
txt_idade = Entry(tela, width=20, borderwidth=2, fg="black", bg="white").place(x=190, y=200).insert(0, "")

lbl_end = Label(tela, text="Endereço:", bg="#ffffff").place(x=450, y=250)
txt_end = Entry(tela, width=25, borderwith=2, fg="black", bg="white").place(x=480, y=200).insert(0, "")

lbl_bairro = Label(tela, text="Bairro:", bg="#ffffff").place(x=130, y=230)
txt_bairro = Entry(tela, width=20, borderwidth=2, fg="black", bg="white").place(x=190, y=230).insert(0, "")

lbl_estado = Label(tela, text="Estado:", bg="ffffff").place(x=330, y=230)
comboestado = ttk.ComboBox(tela,
                           values=[
                               "São Paulo",
                               "Rio de Janeiro",
                               "Minas Gerais",
                                "Espirito Santo",
                           ],)
#comboestado.grid(column=0, row=1) sistema de posicionamento
#comboestado.place(x=370, y=230)

lbl_cidade = Label(tela, text="Cidade:", bg="#ffffff").place(x=520, y=230)
txt_cidade = Entry(tela, width=20, borderwidth=2, fg="black", bg="white").place(x=570, y=230).insert(0, "")

# função salvar 
def salvar():
    # pega os dados do formulário 
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    end = txt_end.get()
    cpf = txt_cpf.get()
    bairro = txt_bairro.get()
    estado = comboestado.get()
    cidade = txt_cidade.get()

    # após a inserção dos dados as caixas de textos, será apagada automaticamente
    txt_codigo.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_idade.delete(0, tk.END)
    txt_end.delete(0, tk.END)
    txt_cpf.delete(0, tk.END)
    txt_bairro.delete(0, tk.END)
    txt_cidade.delete(0, tk.END)
    comboestado.set("")
    txt_bairro.delete(0, tk.END)

    # inserção dos dados dicionário dos dados
    cliente ={"Código": codigo, "Nome": nome, "Idade": idade, "Endereço": end, "CPF": cpf, "Bairro": bairro, "Estado": estado, "Cidade": cidade}
    collection.inser_one(cliente)

# função de atualizar 
def atualizar():
    # pega os dados do formulário 
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    end = txt_end.get()
    cpf = txt_cpf.get()
    bairro = txt_bairro.get()
    estado = comboestado.get()
    cidade = txt_cidade.get()

    # método update 
    collection.update_one({"Código": codigo}, {"$set": {"Código": codigo, "Nome": nome, "Idade": idade, "Endereço": end, "CPF": cpf, "Bairro": bairro, "Estado": estado, "Cidade": cidade}})

# função para apagar dados
def deletar():
    codigo = txt_codigo.get()
    collection.delete_one({"Código": codigo})

# botões para chamar as funções
btn_salvar = Button(tela, text="Salvar", width=10, height=2, bg="#ffffff", fg="black", command=salvar).place(x=130, y=280)
btn_alterar = Button(tela, text="Alterar", width=10, height=2, bg="#ffffff", fg="black", command=atualizar).place(x=220, y=280)
btn_excluir = Button(tela, text="Excluir", width=10, height=2, bg="#ffffff", fg="black", command=deletar).place(x=310, y=280)
btn_sair = Button(tela, text="Sair", width=10, height=2, bg="#ffffff", fg="black", command=tela.quit).place(x=400, y=280)
tela.mainloop()