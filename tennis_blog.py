from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blog_for_tennis_players'
posts = [
    {
        'author': 'Rafa Nadal',
        'title': 'One More Injury',
        'content': 'Retired from Indian Wells and Miami tournaments. Sadness :(',
        'date_posted': 'March 1, 2019'
    },
    {
        'author': 'Maria Sharapova',
        'title': 'My First Disqualification',
        'content': 'Never again meldonium',
        'date_posted': 'March 3, 2019'
    }]


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


@app.route("/")
@app.route("/home")
def home():
    return render_template('home_page.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about_page.html', title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
