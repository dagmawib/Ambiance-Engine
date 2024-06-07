from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=5, max=30)])
    password = PasswordField(validators=[InputRequired(), Length(min=5, max=20)])
    country = StringField(validators=[InputRequired(), Length(min=5, max=50)])
    Fname = StringField(validators=[InputRequired(), Length(min=5, max=50)])
    submit = SubmitField("Login")

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=5 , max=30)])
    password= PasswordField(validators=[InputRequired(), Length(min=5 , max=20)])
    submit = SubmitField("Sign Up")
    