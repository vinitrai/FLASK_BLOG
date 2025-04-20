from flask_wtf import FlaskForm
from wtforms.fields import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired
# creating a new post form
class PostForm(FlaskForm):
    title = StringField('title',validators=[DataRequired()])
    content = TextAreaField('content',validators=[DataRequired()])
    submit = SubmitField('Post')