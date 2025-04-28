from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import pymongo

tela = Tk()
tela.title("Login")
tela.geometry("400x200")
tela.resizable
largura=1000
altura=700

barra_menus = Menu(tela)

# menus
opcoes_menu_arquivos = Menu(barra_menus)
opcoes_menu_gestao = Menu(barra_menus)
opcoes_novo = Menu(opcoes_menu_arquivos)

# menu que possui submenu - cascade
# menu = indica o pai desse submenu que estou criando 
barra_menus.add_cascade(label="Arquivos", menu=opcoes_menu_arquivos)
barra_menus.add_cascade(label="Gestão", menu=opcoes_menu_gestao)
opcoes_menu_arquivos.add_cascade(label="Novo", menu=opcoes_novo) # cascate - submenu no novo menu 

# adicionando os itens do menu Arquivos 
# command - serão comandos únicos, diferente do cascata
opcoes_novo.add_command(label="Cadastrar")
opcoes_menu_arquivos.add_command(label="Abrir")
opcoes_menu_arquivos.add_command(label="Salvar")
opcoes_menu_arquivos.add_command(label="Salvar como...")
opcoes_menu_arquivos.add_separator() # separador
opcoes_menu_arquivos.add_command(label="Sair", command=tela.quit)

# funções de acesso às telas 
# cada função corresponde à um menu, e cada menu abrigará um arquivo externo 
def abrir_tela_clientes():
    subprocess.run(["python", "clientes.py"])

def abrir_tela_animais():
    subprocess.run(["python", "animais.py"])

def logout():
    tela.destroy()
    subprocess.run(["python", "Login.py"])

# adicionando os itens do menu Gestão
opcoes_menu_gestao.add_command(label="Animais", command=abrir_tela_animais)
opcoes_menu_gestao.add_command(label="Clientes", command=abrir_tela_clientes)

# ícones do menu 
foto_sair = PhotoImage(file=r"icones\sair.png")
foto_animais = PhotoImage(file=r"icones\logo_animais.png")
foto_usuarios = PhotoImage(file=r"icones\logo_usuarios.png")
foto_servicos = PhotoImage(file=r"icones\logo_servicos.png")
foto_logout = PhotoImage(file=r"icones\logout.png")

# botões do menu 
lbl_logo = Label(tela, text="PET SHOP DOG'S", compound=TOP, image=foto_sair).place(x=890, y=580)
btn_animais = Button(tela, text="Animais", compound=TOP, command=abrir_tela_animais, image=foto_animais).place(x=100, y=200)
btn_clientes = Button(tela, text="Clientes", compound=TOP, command=abrir_tela_clientes,image=foto_usuarios).place(x=350, y=200)
btn_servicos = Button(tela, text="Serviços", compound=TOP, image=foto_servicos).place(x=550, y=200)
btn_logout = Button(tela, text="Logout", compound=TOP, command=logout,image=foto_logout).place(x=800, y=200)

tela.config(menu=barra_menus)
tela.mainloop()
