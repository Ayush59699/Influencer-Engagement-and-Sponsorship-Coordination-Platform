from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy import select
import os
#from sqlalchemy.orm import session, declarative_base, relationship
currdir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(currdir, 'data.dalite')
db=SQLAlchemy()
db.init_app(app)
app.app_context().push()









if __name__=='__main__':
    app.run(debug=True)





















