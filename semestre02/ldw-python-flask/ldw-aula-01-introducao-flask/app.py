# do pacote importo o Flask 
# render_template renderiza páginas HTML 
from flask import Flask, render_template

# Criando uma instância do Flask 
app = Flask(__name__, template_folder='views') # esse parâmetro representa o nome da aplicação


# definindo a rota principal da aplicação '/'
@app.route('/')
# toda rota precisa de um função para executar 
def home():
    return render_template('index.html')



# definindo a rota principal da aplicação '/'
@app.route('/games')
# toda rota precisa de um função para executar 
def games():
    # essas variáveis estariam vindo de fora 
    title = 'Tarisland'
    year = 2022
    category = 'MMORPG'
    # lista 
    players = ['Giovana', 'Amanda', 'Igor', 'Diegox']
    # dicionário 
    console = {'Nome' : 'PS5', 'Fabricante': 'Sony', 'Ano': 2020}
    # o primeiro title é a var que vai ser criada na página 
    return render_template('games.html', title=title, year=year, category=category, players=players, console=console)


# se for executado diretamente peloo interpretador 
# camada de segurança; se eu importar o app em outro arquivo, não vai rodar o servidor;
if __name__ == '__main__':
    # iniciando o servidor
    app.run(host="localhost", port=5000, debug=True) 

 
