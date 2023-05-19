from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL
from wtforms.validators import DataRequired

class URLForm(FlaskForm):
    url = StringField("Ссылка", validators=[
        DataRequired(message='Поле "Ссылка" не может быть пустым'), URL(message="Ссылка написана не верно")
    ])
    submit = SubmitField("Сократить")