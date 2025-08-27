from tkinter import * 

tela = Tk()
tela.title("Fatec Registro")
tela.configure(background="grey")
tela.geometry("800x800")
tela.resizable(True, True)
tela.maxsize(width=900, height=900)
tela.minsize(width=600, height=600)

lbl_teste = Label(tela, text="Teste").place(x=100, y=100)
#lbl_teste é o nome de identificação interno da label
# Label é o tipo do componente 
# tela é a variável que a label está ligada
# text é o texto atribuído na tela
# place é o posicionamento do componente na tela 

tela.mainloop