from .db import db


class MenuItem(db.Model):
    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    item_cost = db.Column(db.Integer, nullable=False)
    item_price = db.Column(db.Integer, nullable=False)
    menu_category_id = db.Column(db.Integer, db.ForeignKey(
        'menu_categories.id'), nullable=False)
    menu_item_ingredients_id = db.Column(db.Integer, db.ForeignKey(
        'menu_item_ingredients.id'), nullable=False)

    # todo Associations here
    menu_category = db.relationship(
        'MenuCategory', back_populates='menu_item')
    item_ingredients = db.relationship(
        'MenuItemIngredients', back_populates='menu_item')

    def to_dict(self):
        return {
            'id': self.id,
            'item_name': self.item_name,
            'item_cost': self.item_cost,
            'item_price': self.item_price,
            'menu_category_id': self.menu_category_id,
            'menu_item_ingredients_id': self.menu_item_ingredients_id
        }
