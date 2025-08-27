# importações
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

tela = Tk()

# titulo da tela
tela.title("Cadastro de Animais")
# cor da tela
tela.configure(background='grey')
# tamanho da tela
tela.geometry("800x600")

# CRIAÇÃO DO BANCO E TABELA
conn = sqlite3.connect("animais.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS animais(
    codigo INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    peso REAL,
    sexo TEXT,
    especie TEXT,
    raca TEXT,
    dataNasc TEXT,
    dataCadastro TEXT,
    dataAtualizacao TEXT,
    descricao TEXT
)""")
conn.commit()
conn.close()

# FUNÇÃO DE SALVAR DADOS NO BANCO 
def salvar():
    conn = sqlite3.connect("animais.db")
    cur = conn.cursor()
    cur.execute("""INSERT INTO animais 
    VALUES(:codigo, :nome, :idade, :peso, :sexo, :especie, :raca, :dataNasc, :dataCadastro, :dataAtualizacao, :descricao)""",
    {
        'codigo': int(txt_codigo.get()),
        'nome': txt_nome.get(),
        'idade': txt_idade.get(),
        'peso': txt_peso.get(),
        'sexo': var.get(),
        'especie': combo_especie.get(),
        'raca': txt_raca.get(),
        'dataNasc': txt_dataNasc.get(),
        'dataCadastro': txt_dataCadastro.get(),
        'dataAtualizacao': txt_dataAtualizacao.get(),
        'descricao': txt_desc.get()
    })
    conn.commit()
    conn.close()

    # Limpa os campos
    txt_codigo.delete(0, END)
    txt_nome.delete(0, END)
    txt_idade.delete(0, END)
    txt_peso.delete(0, END)
    combo_especie.set('')
    txt_raca.delete(0, END)
    txt_dataNasc.delete(0, END)
    txt_dataCadastro.delete(0, END)
    txt_dataAtualizacao.delete(0, END)
    txt_desc.delete(0, END)

def consulta():
    conn = sqlite3.connect("animais.db")
    cur = conn.cursor()
    cur.execute('SELECT *, codigo FROM animais')
    records = cur.fetchall()
    print_records = ""
    for rec in records:
        print_records += f'Codigo: {rec[0]} -- Nome: {rec[1]} -- Idade: {rec[2]} -- Peso: {rec[3]} -- Sexo: {rec[4]} -- Espécie: {rec[5]} -- Raça: {rec[6]} -- Data Nascimento: {rec[7]} -- Cadastro: {rec[8]} -- Atualização: {rec[9]} -- Descrição: {rec[10]}\n\n'

    lbl_consulta = Label(tela, text=print_records, background='grey', justify=LEFT)
    lbl_consulta.place(x=20, y=400)
    conn.commit()
    conn.close()

def deletar():
    conn = sqlite3.connect("animais.db")
    cur = conn.cursor()
    cur.execute('DELETE FROM animais WHERE codigo =' + txt_codigo.get())
    conn.commit()
    conn.close()
    messagebox.showinfo("Excluindo...", "Registro excluído com sucesso!")

def alterar():
    conn = sqlite3.connect("animais.db")
    cur = conn.cursor()
    cur.execute("""
    UPDATE animais SET 
    nome = :nome,
    idade = :idade,
    peso = :peso,
    sexo = :sexo,
    especie = :especie,
    raca = :raca,
    dataNasc = :dataNasc,
    dataCadastro = :dataCadastro,
    dataAtualizacao = :dataAtualizacao,
    descricao = :descricao 
    WHERE codigo = :codigo
    """, {
        'nome': txt_nome.get(),
        'idade': txt_idade.get(),
        'peso': txt_peso.get(),
        'sexo': var.get(),
        'especie': combo_especie.get(),
        'raca': txt_raca.get(),
        'dataNasc': txt_dataNasc.get(),
        'dataCadastro': txt_dataCadastro.get(),
        'dataAtualizacao': txt_dataAtualizacao.get(),
        'descricao': txt_desc.get(),
        'codigo': txt_codigo.get()
    })
    conn.commit()
    conn.close()

# Variável para o sexo
var = StringVar()
var.set("")

# Cadastro de imagem
pasta_inicial = ""
def escolher_img():
    caminho_img = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem", filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),("Todos os arquivos", "*.*")))
    img_pil = Image.open(caminho_img)
    largura, altura = img_pil.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura / proporcao)
        img_pil = img_pil.resize((110, nova_altura))
    img_tk = ImageTk.PhotoImage(img_pil)
    lbl_img = Label(tela, image=img_tk)
    lbl_img.image = img_tk
    lbl_img.place(x=30, y=70)

btn_escolher = Button(tela, text="Escolher imagem", command=escolher_img)
btn_escolher.place(x=30, y=30)

# Labels e Entrys alinhados
largura_label = 120
largura_entry = 180

# Coluna esquerda
lbl_codigo = Label(tela, text="Código:", background='grey')
lbl_codigo.place(x=180, y=30)
txt_codigo = Entry(tela, width=20)
txt_codigo.place(x=300, y=30)

lbl_nome = Label(tela, text="Nome:", background='grey')
lbl_nome.place(x=180, y=70)
txt_nome = Entry(tela, width=20)
txt_nome.place(x=300, y=70)

lbl_sexo = Label(tela, text="Sexo:", background='grey')
lbl_sexo.place(x=180, y=110)
radio_buttonm = Radiobutton(tela,text="Macho", variable=var, value="Macho")
radio_buttonm.place(x=300, y=110)
radio_buttonf = Radiobutton(tela, text="Fêmea", variable=var, value="Fêmea")
radio_buttonf.place(x=370, y=110)

lbl_dataNasc = Label(tela, text="Data Nasc:", background='grey')
lbl_dataNasc.place(x=180, y=150)
txt_dataNasc = Entry(tela, width=20)
txt_dataNasc.place(x=300, y=150)

lbl_dataCadastro = Label(tela, text="Cadastro:", background='grey')
lbl_dataCadastro.place(x=180, y=190)
txt_dataCadastro = Entry(tela, width=20)
txt_dataCadastro.place(x=300, y=190)

lbl_dataAtualizacao = Label(tela, text="Atualização:", background='grey')
lbl_dataAtualizacao.place(x=180, y=230)
txt_dataAtualizacao = Entry(tela, width=20)
txt_dataAtualizacao.place(x=300, y=230)

# Coluna direita
lbl_idade = Label(tela, text="Idade:", background='grey')
lbl_idade.place(x=480, y=30)
txt_idade = Entry(tela, width=20)
txt_idade.place(x=580, y=30)

lbl_peso = Label(tela, text="Peso (kg):", background='grey')
lbl_peso.place(x=480, y=70)
txt_peso = Entry(tela, width=20)
txt_peso.place(x=580, y=70)

lbl_especie = Label(tela, text="Espécie:", background='grey')
lbl_especie.place(x=480, y=110)
combo_especie = Combobox(tela, width=18)
combo_especie['values'] = ("Cachorro", "Gato", "Pássaro", "Cavalo", "Outro")
combo_especie.current(0)
combo_especie.place(x=580, y=110)

lbl_raca = Label(tela, text="Raça:", background='grey')
lbl_raca.place(x=480, y=150)
txt_raca = Entry(tela, width=20)
txt_raca.place(x=580, y=150)

lbl_desc = Label(tela, text="Descrição:", background='grey')
lbl_desc.place(x=180, y=270)
txt_desc = Entry(tela, width=60)
txt_desc.place(x=180, y=300)

# Botões
btn_salvar = Button(tela, text="Salvar", command=salvar)
btn_salvar.place(x=180, y=340)
btn_editar = Button(tela, text="Editar", command=alterar)
btn_editar.place(x=260, y=340)
btn_deletar = Button(tela, text="Deletar", command=deletar)
btn_deletar.place(x=340, y=340)
btn_consultar = Button(tela, text="Consultar", command=consulta)
btn_consultar.place(x=420, y=340)
btn_sair = Button(tela, text="Sair", command=tela.quit)
btn_sair.place(x=500, y=340)

tela.mainloop()
