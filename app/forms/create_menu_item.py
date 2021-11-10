from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired
from app.models import MenuItem


class CreateMenuItem(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    item_cost = IntegerField('Item Cost', validators=[DataRequired()])
    item_price = IntegerField('Item Price', validators=[DataRequired()])
    menu_category_id = SelectField('Category Id', choices=[
        1, 2, 3, 4, 5, 6, 7, 8, 9], validators=[DataRequired()])
    menu_item_ingredients_id = IntegerField(
        'Item Ingredient Id', validators=[DataRequired()])
