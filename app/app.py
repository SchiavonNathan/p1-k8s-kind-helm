from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Olá, mundo! 👋</h1><h3>Estou rodando com Helm no Kubernetes!</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
