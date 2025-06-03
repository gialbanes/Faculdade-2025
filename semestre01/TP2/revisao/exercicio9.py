from tkinter import * 
import pymongo

tela = Tk()

tela.title("Média do aluno")
tela.geometry("700x500")

conexao = pymongo.MongoClient("mongodb://127.0.0.1:27017/") # conexão com o mongo
banco = conexao["revisao"] # criando o banco de dados chamado revisao
conexao = banco["alunos"] # criando a celeção alunos dentro do banco de dados revisão 

# Labels
lbl_nome = Label(tela, text="Nome:", font="Arial 12")
lbl_nome.place(x=20, y=20)

lbl_idade = Label(tela, text="Idade:", font="Arial 12")
lbl_idade.place(x=20, y=60)

lbl_nota1 = Label(tela, text="Nota 1:", font="Arial 12")
lbl_nota1.place(x=20, y=100)

lbl_nota2 = Label(tela, text="Nota 2:", font="Arial 12")
lbl_nota2.place(x=20, y=140)

lbl_nota3 = Label(tela, text="Nota 3:", font="Arial 12")
lbl_nota3.place(x=20, y=180)

lbl_nota4 = Label(tela, text="Nota 4:", font="Arial 12")
lbl_nota4.place(x=20, y=220)

lbl_nota5 = Label(tela, text="Nota 5:", font="Arial 12")
lbl_nota5.place(x=20, y=260)

# Entradas
txt_nome = Entry(tela, width=30, borderwidth=2)
txt_nome.place(x=90, y=20)

txt_idade = Entry(tela, width=30, borderwidth=2)
txt_idade.place(x=90, y=60)

txt_nota1 = Entry(tela, width=30, borderwidth=2)
txt_nota1.place(x=90, y=100)

txt_nota2 = Entry(tela, width=30, borderwidth=2)
txt_nota2.place(x=90, y=140)

txt_nota3 = Entry(tela, width=30, borderwidth=2)
txt_nota3.place(x=90, y=180)

txt_nota4 = Entry(tela, width=30, borderwidth=2)
txt_nota4.place(x=90, y=220)

txt_nota5 = Entry(tela, width=30, borderwidth=2)
txt_nota5.place(x=90, y=260)

lbl_resultado = Label(tela, text="")
lbl_resultado.place(x=300, y=370)


def media():
    global media
    media = (int(txt_nota1.get()) + int(txt_nota2.get()) + int(txt_nota3.get()) + int(txt_nota4.get()) + int(txt_nota5.get())) / 5
    if media >= 5:
        resultado = f"Aluno {txt_nome.get()} tem {txt_idade.get()} e foi aprovado com média de {media:.2f}"
    else:
        resultado = f"Aluno {txt_nome.get()} tem {txt_idade.get()} e foi reprovado com média de {media:.2f}"

    lbl_resultado.config(text=resultado)



btn_media = Button(tela, text="Calcular média", command=media)
btn_media.place(x=250, y=330)

def salvar():
    global media 
    aluno = {"nome": txt_nome.get(), "idade": txt_idade.get(), "media": media}
    conexao.insert_one(aluno)


btn_salvar = Button(tela, text="Salvar", command=salvar)
btn_salvar.place(x=280, y=450)

tela.mainloop()
