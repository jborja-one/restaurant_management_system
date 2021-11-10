from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired
from app.models import MenuCategory


class CreateMenuCategory(FlaskForm):
    category_name: StringField('Category Name', validators=[DataRequired()])
    menu_item_id: IntegerField('Menu Item Id', validators=[DataRequired()])
