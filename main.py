from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# from https://www.youtube.com/watch?v=yKHJsLUENl0&list=PLHocQMwDsV-jp3z7T4ousLoTpaM_3uGBs&index=23&t=96s&ab_channel=PatrickLoeber
# 31:01 Delete

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    

@app.route('/')
def index():
    # show all todos
    todo_list = ToDo.query.all()
    return render_template('base.html', todo_list = todo_list)

@app.route('/add', methods=['POST'])
def add():
    # add new item
    title = request.form.get('title')
    new_todo = ToDo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)