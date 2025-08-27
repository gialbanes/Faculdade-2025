from tkinter import * 
tela = Tk()

txt_nome = Entry(tela, width=50)
txt_nome.pack() # função para ser exibido dentro do componente pai, no caso, a tela 
txt_nome.insert(0, "Digite seu nome: ")

def clicar():
    lbl_nome = Label(tela, text="Bem-vindo, " + txt_nome.get()) # get pega o valor digitado na caixa de texto 
    lbl_nome.pack()

btn_botao = Button(tela, text="Clique", command=clicar) # command é o evento para chamar a função
btn_botao.pack()

tela.mainloop()