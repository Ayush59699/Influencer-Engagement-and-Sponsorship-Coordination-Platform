from flask import Flask, request
from flask import redirect, render_template, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(FlaskForm):
    name=StringField('Your Name?', validators=[DataRequired()])
    submit=SubmitField('Submit')


@app.route('/hello', methods=['GET','POST']) # session helps remember data even after refresh and request
def hello():
    form=NameForm()
    if form.validate_on_submit():
        session['name']=form.name.data
        return redirect(url_for('hello')) #hello is functn name
    form.name=data=''
    return render_template('hello.html', form=form, name=session.get('name'))


@app.route('/', methods=['GET', 'POST'])
def index():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
    return render_template('index.html', form=form, name=name)


@app.route('/user')
def user():
    name="ayush"
    return render_template('user.html',name=name)









if(__name__=='__main__'): 
    app.run(debug=True)
