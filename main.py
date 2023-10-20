from flask import Flask, render_template
from db.create_table import create_table
from model.get_all_todos import get_all_todos
from db.utils import map_tuple_to_dict


app = Flask(__name__)
db_name = 'todos'
table_name = 'todo'

@app.route('/')
def home():
    print('home')
    todos = get_all_todos(db_name, table_name)
    print(map_tuple_to_dict(todos))
    return render_template('index.html')


if __name__ == '__main__':
    # create_table()
    app.run(debug=True, use_reloader=False)
