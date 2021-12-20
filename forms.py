from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class todo(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
    print()
    print()
    task = StringField('task',validators=[DataRequired()])
    submit = SubmitField('submit')
# class delete(FlaskForm):
#     username = StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
#     task = StringField('task',validators=[DataRequired()])