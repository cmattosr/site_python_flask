from flask import Flask, render_template

app = Flask(__name__)

#para criar páginas no flask é necessário um route, uma função e um template
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contato")
def contatos():
    return render_template("contato.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario_html=nome_usuario)

#colocar o site no ar
#o parâmetro debug=True faz com que não seja necessário reiniciar o serviço para verificar alterações no site

if __name__ == "__main__":
    app.run(debug=True)