# importações
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
tela = Tk()

# titulo da tela
tela.title("Cadastro de Pessoas")
# cor da tela
tela.configure(background='grey')
# tamanho da tela
tela.geometry("800x600")

# CRIAÇÃO DO BANCO E TABELA
# criar database
conn = sqlite3.connect("tp.db")
#criar o cursor 
cur = conn.cursor()
# criar a tabela 
cur.execute("CREATE TABLE IF NOT EXISTS pessoas(codigo INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, altura REAL, peso REAL, sexo TEXT, cidade TEXT, dataNasc TEXT, dataCadastro TEXT, dataAtualizacao TEXT, descricao TEXT)")
conn.commit()
#fechar conexão
conn.close()

# FUNÇÃO DE SALVAR DADOS NO BANCO 
def salvar():
    # conecta ao banco
    conn = sqlite3.connect("tp.db")
    cur = conn.cursor()
    # insere os dados na tabela
    cur.execute("INSERT INTO pessoas VALUES(:codigo, :nome, :idade, :altura, :peso, :sexo, :cidade, :dataNasc, :dataCadastro, :dataAtualizacao, :descricao)", {'codigo': int(txt_codigo.get()), 'nome': txt_nome.get(), 'idade': txt_idade.get(), 'altura': txt_altura.get(), 'peso': txt_peso.get(), 'sexo': var.get(), 'cidade': combo.get(), 'dataNasc': txt_dataNasc.get(), 'dataCadastro': txt_dataCadastro.get(), 'dataAtualizacao': txt_dataAtualizacao.get(), 'descricao': txt_desc.get()})

    # commita a inserção 
    conn.commit()
    #fecha a conexão 
    conn.close()

    # LIMPA TEXTBOX
    txt_nome.delete(0, END)
    txt_idade.delete(0, END)
    txt_altura.delete(0, END)
    txt_peso.delete(0, END)
    #var.delete(0, END)
    combo.delete(0, END)
    txt_dataNasc.delete(0, END)
    txt_dataCadastro.delete(0, END)
    txt_dataAtualizacao.delete(0, END)
    txt_desc.delete(0, END)

# FUNÇÃO DE CONSULTAR O BANCO 
def consulta():
    # conecta ao banco 
    conn = sqlite3.connect("tp.db")
    # cria o cursor 
    cur = conn.cursor()
    # consulta os dados na tabela pessoas
    cur.execute('SELECT *, codigo FROM pessoas')
    #  recupera todas as linhas resultantes da consulta executada anteriormente; é uma lista de tuplas, onde cada tupla representa uma linha do bd 
    records = cur.fetchall()
    # mostra os resultados encontrados
    print_records = ""
    for rec in records:
        print_records += 'Codigo:' + str(rec[0]) + ' -- Nome:' + str(rec[1]) + ' -- Idade:' + str(rec[2]) + ' -- Altura:' + str(rec[3]) + ' -- Peso:' + str(rec[4]) + ' -- Sexo:' + str(rec[5]) + ' -- Cidade:' + str(rec[6]) + ' -- Data de nascimento:' + str(rec[7]) + ' -- Data de cadastro:' + str(rec[8]) + ' -- Data de atualização:' + str(rec[9]) + ' -- Descrição:' + str(rec[10]) + '\n\n'

    # criando e posicionando a label para mostrar os resultados 
    Label(tela, text=print_records).place(x=50, y=450)
    # commitando as mudanças 
    conn.commit()
    # fechando a conexão
    conn.close()

# FUNÇÃO DE DELETAR DADOS DO BANCO 
def deletar():
    # conecta ao banco 
    conn = sqlite3.connect("tp.db")
    # cria o cursor 
    cur = conn.cursor()
    # deleta o registro 
    cur.execute('DELETE FROM pessoas WHERE codigo =' + txt_codigo.get())
    # commitando as mudanças 
    conn.commit()
    # fechando a conexão
    conn.close()
    # mostra a mensagem de sucesso da operação de deletar
    messagebox.showinfo("Excluindo...", "Registro excluído com sucesso!")

# FUNÇÃO DE ALTERAÇÃO 
def alterar():
    # conecta ao banco 
    conn = sqlite3.connect("tp.db")
    # cria o cursor 
    cur = conn.cursor()
    # altera o registro 
    cur.execute("""UPDATE pessoas SET nome = :nome, idade = :idade, altura = :altura, peso = :peso, sexo = :sexo, cidade = :cidade, dataNasc = :dataNasc, dataCadastro = :dataCadastro, descricao = :descricao WHERE codigo = codigo""", {'nome': txt_nome.get(), 'idade': txt_idade.get(), 'altura': txt_altura.get(), 'peso': txt_peso.get(), 'sexo': var.get(), 'cidade': combo.get(), 'dataNasc': txt_dataNasc.get(), 'dataCadastro': txt_dataCadastro.get(), 'descricao': txt_desc.get(), 'codigo': txt_codigo.get()})

    # commitando as mudanças 
    conn.commit()
    # fechando a conexão
    conn.close()

# definindo checkbox ja assinalada de acordo com seu valor
# definindo que o critério do valor pro checkbox ser assinalado é string e valor "m"
var = StringVar()
var.set("")

# checkbox para sexo
radio_buttonm = Radiobutton(tela,text="M", variable=var, value="m")
radio_buttonm.place(x=170, y=150)
radio_buttonf = Radiobutton(tela, text="F", variable=var, value="f")
radio_buttonf.place(x=220, y=150)

# combobox para cidade
combo = Combobox(tela)
combo['values']=("Iguape", "Ilha Comprida", "Registro", "Juquia", "Miracatu", "Cajati")
combo.current(1)
combo.place(x=550, y=150)

