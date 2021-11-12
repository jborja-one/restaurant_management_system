from flask.cli import AppGroup
from .users import seed_users, undo_users
from .menu_item import seed_menu_items, undo_menu_items
from .menu_categories import seed_menu_categories, undo_menu_categories
from .ingredient_units import seed_ingredient_units, undo_ingredient_units
from .menu_item_ingredients import seed_menu_item_ingredients, undo_menu_item_ingredients
from .ingredient_list import seed_ingredient_list, undo_ingredient_list


# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_ingredient_list()
    seed_users()
    seed_menu_categories()
    seed_ingredient_units()
    seed_menu_item_ingredients()
    seed_menu_items()

    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_ingredient_list()
    undo_users()
    undo_menu_categories()
    undo_ingredient_units()
    undo_menu_item_ingredients()
    undo_menu_items()

    # Add other undo functions here
