from .db import db


class MenuCategory(db.Model):
    __tablename__ = 'menu_categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)
    # menu_item_id = db.Column(db.Integer, nullable=False)

    # todo Associations Here
    menu_item = db.relationship('MenuItem', back_populates='menu_category')

    def to_dict(self):
        return {
            'id': self.id,
            'category_name': self.category_name,
            # 'menu_item_id': self.menu_item_id
        }
