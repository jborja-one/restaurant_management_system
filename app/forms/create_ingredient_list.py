from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired


class CreateIngredientList(FlaskForm):
    ingredient_name = db.Column(
        db.String(60), nullable=False, validators=[DataRequired()])
