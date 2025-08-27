from tkinter import * 

tela = Tk()
tela.title("Soma")
tela.configure(background="grey")
tela.geometry("600x600")
tela.resizable(True, True)
tela.maxsize(width=400, height=400)
tela.minsize(width=800, height=800)

# título dentro da janela 
lbl_titulo = Label(tela, text="Cálculo de soma", font="Arial 20 bold italic", fg="black", bg="grey")
lbl_titulo.pack()

lbl_num1 = Label(tela, text="Digite o primeiro número:", font="Arial 12 bold", fg="black", bg="grey").place(x=10, y=50)
lbl_num2 = Label(tela, text="Digite o segundo número:", font="Arial 12 bold", fg="black", bg="grey").place(x=10, y=100)
lbl_resultado = Label(tela, text="Resultado:", font="Arial 12 bold", fg="black", bg="grey").place(x=10, y=200)

txt_num1 = Entry(tela, width=20, bg="white")
txt_num1.place(x=220, y=55)
txt_num1.insert(0, "Número")

txt_num2 = Entry(tela, width=20, bg="white")
txt_num2.place(x=220, y=105)
txt_num2.insert(0, "Número")



def soma():
    soma = int(txt_num1.get()) + int(txt_num2.get())
    
    txt_resultado = Entry(tela, width=20, bg="white")
    txt_resultado.place(x=130, y=200)
    txt_resultado.delete(0, 'end')  # limpa o campo
    txt_resultado.insert(0, str(soma))  # insere o novo valor
    
btn_somar = Button(tela, text="Somar", fg="black", bg="white", command=soma)
btn_somar.place(x=130, y=230)

tela.mainloop()