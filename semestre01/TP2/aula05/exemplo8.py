from tkinter import * 

tela = Tk()
tela.title("teste")
tela.configure(background="grey")
tela.geometry("600x600")
tela.resizable(True, True)
tela.maxsize(width=400, height=400)
tela.minsize(width=800, height=800)

# objetivo: criar botão 
# objetivo: add caixa de texto  

txt_nome = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white") # entry define a caixa de texto
txt_nome.pack()
txt_nome.insert(0, "Digite seu nome") # define a entrada de dados na caixa de texto 

btn_botao = Button(tela, text="Clicar")
btn_botao.pack()

tela.mainloop()