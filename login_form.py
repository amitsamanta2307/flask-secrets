from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[
                            DataRequired(message="Email is required"),
                            Email(message="That's not a valid email address.")
                        ])
    password = PasswordField(label='Password',
                             validators=[
                                 DataRequired(message="Password is required"),
                                 Length(message="Password should be minimum 8 characters long", min=8)
                             ])
    submit = SubmitField(label="Log In")
