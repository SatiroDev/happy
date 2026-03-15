from flask import Flask, render_template, url_for

app = Flask(__name__)

lista_fotos = [
    'img/foto.jpeg',
    'img/foto1.jpeg',
    'img/foto2.jpeg',
    'img/foto3.jpeg',
    'img/foto4.jpeg',
    'img/foto5.jpeg',
    'img/foto6.jpeg',
    'img/foto7.jpeg',
    'img/foto8.jpeg',
    'img/foto9.jpeg'

]

lista_motivos = [
    {
        "id": 1,
        "frase": "Seu sorriso que ilumina até meus dias mais difíceis"
    },
    {
        "id": 2,
        "frase": "Seu jeito de me fazer rir sem esforço"
    },
    {
        "id": 3,
        "frase": "Seu coração enorme"
    },
    {
        "id": 4,
        "frase": "Sua força mesmo quando você acha que não é forte"
    },
    {
        "id": 5,
        "frase": "A paz que sinto quando estou com você"
    },
    {
        "id": 6,
        "frase": "Seu abraço que parece casa"
    },
    {
        "id": 7,
        "frase": "Sua sinceridade"
    },
    {
        "id": 8,
        "frase": "Seu jeito carinhoso comigo"
    },
    {
        "id": 9,
        "frase": "Sua inteligência e dedicação"
    },
    {
        "id": 10,
        "frase": "A forma como você se importa com os detalhes"
    },
    {
        "id": 11,
        "frase": "Seu olhar cheio de verdade"
    },
    {
        "id": 12,
        "frase": "Seu apoio nos meus sonhos"
    },
    {
        "id": 13,
        "frase": "A leveza que você traz para a minha vida"
    },
    {
        "id": 14,
        "frase": "Seu jeito único de demonstrar carinho"
    },
    {
        "id": 15,
        "frase": "A forma como você transforma momentos simples em especiais"
    },
    {
        "id": 16,
        "frase": "Seu jeitinho quando está feliz"
    },
    {
        "id": 17,
        "frase": "Porque ao seu lado tudo faz mais sentido"
    }
]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cards")
def cards():
    return render_template("telas.html",  cards=lista_motivos, fotos=lista_fotos)

if __name__ == "__main__":
    app.run(debug=True)