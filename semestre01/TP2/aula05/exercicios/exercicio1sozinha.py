from tkinter import * 

tela = Tk()
tela.title("Cadastro de clientes")
tela.configure(background="grey")
tela.geometry("600x600")
tela.resizable(True, True)
tela.maxsize(width=400, height=400)
tela.minsize(width=800, height=800)

# título dentro da janela
lbl_titulo = Label(tela, text="CADASTRO DE CLIENTES", font="Arial 20 bold italic", fg="black", bg="grey")
lbl_titulo.pack()

# labels dos dados 
lbl_nome = Label(tela, text="Nome:", font="Arial 12 bold", fg="black", bg="grey").place(x=10, y=50)
lbl_email = Label(tela, text="E-mail:", font="Arial 12 bold", fg="black", bg="grey").place(x=10, y=100)
lbl_telefone = Label(tela, text="Telefone:", font="Arial 12 bold", fg="black", bg="grey").place(x=10, y=150)
lbl_endereco = Label(tela, text="Endereço:", font="Arial 12 bold", fg="black", bg="grey").place(x=10, y=200)

# entry para digitar os dados 
txt_nome = Entry(tela, width=20, bg="white")
txt_nome.place(x=100, y=50)
txt_nome.insert(0, "Nome:")

txt_email = Entry(tela, width=20, bg="white")
txt_email.place(x=100, y=100)
txt_email.insert(0, "Email:")

txt_telefone = Entry(tela, width=20, bg="white")
txt_telefone.place(x=100, y=150)
txt_telefone.insert(0, "Telefone:")

txt_endereco = Entry(tela, width=20, bg="white")
txt_endereco.place(x=100, y=200)
txt_endereco.insert(0, "Endereço:")

# título de exibição dos dados
lbl_subtitulo = Label(tela, text="DADOS DO CLIENTE", font="Arial 20 bold italic", fg="black", bg="grey").place(x=250, y=300)

# função para clicar no botão e mostrar os dados do cliente
def mostrar_dados():
    lbl_nome_resultado = Label(tela, text="Nome:" + txt_nome.get())
    lbl_nome_resultado.place(x=250, y=350)
    
    lbl_email_resultado = Label(tela, text="Email:" + txt_email.get())
    lbl_email_resultado.place(x=250, y=370)
    
    lbl_telefone_resultado = Label(tela, text="Telefone:" + txt_telefone.get())
    lbl_telefone_resultado.place(x=250, y=390)
    
    lbl_endereco_resultado = Label(tela, text="Endereco:" + txt_endereco.get())
    lbl_endereco_resultado.place(x=250, y=410)
    
#botão que vai mostra os dados
btn_mostar = Button(tela, text="Mostre os dados", fg="black", bg="white", command=mostrar_dados).place(x=250, y=450)
tela.mainloop()