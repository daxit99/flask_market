from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import length,EqualTo,Email,DataRequired,ValidationError
from market.model import User  

class RegisterForm(FlaskForm):
    def valiadate_Username(self,Username_to_check):
        user=User.query.filter_by(Username=Username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! please try a diffrent Username')

    def validate_email_address(self,email_address_to_check):
        email_address=User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exists! please try diffrent email address')

    Username =StringField(label="User Name:",validators=[length(min=2,max=30),DataRequired()])
    email_address=StringField(label="Email Address:",validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Password:',validators=[length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Create Account')
