from flask_sqlalchemy import SQLAlchemy, model
from flask import Flask, render_template, request
from sqlalchemy.orm import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy import select
import os
from flask_sqlalchemy import session
#from sqlalchemy.orm import session, declarative_base, relationship
currdir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(currdir, 'data.sqlite3')
db=SQLAlchemy()
db.init_app(app)
app.app_context().push()


class User(db.Model):
    __tablename__='user'
    user_id=db.Column(db.Integer, autoIncrement=True)
    username=db.Column(db.String, unique=True)
    email=db.Column(db.String, unique=True)

@app.route('/', methods=['GET','POST'])
def home():
    users=User.query.all()
    for i in users:
        print(i)
    return render_template('home.html')









if __name__=='__main__':
    app.run(debug=True)





















