from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

tela = Tk()
tela.geometry("700x450")
tela.title("Cadastro de Carros")

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

# Função para exibir os dados cadastrados
def clicar():
    lbl_resultado.config(text=f"Modelo: {txt_modelo.get()}\n"
                              f"Marca: {txt_marca.get()}\n"
                              f"Ano: {txt_ano.get()}\n"
                              f"Cor: {txt_cor.get()}\n"
                              f"Placa: {txt_placa.get()}")


# Campos de entrada
Label(tela, text="Modelo:").place(x=200, y=50)
txt_modelo = Entry(tela, width=30)
txt_modelo.place(x=300, y=50)

Label(tela, text="Marca:").place(x=200, y=80)
txt_marca = Entry(tela, width=30)
txt_marca.place(x=300, y=80)

Label(tela, text="Ano:").place(x=200, y=110)
txt_ano = Entry(tela, width=30)
txt_ano.place(x=300, y=110)

Label(tela, text="Cor:").place(x=200, y=140)
txt_cor = Entry(tela, width=30)
txt_cor.place(x=300, y=140)

Label(tela, text="Placa:").place(x=200, y=170)
txt_placa = Entry(tela, width=30)
txt_placa.place(x=300, y=170)

# Botão de cadastro
btn_cadastrar = Button(tela, text="Cadastrar", font="Arial 12 bold", command=clicar)
btn_cadastrar.place(x=390, y=210)

# Exibição dos dados cadastrados
lbl_resultado = Label(tela, text="", font="Arial 12", bg="white", width=30, height=6, anchor="w", justify="left")
lbl_resultado.place(x=200, y=270)

# Carregamento das imagens (certifique-se de que os arquivos existem)
try:
    foto_salvar = PhotoImage(file="icones/salvar.png")
    foto_excluir = PhotoImage(file="icones/excluir.png")
    foto_alterar = PhotoImage(file="icones/alterar.png")
    foto_consultar = PhotoImage(file="icones/consultar.png")
    foto_sair = PhotoImage(file="icones/sair.png")
    
    btn_salvar = Button(tela, image=foto_salvar, compound=TOP).place(x=210, y=400)
    btn_excluir = Button(tela, image=foto_excluir, compound=TOP).place(x=290, y=400)
    btn_alterar = Button(tela, image=foto_alterar, compound=TOP).place(x=360, y=400)
    btn_consultar = Button(tela, image=foto_consultar, compound=TOP).place(x=430, y=400)
    btn_sair = Button(tela, image=foto_sair, compound=RIGHT).place(x=630, y=320)
except:
    print("Erro ao carregar as imagens dos botões. Verifique os caminhos.")

tela.mainloop()
