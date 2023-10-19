from flask import Flask, render_template
from create_table import create_table


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    create_table()
    app.run(debug=True, use_reloader=False)
