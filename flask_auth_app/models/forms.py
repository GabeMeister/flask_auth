""" Define the views """

# pylint: disable=C0103,C0111

from flask_auth_app.models.user import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from werkzeug.security import check_password_hash


class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[
        InputRequired(message='Please enter a unique username'),
        Length(min=4, max=15, message='Username must be between 4 and 15 characters long')
    ])
    password = PasswordField('Password:', validators=[
        InputRequired(message='Please enter a password'),
        Length(min=8, max=80, message='Password must be between 8 and 80 characters long')
    ])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')

    def validate(self):
        print 'got here'
        valid = FlaskForm.validate(self)
        if not valid:
            return False

        # make sure username exists in database
        user = User.query.filter_by(username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unrecognized username. Please try again')
            return False

        # make sure password matches
        if not check_password_hash(user.password, self.password.data):
            self.password.errors.append('Password incorrect. Please try again')
            return False

        return True


class RegisterForm(FlaskForm):
    email = StringField('Email:', validators=[
        InputRequired(message='Please enter a valid email'),
        Email(message='Enter a valid email')
    ])
    username = StringField('Username:', validators=[
        InputRequired(message='Please enter a unique username'),
        Length(min=4, max=15, message='Username must be between 4 and 15 characters long')
    ])
    password = PasswordField('Password:', validators=[
        InputRequired(message='Please enter a password'),
        Length(min=8, max=80, message='Password must be between 8 and 80 characters long')
    ])
    confirm_password = PasswordField('Confirm Password:', validators=[
        InputRequired('Please confirm password'),
        Length(min=8, max=80),
        EqualTo(fieldname='password', message='Passwords must match')
    ])
    submit = SubmitField('Submit')
