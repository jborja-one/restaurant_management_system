from .db import db


class MenuItemIngredients(db.Model):
    __tablename__ = 'menu_item_ingredients'

    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(100), nullable=False)
    ingredient_unit = db.Column(db.Integer, db.ForeignKey(
        'ingredient_units.id'), nullable=False)
    ingredient_qty = db.Column(db.Integer, nullable=False)
    menu_item_id = db.Column(db.Integer, nullable=False)

    # todo Associations here
    menu_item = db.relationship(
        'MenuItem', back_populates='item_ingredients')
    ingredient_unit_id = db.relationship(
        'IngredientUnit', back_populates='ingredient_unit')

    def to_dict(self):
        return {
            'id': self.id,
            'ingredient_name': self.ingredient_name,
            'ingredient_unit': self.ingredient_unit,
            'ingredient_qty': self.ingredient_qty,
            'menu_item_id': self.menu_item_id
        }
