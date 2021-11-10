from app.models import db, MenuItem


def seed_menu_items():
    pollo_a_la_brasa = MenuItem(
        id=1,
        item_name='Pollo a la Brasa',
        item_cost=10,
        item_price=19,
        menu_category_id=2,
        menu_item_ingredients_id=1
    )
    salchipapa = MenuItem(
        id=2,
        item_name='Salchipapa',
        item_cost=4,
        item_price=10,
        menu_category_id=1,
        menu_item_ingredients_id=2
    )

    db.session.add(pollo_a_la_brasa)
    db.session.add(salchipapa)

    db.session.commit()


def undo_menu_items():
    db.session.execute('TRUNCATE menu_items RESTART IDENTITY CASCADE;')
    db.session.commit()
