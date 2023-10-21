from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from db.create_table import create_table
from model.get_all_todos import get_all_todos
from model.get_todos_by_status import get_todos_by_status
from model.get_todo_by_id import get_todo_by_id
from model.add_new_todo import add_new_todo
from model.delete_todo import delete_todo
from model.update_todo import update_todo_db


app = Flask(__name__)
CORS(app)
db_name = 'todos'
table_name = 'todo'


@app.route('/', methods=["GET", "DELETE"])
def home():
    response = None
    if request.method == 'GET':
        response = get_all_todos(db_name, table_name)
        return jsonify(response)
          
    if request.method == "DELETE":
        response = request.get_json()
        delete_todo(db_name, table_name, response['todo_id'])
        return jsonify(response)


@app.route('/add_todo', methods=['POST'])
def add_todo():
    new_todo = request.get_json(force=True)
    add_new_todo(db_name, table_name, new_todo)
    return jsonify(new_todo)


@app.route('/update_todo', methods=['PUT'])
def update_todo():
    todo_to_update = request.get_json(force=True)
    todo_id = todo_to_update['todo_id']
    print(todo_to_update)
    update_todo_db(db_name, table_name, todo_to_update, todo_id)
    return jsonify(todo_to_update)


@app.route('/status/<status>', endpoint='get_by_status')
def get_by_status(status):
    response = get_todos_by_status(db_name, table_name, status)
    return jsonify(response)


@app.route('/id/<todo_id>', endpoint='get_by_id')
def get_by_id(todo_id):
    response = get_todo_by_id(db_name, table_name, todo_id)
    return jsonify(response)


if __name__ == '__main__':
    # create_table()
    app.run(debug=True, use_reloader=False)
