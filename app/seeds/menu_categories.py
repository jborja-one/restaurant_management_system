from app.models import db, MenuCategory


def seed_menu_categories():
    appetizer = MenuCategory(
        id=1,
        category_name='Appetizer'
    )
    entree = MenuCategory(
        id=2,
        category_name='Entree'
    )
    dessert = MenuCategory(
        id=3,
        category_name='Dessert'
    )
    sandwich = MenuCategory(
        id=4,
        category_name='Sandwich'
    )
    side = MenuCategory(
        id=5,
        category_name='Side'
    )
    sauce = MenuCategory(
        id=6,
        category_name='Sauce'
    )
    salsa = MenuCategory(
        id=7,
        category_name='Salsa'
    )
    soda = MenuCategory(
        id=8,
        category_name='Soda'
    )
    drink = MenuCategory(
        id=9,
        category_name='Drink'
    )

    db.session.add(appetizer)
    db.session.add(entree)
    db.session.add(dessert)
    db.session.add(sandwich)
    db.session.add(side)
    db.session.add(sauce)
    db.session.add(salsa)
    db.session.add(soda)
    db.session.add(drink)

    db.session.commit()


def undo_menu_categories():
    db.session.execute(
        'TRUNCATE menu_categories RESTART IDENTITY CASCADE;')
    db.session.commit()
