from tkinter import *
from tkinter import messagebox
import subprocess
import pymongo

tela = Tk()
tela.title("Login")
tela.geometry("400x200")
tela.resizable
largura = 400
altura = 200

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
db = cliente["exemplo"]
cliente = db['login']

def sair():
    resposta = messagebox.askquestion("Sair do sistema?", "Você tem certeza que deseja sair?")
    if resposta == "yes":
        tela.destroy()

def validar_acesso(usuario, senha):
    resultado = cliente.find_one({"usuario": usuario, "senha": senha})
    if resultado:
        abrir_app()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")

def abrir_app():
    tela.destroy()
    subprocess.run(["python", "menu.py"]) # subprocess: executa um novo processo

def click_botao():
    usuario = txt_usuario.get()
    senha = txt_senha.get()
    validar_acesso(usuario, senha)

lbl_usuario = Label(tela, text="Usuário").place(x=50, y=60)
lbl_senha = Label(tela, text="Senha").place(x=50, y=100)

txt_usuario = Entry(tela, width=20)
txt_usuario.place(x=100, y=60)

txt_senha = Entry(tela, width=20, show="*") 
txt_senha.place(x=100, y=100)

foto_acesso = PhotoImage(file=r"icones\acesso.png")
foto_sair = PhotoImage(file=r"icones\sair.png")

btn_usuario = Button(tela, text="Acessar", image=foto_acesso, compound=TOP, command=click_botao)
btn_usuario.place(x=250, y=50)

btn_sair = Button(tela, text="Sair", image=foto_sair, compound=TOP, command=sair)
btn_sair.place(x=320, y=50)

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2 

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
tela.mainloop()
