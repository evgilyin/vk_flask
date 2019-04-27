from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class GroupForm(FlaskForm):
    vk_group = StringField('Введите ссылку на сообщество в формате https://vk.com...', render_kw={"class": "form-control"})
    # submit = SubmitField('Проверить', render_kw={"class": "btn btn-primary"}, onclick="$('#loading').show();")
