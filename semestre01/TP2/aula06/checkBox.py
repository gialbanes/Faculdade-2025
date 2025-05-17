from tkinter import * 
tela = Tk()
tela.title("Open file")
tela.geometry("300x300")

def show():
    Label(tela, text=var.get()).pack()

var = StringVar() # variável que vai guardar as opções do checkbox 

chk_button = Checkbutton(tela, text="Check box", variable=var, onvalue="On", offvalue="off")
chk_button.deselect() # já inicia a caixinha desmarcada
chk_button.pack() #.pack() é um método para colocar o elemento na tela 

Button(tela, text="show me", command=show).pack()

tela.mainloop()