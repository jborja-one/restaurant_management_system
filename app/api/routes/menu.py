from flask import Blueprint, redirect, request, session
from app.models.menu_item import MenuItem
from app.models.menu_category import MenuCategory
from app.models.menu_item_ingredients import MenuItemIngredients
from app.models import db

menu_routes = Blueprint('menu_items', __name__)


@menu_routes.route('/')
def get_menu_items():
    menu_query = MenuItem.query.all()
    menu_items = [menu_item.to_dict() for menu_item in menu_query]
    for item in menu_items:
        # item['item'] = MenuItem.query.all()
        item['category'] = MenuCategory.query.get(
            item['menu_category_id']).to_dict()
        item['ingredients'] = MenuItemIngredients.query.get(
            item['menu_item_ingredients_id']).to_dict()
        return {'menu_items': menu_items}
