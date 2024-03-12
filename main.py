from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# from https://www.youtube.com/watch?v=yKHJsLUENl0&list=PLHocQMwDsV-jp3z7T4ousLoTpaM_3uGBs&index=23&t=96s&ab_channel=PatrickLoeber
# 17:52 DEMO

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

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)