# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/index.html")
def home():

    nome = "Sarah Vitoria" # escreva seu nome
    idade = "17" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai.html")
def pai():

    nome = "Sergio Guerrero" # escreva seu nome
    idade = "55" # escreva sua idade

    return render_template('pai.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
@app.mae("/mae.html")
def home():

    nome = "Rosana Guerrero" # escreva seu nome
    idade = "50" # escreva sua idade

    return render_template('mae.html' , nome = nome , idade = idade)

# defina a rota para a página do amigo
@app.amigo("/amigo.html")
def home():

    nome = "Isabela" # escreva seu nome
    idade = "18" # escreva sua idade

    return render_template('amigo.html' , nome = nome , idade = idade)
# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
