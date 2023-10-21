from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from db.create_table import create_table
from model.get_all_todos import get_all_todos
from model.get_todos_by_status import get_todos_by_status
from model.get_todo_by_id import get_todo_by_id
from model.add_new_todo import add_new_todo
from model.delete_todo import delete_todo
from model.update_todo import update_todo


app = Flask(__name__)
CORS(app)
db_name = 'todos'
table_name = 'todo'

# @app.after_request
# def add_security_headers(resp):
#     resp.headers['Content-Security-Policy']='*'
#     resp.headers["Access-Control-Allow-Origin"] = "*"
#     return resp

def get_todos():
    response = get_all_todos(db_name, table_name)
    print(response)
    return jsonify(response)



def update_existing_todo():
    updated_todo = request.get_json()
    todo_id = updated_todo['todo_id']
    update_todo(db_name, table_name, updated_todo, todo_id)
    return updated_todo

def remove_todo():
    todo_id = request.get_json()
    delete_todo(db_name, table_name, todo_id)
    return todo_id

@app.route('/', methods=["GET", "PUT", "DELETE"])
def home():
    response = None
    if request.method == 'GET':
        response = get_all_todos(db_name, table_name)
        print(response)

    if request.method == "PUT":
        response = request.get_json()
        todo_id = response['todo_id']
        update_todo(db_name, table_name, response, todo_id)
          
    if request.method == "DELETE":
        response = request.get_json()
        delete_todo(db_name, table_name, response)
    return jsonify(response)


@app.route('/add_todo', methods=['POST'])
def add_todo():
    new_todo = request.get_json()
    add_new_todo(db_name, table_name, new_todo)
    return new_todo
       
@app.route('/status/<status>', endpoint='get_by_status')
def get_by_status(status):
    response = get_todos_by_status(db_name, table_name, status)
    return jsonify(response)


@app.route('/id/<todo_id>', endpoint='get_by_id')
def get_by_status(todo_id):
    response = get_todo_by_id(db_name, table_name, todo_id)
    return jsonify(response)





if __name__ == '__main__':
    # create_table()
    app.run(debug=True, use_reloader=False)
