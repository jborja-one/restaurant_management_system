from .db import db


class IngredientUnit(db.Model):
    __tablename__ = 'ingredient_units'

    id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String(5), nullable=False)

    # todo Associations here
    ingredient_unit = db.relationship(
        'MenuItemIngredients', back_populates='ingredient_unit_id')

    def to_dict(self):
        return {
            'id': self.id,
            'unit_name': self.unit_name
        }
