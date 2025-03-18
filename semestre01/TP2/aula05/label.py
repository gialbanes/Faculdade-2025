# o nome do arquivo não pode ser o mesmo da biblioteca que estou importando
from tkinter import * 
tela = Tk()

tela.title("Fatec de Registro")
tela.configure(background='#133743')
tela.geometry("700x600")
tela.resizable(True, True) # para poder redimensionar a tela
tela.maxsize(width=760, height=680) # para definir o tamanho máximo da tela
tela.minsize(width=300, height=200)

# o primeiro argumento é em qual ambiente ele vai ser redenrizado
# o método plcace
lbl_nome = Label(tela, text="Nome: ", font="Arial 12 bold italic").place(x=10, y=10)
lbl_telefone = Label(tela, text="Telefone: ", font="Arial 12 bold italic").place(x=10, y=40)
lbl_endereco = Label(tela, text="Endereço: ", font="Arial 12 bold italic").place(x=10, y=70)
lbl_cpf = Label(tela, text="CPF: ", font="Arial 12 bold italic").place(x=10, y=100)
btn_botao = Button(tela, text="Clicar")
btn_botao.pack()

tela.mainloop()