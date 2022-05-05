from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, regexp, length

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "bbq-Carl"

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), regexp("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")])
    password = PasswordField(label='Password', validators=[DataRequired(), length(min=8)])
    submit = SubmitField(label='Log In')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "pie@piemaster.com" and login_form.password.data == app.secret_key:
            print(login_form.email.data)
            print(login_form.password.data)
            return render_template('success.html')
        else: 
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)