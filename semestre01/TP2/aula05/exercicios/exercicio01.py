from tkinter import *

# Inicializa a tela
tela = Tk()

tela.title("Cadastro de Clientes")
tela.configure(background="blue")
tela.geometry("800x600")

# Labels
lbl_titulo = Label(tela, text="CADASTRO DE CLIENTES", font="Arial 18 bold", bg="blue", fg="white")
lbl_titulo.place(x=250, y=10)

lbl_nome = Label(tela, text="Digite o nome: ", font="Arial 12 bold", bg="blue", fg="white")
lbl_nome.place(x=10, y=50)

lbl_email = Label(tela, text="Digite o email: ", font="Arial 12 bold", bg="blue", fg="white")
lbl_email.place(x=10, y=80)

lbl_telefone = Label(tela, text="Digite o telefone: ", font="Arial 12 bold", bg="blue", fg="white")
lbl_telefone.place(x=10, y=110)

lbl_endereco = Label(tela, text="Digite o endereco: ", font="Arial 12 bold", bg="blue", fg="white")
lbl_endereco.place(x=10, y=140)

lbl_dados = Label(tela, text="Dados do Cliente", font="Arial 18 bold", bg="blue", fg="white")
lbl_dados.place(x=250, y=200)

# Text areas (Entry fields)
txt_nome = Entry(tela, width=50, fg="black", bg="white")
txt_nome.place(x=200, y=50)
txt_nome.insert(0, "Nome: ")

txt_email = Entry(tela, width=50, fg="black", bg="white")
txt_email.place(x=200, y=80)
txt_email.insert(0, "Email:")

txt_telefone = Entry(tela, width=50, fg="black", bg="white")
txt_telefone.place(x=200, y=110)
txt_telefone.insert(0, "Telefone: ")

txt_endereco = Entry(tela, width=50, fg="black", bg="white")
txt_endereco.place(x=200, y=140)
txt_endereco.insert(0, "Endereco: ")

# Função de ação do botão
def clicar():
    lbl_nome_resultado = Label(tela, text="Nome: " + txt_nome.get(), font="Arial 12", bg="blue", fg="white")
    lbl_nome_resultado.place(x=250, y=250)

    lbl_email_resultado = Label(tela, text="Email: " + txt_email.get(), font="Arial 12", bg="blue", fg="white")
    lbl_email_resultado.place(x=250, y=280)

    lbl_telefone_resultado = Label(tela, text="Tel: " + txt_telefone.get(), font="Arial 12", bg="blue", fg="white")
    lbl_telefone_resultado.place(x=250, y=310)

    lbl_endereco_resultado = Label(tela, text="End: " + txt_endereco.get(), font="Arial 12", bg="blue", fg="white")
    lbl_endereco_resultado.place(x=250, y=340)

# Função para limpar o texto da caixa ao focar
def verificaFocusCaixa(event):
        if txt_nome.get() == "Nome: ":
            txt_nome.delete(0, END)
        if txt_email.get() == "Email:":
            txt_email.delete(0, END)
        if txt_telefone.get() == "Telefone: ":
            txt_telefone.delete(0, END)
        if txt_endereco.get() == "Endereco: ":
            txt_endereco.delete(0, END)

txt_nome.bind("<FocusIn>", verificaFocusCaixa)
txt_email.bind("<FocusIn>", verificaFocusCaixa)
txt_telefone.bind("<FocusIn>", verificaFocusCaixa)
txt_endereco.bind("<FocusIn>", verificaFocusCaixa)

# Botão
btn_cadastrar = Button(tela, text="Cadastrar Cliente", font="Arial 12 bold", command=clicar)
btn_cadastrar.place(x=250, y=380)

# Inicia o loop principal
tela.mainloop()