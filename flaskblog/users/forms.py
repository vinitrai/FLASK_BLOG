from flask_wtf import FlaskForm 
from wtforms.fields import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,Length,EqualTo,ValidationError
from flask_wtf.file import FileField, FileRequired,FileAllowed
from flaskblog.models import User 
from flask_login import current_user

# new user registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('That username exists already,please choose a different one!')
    
    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('The email exists already! Plz choose a different one')

# user login form
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
# user account update form
class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    
    submit = SubmitField('Update')

    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('That username exists already,please choose a different one!')
    
    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('The email exists already! Plz choose a different one')


# reset password request form
class RequestResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Request Password Reset')
    def validate_email(self,email):
       user = User.query.filter_by(email = email.data).first()
       if user is None:
           raise ValidationError('There is no account with that email.You must register first!')
       
# password reset form
class ResetPasswordForm(FlaskForm):
    password = StringField('password',validators=[DataRequired()])
    confirm_password = StringField('confirm password',validators=[DataRequired()])
    submit = SubmitField('Reset Password')
    