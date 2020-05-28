# controllers.py

from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Post
from models import Presenca


@app.route('/')
def index():
    # mensagens = Mensagem.recupera_todas()
    posts = Post.recupera_todos()
    presencas = Presenca.recupera_presentes()

    ## Insere opções no menu
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': True, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': False,
                'href': '/gleitho',
                'texto': 'Sobre - Gleitho'})
    menu.append({'active': False,
                'href': '/Thiago',
                'texto': 'Sobre - Thiago'})
    menu.append({'active': False,
                'href': '/Ludvin',
                'texto': 'Sobre - Ludvin'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})

    ## Inserimos tudo que foi criado no dicionário context, ele será passado para a view
    context = {'titulo': 'Página principal',
            'menu': menu,
            'posts': posts,
            'presencas': presencas            
            }

    return render_template('index.html', **context)


@app.route('/post')
def post():
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': True,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': False,
                'href': '/gleitho',
                'texto': 'Sobre - Gleitho'})
    menu.append({'active': False,
                'href': '/Thiago',
                'texto': 'Sobre - Thiago'})
    menu.append({'active': False,
                'href': '/Ludvin',
                'texto': 'Sobre - Ludvin'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})

    context = {'titulo': 'Escrever post',
            'menu': menu}

    return render_template('post.html', **context)


@app.route('/gleitho')
def gleitho():
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': True,
                'href': '/gleitho',
                'texto': 'Sobre - Gleitho'})
    menu.append({'active': False,
                'href': '/Thiago',
                'texto': 'Sobre - Thiago'})
    menu.append({'active': False,
                'href': '/Ludvin',
                'texto': 'Sobre - Ludvin'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})

    context = {'titulo': 'Sobre - Gleitho',
            'menu': menu}

    return render_template('gleitho.html', **context)

@app.route('/Thiago')
def thiago():
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': False,
                'href': '/gleitho',
                'texto': 'Sobre - Gleitho'})
    menu.append({'active': True,
                'href': '/Thiago',
                'texto': 'Sobre - Thiago'})
    menu.append({'active': False,
                'href': '/Ludvin',
                'texto': 'Sobre - Ludvin'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})

    context = {'titulo': 'Sobre - Thiago',
            'menu': menu}

    return render_template('Thiago.html', **context)

@app.route('/Ludvin')
def ludvin():
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': False,
                'href': '/gleitho',
                'texto': 'Sobre - Gleitho'})
    menu.append({'active': False,
                'href': '/Thiago',
                'texto': 'Sobre - Thiago'})
    menu.append({'active': True,
                'href': '/Ludvin',
                'texto': 'Sobre - Ludvin'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})

    context = {'titulo': 'Sobre - Ludvin',
            'menu': menu}

    return render_template('ludvin.html', **context)

@app.route('/presenca')
def presenca():
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': False,
                'href': '/gleitho',
                'texto': 'Sobre - Gleitho'})
    menu.append({'active': False,
                'href': '/Thiago',
                'texto': 'Sobre - Thiago'})
    menu.append({'active': False,
                'href': '/Ludvin',
                'texto': 'Sobre - Ludvin'})
    menu.append({'active': True,
                'href': '/presenca',
                'texto': 'Presença'})

    context = {'titulo': 'Presença',
            'menu': menu}

    return render_template('presenca.html', **context)


@app.route('/post/gravar', methods=['POST'])
def gravar_post():
    titulo = request.form['titulo']
    autor = request.form['autor']
    texto = request.form['texto']
    post = Post(titulo, autor, texto)
    post.gravar()
    return redirect('/')


@app.route('/presenca/gravar_presenca', methods=['POST'])
def gravar():
    email = request.form['email']
    presente = request.form['presente']
    resposta = request.form['resposta']
    comentarios = request.form['comentarios']
    pst = Presenca(email, presente, resposta, comentarios)
    pst.gravar_presenca()
    return redirect('/')


app.run()
