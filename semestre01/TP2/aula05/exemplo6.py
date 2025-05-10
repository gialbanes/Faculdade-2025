from tkinter import * 

tela = Tk()
tela.title("teste")

# objetivo: carregar a interface no centro da tela do pc 

# dimensões da tela do tkinter
largura = 800
altura = 300

# dimensões da tela do pc 
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

# faz o posicionamento no centro 
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#tamanho da tela no terminal 
print(largura_screen, altura_screen)

#definição do tamanho da tela com geometry
tela.geometry("%dx%d+%d+%d" % (largura, altura_screen, posx, posy))

tela.mainloop()
