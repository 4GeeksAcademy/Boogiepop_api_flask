from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json  
    print("Incoming request with the following body", request_body)
    todos.append(request_body) 
    return jsonify(todos) 

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):  # Verifica que la posición sea válida
        todos.pop(position)  # Elimina la tarea en la posición dada
    return jsonify(todos)  # Devuelve la lista actualizada

if __name__ == '__main__':
    app.run(debug=True, port=3245)