from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired


class CreateMenuItemIngredients(FlaskForm):
    ingredient_name = StringField(
        'Ingredient Name', validators=[DataRequired()])
    ingredient_unit = SelectField('Ingredient Unit', choices=[
                                  1, 2, 3, 4, 5, 6, 7, 8, 9, 10], validators=[DataRequired()])
    ingredient_qty = IntegerField(
        'Ingredient Quality', validators=[DataRequired()])
    menu_item_id = IntegerField('Menu Item ID', validators=[DataRequired()])
