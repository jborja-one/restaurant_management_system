from app.models import db, MenuItemIngredients


def seed_menu_item_ingredients():
    chicken = MenuItemIngredients(
        id=1,
        ingredient_name='Chicken',
        ingredient_unit=10,
        ingredient_qty=1,
        menu_item_id=1,
    )
    potatoes = MenuItemIngredients(
        id=2,
        ingredient_name='Potato',
        ingredient_unit=6,
        ingredient_qty=1.5,
        menu_item_id=1,
    )
    lettuce = MenuItemIngredients(
        id=3,
        ingredient_name='Lettuce',
        ingredient_unit=1,
        ingredient_qty=10,
        menu_item_id=1,
    )
    tomato = MenuItemIngredients(
        id=4,
        ingredient_name='Tomato',
        ingredient_unit=10,
        ingredient_qty=0.5,
        menu_item_id=1,
    )
    salt = MenuItemIngredients(
        id=5,
        ingredient_name='Salt',
        ingredient_unit=4,
        ingredient_qty=1.5,
        menu_item_id=1,
    )
    potatoes = MenuItemIngredients(
        id=6,
        ingredient_name='Potato',
        ingredient_unit=6,
        ingredient_qty=2,
        menu_item_id=2,
    )
    hotdog = MenuItemIngredients(
        id=7,
        ingredient_name='Hot Dog',
        ingredient_unit=10,
        ingredient_qty=2,
        menu_item_id=2,
    )

    db.session.add(chicken)
    db.session.add(potatoes)
    db.session.add(lettuce)
    db.session.add(tomato)
    db.session.add(salt)
    db.session.add(potatoes)
    db.session.add(hotdog)

    db.session.commit()


def undo_menu_item_ingredients():
    db.session.execute(
        'TRUNCATE menu_item_ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
