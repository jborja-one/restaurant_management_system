from flask import Blueprint, redirect, request, session
from app.models.menu_item import MenuItem
from app.models import db

menu_routes = Blueprint('menu_items', __name__)


@menu_routes.route('/')
def get_menu_items():
    menu_items = MenuItem.query.all()
    new_dict = {'item': {}, 'category': {}, 'ingredients': {}}
    for item in menu_items:
        new_dict['item'] = item.to_dict()
        new_dict['category'][item.menu_category_id] = item.to_dict()
        new_dict['ingredients'][item.menu_item_ingredients_id] = item.to_dict()
    # import pdb
    # pdb.set_trace()
    # print(menu_items, '*********************')
    return new_dict
