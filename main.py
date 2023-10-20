from flask import Flask, render_template, jsonify, request
from db.create_table import create_table
from model.get_all_todos import get_all_todos
from model.get_todos_by_status import get_todos_by_status
from model.get_todo_by_id import get_todo_by_id
from model.add_new_todo import add_new_todo


app = Flask(__name__)
db_name = 'todos'
table_name = 'todo'

@app.route('/')
def get_todos():
    response = get_all_todos(db_name, table_name)
    return jsonify(response)


@app.route('/status/<status>', endpoint='get_by_status')
def get_by_status(status):
    response = get_todos_by_status(db_name, table_name, status)
    return jsonify(response)


@app.route('/id/<todo_id>', endpoint='get_by_id')
def get_by_status(todo_id):
    response = get_todo_by_id(db_name, table_name, todo_id)
    return jsonify(response)


@app.route('/add_todo', method=['POST'])
def add_todo():
    new_todo = request.get_json()
    add_new_todo(db_name, table_name, new_todo)
    return new_todo







if __name__ == '__main__':
    # create_table()
    app.run(debug=True, use_reloader=False)
