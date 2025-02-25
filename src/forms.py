from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo,Length,ValidationError
from src.models import User

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_name = original_username


    def validate_username(self, username):
        '''
        在 Flask - WTF 中，validate_<field_name> 格式的方法（如 validate_username）是自定义验证器方法，它们会在表单提交并进行验证时被自动调用。
        '''
        if self.original_name != username.data:
            user = User.query.filter_by(username = self.username.data).first()
            if user is not None:
                raise ValidationError("Please use a adifferent name")


class PostForm(FlaskForm):
    '''
    用户动态表单
    '''
    post = TextAreaField('Say something', validators=[DataRequired(),Length(min=1,max=140)])
    submit = SubmitField('Submit')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')