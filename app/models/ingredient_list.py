# from .db import db


# class IngredientList(db.Model):
#     __tablename__ = 'ingredient_lists'

#     id = db.Column(db.Integer, primary_key=True)
#     ingredient_name = db.Column(db.String(100), nullable=False)

#     # todo Associations here
#     ingredient_list = db.relationship(
#         'MenuItemIngredients', back_populates='ind_ingredient')

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'ingredient_name': self.ingredient_name
#         }
