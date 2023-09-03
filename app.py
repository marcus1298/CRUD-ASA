from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bem-vindo ao sistema de cadastro de assslunos!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)