## models.py
from banco import bd


class Post:
    def __init__(self, titulo, autor, texto):
        self.titulo = titulo
        self.autor = autor
        self.texto = texto

    def gravar(self):
        sql = '''insert into posts (titulo, autor, texto) values (?, ?, ?)'''
        primeiro_interrogacao = self.titulo
        segundo_interrogacao = self.autor
        terceiro_interrogacao = self.texto
        bd().execute(sql, [primeiro_interrogacao, segundo_interrogacao, terceiro_interrogacao])
        bd().commit()

    @staticmethod
    def recupera_todos():
        ## Usamos o objeto retornado por bd() para realizar comandos sql
        sql = '''select titulo, autor, texto from posts order by id desc'''
        cur = bd().execute(sql)
        ## Montamos dicionário dicionários com os resultados da consulta para passar para a view
        posts = []
        for titulo, autor, texto in cur.fetchall(): # fetchall() gera uma lista com os resultados:
            post = Post(titulo, autor, texto)
            posts.append(post)
        
        return posts


class Presenca:
    def __init__(self, email, presente, resposta, comentarios):
        self.email = email
        self.presente = presente
        self.resposta = resposta
        self.comentarios = comentarios

    def gravar_presenca(self):
        sql = '''insert into presenca (email, presente, resposta, comentarios) values (?, ?, ?, ?)'''
        first_email = self.email
        second_presente = self.presente
        third_resposta = self.resposta
        fourth_comentarios = self.comentarios
        bd().execute(sql, [first_email, second_presente, third_resposta, fourth_comentarios])
        bd().commit()

    @staticmethod
    def recupera_presentes():
        ## Usamos o objeto retornado por bd() para realizar comandos sql
        sql = '''select email, presente, resposta, comentarios from presenca order by id desc'''
        cur = bd().execute(sql)
        ## Montamos dicionário dicionários com os resultados da consulta para passar para a view
        presencas = []
        for email, presente, resposta, comentarios in cur.fetchall(): # fetchall() gera uma lista com os resultados:
            presenca = Presenca(email, presente, resposta, comentarios)
            presencas.append(presenca)
        
        return presencas
