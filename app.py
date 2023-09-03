from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados iniciais (em memória, sem banco de dados)
alunos = []

@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    novo_aluno = request.json
    alunos.append(novo_aluno)
    return jsonify({"message": "Aluno criado com sucesso!"}), 201

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualizar_aluno(id_aluno):
    aluno_atualizado = request.json
    if id_aluno >= len(alunos) or id_aluno < 0:
        return jsonify({"message": "Aluno não encontrado"}), 404
    alunos[id_aluno] = aluno_atualizado
    return jsonify({"message": "Aluno atualizado com sucesso!"})

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deletar_aluno(id_aluno):
    if id_aluno >= len(alunos) or id_aluno < 0:
        return jsonify({"message": "Aluno não encontrado"}), 404
    del alunos[id_aluno]
    return jsonify({"message": "Aluno deletado com sucesso!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)