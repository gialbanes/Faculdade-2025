from tkinter import * 
tela = Tk()

tela.geometry("700x500")
tela.title("Cadastro de clientes")
tela.configure(background='#133743')
tela.resizable(True, True) # para poder redimensionar a tela
tela.maxsize(width=760, height=680) # para definir o tamanho máximo da tela
tela.minsize(width=300, height=200)

# colocando caixa de texto 
lbl_titulo = Label(tela, text="Cadastro de clientes", font="Arial 20 bold italic", bg="#1e3743", fg="#BCD1AD").pack()
lbl_titulo.pack()

lbl_nome = Label(tela, text="Nome: ", font="Arial 12 bold italic", bg="#1e3743", fg="#f0ffff").place(x=10, y=45)
txt_nome = Entry(tela, width=60, borderWitdh=5, fg="blue").place(x=165, y=45)
txt_nome.insert(0, "Digite seu nome")

lbl_email = Label(tela, text="E-mail: ", font="Arial 12 bold italic").place(x=10, y=40)
txt_email = Entry(tela, width=60, borderWitdh=5, fg="blue").place(x=165, y=45)
txt_email.insert(0, "Digite seu e-mail")

lbl_tel = Label(tela, text="Telefone: ", font="Arial 12 bold italic").place(x=10, y=70)
txt_tel = Entry(tela, width=60, borderWitdh=5, fg="blue").place(x=165, y=45)
txt_tel.insert(0, "Digite seu telefone")

lbl_endereco = Label(tela, text="Endereço: ", font="Arial 12 bold italic").place(x=10, y=100)
txt_endereco = Entry(tela, width=60, borderWitdh=5, fg="blue").place(x=165, y=45)
txt_endereco.insert(0, "Digite seu endereço")

# colocando botão 
btn_botao = Button(tela, text="Clicar")
btn_botao.pack()

# função pra tirar o placeholder 
def verificaFocusCaixa(event):
    txt_nome.delete(0, END)

txt_nome.bind("<FocusIn>", verificaFocusCaixa)


tela.mainloop()