from tkinter import * 
from tkinter import ttk
import tkinter as tk
import pymongo

tela = Tk()
tela.title("Cadastro de veículos")
tela.geometry("700x700")
tela.configure(bg="grey")
var = StringVar()
var.set("")

# configuração do mongodb
exercicios = pymongo.MongoClient("mongodb://localhost:27017/")
db = exercicios["exercicios"]
collection = db["veiculos"]

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
    idade = txt_idade.get()
    sexo = var.get()
    cidade = combo.get()
    dataNasc = txt_dataNasc.get()
    
    txt_codigo.delete(0, END)
    txt_nome.delete(0, END)
    txt_idade.delete(0, END)
    combo.set("")
    txt_dataNasc.delete(0, END)
    
    veiculos = {"codigo": codigo, "nome": nome, "idade": idade, "sexo": sexo, "cidade": cidade, "dataNasc": dataNasc}
    collection.insert_one(veiculos)

def consultar():
    codigo = txt_codigo.get()
    veiculos = collection.find_one({"codigo": codigo})
    if veiculos:
        txt_nome.delete(0, END)
        txt_nome.insert(0, veiculos.get("nome", ""))
        
        txt_idade.delete(0, END)
        txt_idade.insert(0, veiculos.get("idade", ""))
        
        var.set(veiculos.get("sexo", ""))
        combo.set(veiculos.get("cidade", ""))
        
        txt_dataNasc.delete(0, END)
        txt_dataNasc.insert(0, veiculos.get("dataNasc", "")) 
        
    else:
        tk.messagebox.showinfo("Consulta", f"Nenhum cliente encontrado com o código '{codigo}'")  

def atualizar():
    codigo = txt_codigo.get() 
    nome = txt_nome.get() 
    idade = txt_idade.get() 
    sexo = var.get() 
    cidade = combo.get() 
    dataNasc = txt_dataNasc.get() 
    
    collection.update_one({"codigo": codigo}, {"$set": {"codigo": codigo, "nome": nome, "idade": idade, "sexo": sexo, "cidade": cidade, "dataNasc": dataNasc}})

def deletar():
    codigo = txt_codigo.get()
    collection.delete_one({"codigo": codigo})

# botões do crud 
btn_salvar = Button(tela, text="Salvar", command=salvar)
btn_salvar.place(x=130, y=310)

btn_consultar = Button(tela, text="Consultar", command=consultar)
btn_consultar.placex(x=210, y=310)

btn_deletar = Button(tela, text="Deletar", command=deletar)
btn_deletar.place(x=300, y=310)

btn_editar = Button(tela, text="Editar", command=atualizar)
btn_editar.place(x=390, y=310)

btn_sair = Button(tela, text="Sair", command=tela.quit)
btn_sair.place(x=480, y=310)
    
tela.mainloop()