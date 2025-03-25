from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

tela = Tk()
tela.geometry("700x400")

pasta_inicial = ""

def escolher_imagem():
    #localização e tipos dos arquivos a serem utilizados
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem", filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"), ("Todos os arquivos", "*.*")))

    # abertura do arquivo através do PIL
    imagem_pil = Image.open(caminho_imagem)
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura/proporcao)
        #redimensionamento 
        imagem_pil = imagem_pil.resize((110, nova_altura))

    # covertendo a imagm para o formato compatível ao tkinter
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = Label(tela, image=imagem_tk)
    lbl_imagem.image = imagem_tk
    # a imagem escolhida será armazenada em uma label
    lbl_imagem.place(x=10, y=50)

# botão chamando a função escolher_imagem, onde vou escolher a imagem de fato
btn_escolher = Button(tela, text="Escolher imagem", command=escolher_imagem)
btn_escolher.place(x=10, y=140)

foto_salvar = PhotoImage(file = r"icones\salvar.png")
foto_excluir = PhotoImage(file = r"icones\excluir.png")
foto_alterar = PhotoImage(file = r"icones\alterar.png")
foto_consultar = PhotoImage(file = r"icones\consultar.png")
foto_sair = PhotoImage(file = r"icones\sair.png")

btn_salvar = Button(tela, text="Salvar", image=foto_salvar, compound=TOP).place(x=130, y=310)
btn_excluir = Button(tela, text="Excluir", image=foto_excluir, compound=TOP).place(x=200, y=310)
btn_alterar = Button(tela, text="Alterar", image=foto_alterar, compound=TOP).place(x=270, y=310)
btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP).place(x=340, y=310)
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=RIGHT).place(x=620, y=340)

tela.mainloop()

