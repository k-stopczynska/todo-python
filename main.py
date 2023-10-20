from flask import Flask, render_template, jsonify
from db.create_table import create_table
from model.get_all_todos import get_all_todos
from model.get_todos_by_status import get_todos_by_status
from db.utils import map_tuple_to_dict


app = Flask(__name__)
db_name = 'todos'
table_name = 'todo'

@app.route('/')
def get_todos():
    response = get_all_todos(db_name, table_name)
    return jsonify(response)

@app.route('/status/<status>')
def get_by_status(status):
    response = get_todos_by_status(db_name, table_name, status)
    return jsonify(response)





if __name__ == '__main__':
    # create_table()
    app.run(debug=True, use_reloader=False)
