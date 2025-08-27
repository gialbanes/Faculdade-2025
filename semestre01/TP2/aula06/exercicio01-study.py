# importando o sqlite e PIL para trabalhar com imgs
import sqlite3
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

tela = Tk()
tela.title("Controle de pessoas")
tela.configure(background="grey")
var = StringVar()
var.set("")
largura = 800
altura = 600

#criacao do db
conn = sqlite3.connect("mydb.db")
#criar cursor - objeto que permite executar comandos sql 
cur = conn.cursor()
# criar tabela 
cur.execute("CREATE TABLE IF NOT EXISTS pessoas(codigo int primary key, nome text, idade int, sexo text, cidade text, datanasc);")
# commitar as mudanças 
conn.commit()
# fechar a conexao 
conn.close()

# Título
lbl_titulo = Label(tela, text="Controle de pessoas", font="Arial 20 bold italic", fg="black", bg="grey")
lbl_titulo.pack(pady=10)

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
    conn = sqlite3.connect("mydb.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO pessoas VALUES (:codigo, :nome, :idade, :sexo, :cidade, :datanasc)", {'codigo': txt_codigo.get(), 'nome': txt_nome.get(), 'idade': txt_idade.get(), 'sexo': var.get(), 'cidade': combo.get(), 'dataNasc': txt_dataNasc.get()})
    conn.commit()
    conn.close()
    
    # limpar as textboxes
    txt_codigo.delete(0, END)
    txt_nome.delete(0, END)
    txt_idade.delete(0, END)
    txt_dataNasc.delete(0, END)
    
def consultar():
    conn = sqlite3.connect("mydb.db")
    cur = conn.cursor()
    # faz a consulta na tabela de tudo pelo codigo
    cur.execute("SELECT *, codigo FROM pessoas")
    # pega todos os registros retornados na ultima consulta no db
    # records vai ser uma lista de tuplas, onde cada tupla representa uma linha da tabela 
    records = cur.fetchall()
    # string que vai armazenar os dados formatados 
    print_records = ""
    # percorre cada linha
    for rec in records:
        print_records += 'Código: ' + str(rec[0]) + 'Nome:' + str(rec[1]) + '\n Idade:' + rec(str[2]) + '\n Sexo:' + rec(str[3]) + '\n Cidade:' + rec(str[4]) + '\n Data de nascimento:' + rec(str[5])
    
    # posicionando os resultados
    Label(tela, text=print_records).place(x=20, y=320)
    
    conn.commit()
    conn.close()
    
def deletar():
    conn = sqlite3.connect("mydb.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM pessoas WHERE codigo = " + txt_codigo.get())
    conn.commit()
    conn.close()
    #mostrar msg na tela
    messagebox.showinfo("Excluindo...", "Regitro excluído com sucesso!")
    
def atualizar():
    conn = sqlite3.connect("mydb.db")
    cur = conn.cursor()
    # pega o código que sofrerá alteração
    record_id = txt_codigo.get()
    cur.execute("UPDATE pessoas SET nome = :nome, idade = :idade, sexo = :sexo, cidade = :cidade, dataNasc = :dataNasc WHERE codigo = :codigo", { 'nome': txt_nome.get(), 'idade': txt_idade.get(), 'sexo': var.get(), 'cidade': combo.get(), 'dataNasc': txt_dataNasc.get(), 'codigo': record_id})
    conn.commit()
    conn.close()
    
# fotos dos botões do crud 
# .resize() para não ficar desproporcional 
foto_salvar = Image.open(r"icones\salvar.png").resize((30,30))
foto_consultar = Image.open(r"icones\consultar.png").resize((30,30))
foto_deletar = Image.open(r"icones\excluir.png").resize((30,30))
foto_editar = Image.open(r"icones\alterar.png").resize((30,30))
foto_sair = Image.open(r"icones\sair.png").resize((30,30))

# convertendo as imagens redimensionadas dos botões para o formato compatível com o tkinter
foto_salvar = ImageTk.PhotoImage(foto_salvar)
foto_consultar = ImageTk.PhotoImage(foto_consultar)
foto_deletar = ImageTk.PhotoImage(foto_deletar)
foto_editar = ImageTk.PhotoImage(foto_editar)
foto_sair = ImageTk.PhotoImage(foto_sair)

# botões do crud 
btn_salvar = Button(tela, text="Salvar", image=foto_salvar, compound=TOP)
btn_salvar.config(command=salvar)
btn_salvar.place(x=130, y=310)

btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP)
btn_consultar.config(command=consultar)
btn_salvar.place(x=200, y=310)

btn_deletar = Button(tela, text="Deletar", image=foto_deletar, compound=TOP)
btn_deletar.config(command=deletar)
btn_salvar.place(x=270, y=310)

btn_editar = Button(tela, text="Editar", image=foto_editar, compound=TOP)
btn_editar.config(command=atualizar)
btn_salvar.place(x=340, y=310)

btn_sair = Button(tela, text="Sair", image=foto_sair, compound=RIGHT, command=tela.quit)
btn_sair.place(x=620, y=310)


tela.mainloop()

