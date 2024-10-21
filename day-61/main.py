from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import email_validator
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "Meet_Pravinbhai_Thummar"
bootstrap = Bootstrap5(app)


class MyForm(FlaskForm):
    """Class to serve login form"""
    # email = Field('email', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Invalid Email Entered."), Length(0, 30, "Invalid length of Input")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(8, 30, "Invalid length of Input")])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html', form=MyForm())


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    form = MyForm()
    print(form.email.data)
    print(form.password.data)
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('/success.html')
    return render_template('/denied.html')


if __name__ == '__main__':
    app.run(debug=True)