# cadastro de imagem
pasta_inicial = ""
def escolher_img():
    # localização e tipos dos arquivos a serem utilizados
    caminho_img = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem", filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),("Todos os arquivos", "*.*")))
    # abertura do arquivo através do PIL
    img_pil = Image.open(caminho_img)
    largura, altura = img_pil.size
    if largura > 150:
        proporcao = largura/ 150
        nova_altura = int(altura/proporcao)
        #redimensionamento 
        img_pil = img_pil.resize((110, nova_altura))
    # covertendo a imagm para o formato compatível ao tkinter
    img_tk = ImageTk.PhotoImage(img_pil)
    # a imagem escolhida será armazenada em uma label
    lbl_img = Label(tela, image=img_tk)
    lbl_img.image = img_tk
    lbl_img.place(x=10, y=50)

# botão chamando a função escolher_imagem, onde vou escolher a imagem de fato
btn_escolher = Button(tela, text="Escolher imagem", command=escolher_img)
btn_escolher.place(x=10, y=140)

# Fotos dos botões com resize para 30x30 pra não ficar desproporcional 
foto_salvar = Image.open(r"icones\salvar.png").resize((30, 30))
foto_editar = Image.open(r"icones\alterar.png").resize((30, 30))
foto_deletar = Image.open(r"icones\excluir.png").resize((30, 30))
foto_consultar = Image.open(r"icones\consultar.png").resize((30, 30))
foto_sair = Image.open(r"icones\sair.png").resize((30, 30))

# Convertendo as imagens redimensionadas para o formato compatível com o tkinter
foto_salvar = ImageTk.PhotoImage(foto_salvar)
foto_editar = ImageTk.PhotoImage(foto_editar)
foto_deletar = ImageTk.PhotoImage(foto_deletar)
foto_consultar = ImageTk.PhotoImage(foto_consultar)
foto_sair = ImageTk.PhotoImage(foto_sair)

# Botões inferiores
# compound: aonde o texto deve aparecer com a imagem 
btn_salvar = Button(tela, text="Salvar", image=foto_salvar, compound=TOP)
btn_salvar.place(x=130, y=310)
btn_salvar.config(command=salvar)

btn_editar = Button(tela, text="Editar", image=foto_editar, compound=TOP)
btn_editar.place(x=200, y=310)
btn_editar.config(command=alterar)

btn_deletar = Button(tela, text="Deletar", image=foto_deletar, compound=TOP)
btn_deletar.place(x=270, y=310)
btn_deletar.config(command=deletar)

btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP)
btn_consultar.place(x=340, y=310)
btn_consultar.config(command=consulta)

btn_sair = Button(tela, text="Sair", image=foto_sair, compound=RIGHT, command=tela.quit)
btn_sair.place(x=620, y=310)

# Labels
# labels da esquerda
lbl_codigo = Label(tela, text="Código:", font=("Arial", 8), foreground="black")
lbl_codigo.place(x=130, y=50)
lbl_nome = Label(tela, text="Nome:", font=("Arial", 8), foreground="black")
lbl_nome.place(x=130, y=100)
lbl_sexo = Label(tela, text="Sexo:", font=("Arial", 8), foreground="black")
lbl_sexo.place(x=130, y=150)
lbl_dataNasc = Label(tela, text="Data Nascimento:", font=("Arial", 8), foreground="black")
lbl_dataNasc.place(x=130, y=200)
lbl_dataAtualizacao = Label(tela, text="Data Atualização:", font=("Arial", 8), foreground="black")
lbl_dataAtualizacao.place(x=130, y=250)
lbl_desc = Label(tela, text="Descrição:", font=("Arial", 8), foreground="black")
lbl_desc.place(x=130, y=280)
# labels da direita
lbl_idade = Label(tela, text="Idade:", font=("Arial", 8), foreground="black")
lbl_idade.place(x=500, y=100)
lbl_altura = Label(tela, text="Altura:", font=("Arial", 8), foreground="black")
lbl_altura.place(x=270, y=150)
lbl_peso = Label(tela, text="Peso:", font=("Arial", 8), foreground="black")
lbl_peso.place(x=370, y=150)
lbl_cidade = Label(tela, text="Cidade:", font=("Arial", 8), foreground="black")
lbl_cidade.place(x=500, y=150)
lbl_dataCadastro = Label(tela, text="Data Cadastro:", font=("Arial", 8), foreground="black")
lbl_dataCadastro.place(x=320, y=200)

# campos de digitação
txt_codigo = Entry(tela, width=10, background="white")
txt_codigo.place(x=200, y=50)
txt_nome = Entry(tela, width=40, background="white")
txt_nome.place(x=200, y=100)
txt_idade = Entry(tela, width=10, background="white")
txt_idade.place(x=550, y=100)
txt_altura = Entry(tela, width=10, background="white")
txt_altura.place(x=300, y=150)
txt_peso = Entry(tela, width=10, background="white")
txt_peso.place(x=415, y=150)
txt_dataNasc = Entry(tela, width=10, background="white")
txt_dataNasc.place(x=220, y=200)
txt_dataCadastro = Entry(tela, width=10, background="white")
txt_dataCadastro.place(x=420, y=200)
txt_dataAtualizacao = Entry(tela, width=10, background="white")
txt_dataAtualizacao.place(x=220, y=250)
txt_desc = Entry(tela, width=50, background="white")
txt_desc.place(x=200, y=280)

#retorno do cadastro
lbl_retorno = Label(tela, text="", font=("Arial", 8), background="white")
lbl_retorno.place(x=50, y=420)

tela.mainloop()