from app.models import db, IngredientList


def seed_ingredient_list():
    chicken = IngredientList(
        id=1,
        ingredient_name='Chicken'
    )
    potato = IngredientList(
        id=2,
        ingredient_name='Potato'
    )
    lettuce = IngredientList(
        id=3,
        ingredient_name='Lettuce'
    )
    tomato = IngredientList(
        id=4,
        ingredient_name='Tomato'
    )
    salt = IngredientList(
        id=5,
        ingredient_name='Salt'
    )
    hotdog = IngredientList(
        id=6,
        ingredient_name='HotDog'
    )

    db.session.add(chicken)
    db.session.add(potato)
    db.session.add(lettuce)
    db.session.add(tomato)
    db.session.add(salt)
    db.session.add(hotdog)

    db.session.commit()


def undo_ingredient_list():
    db.session.execute(
        'TRUNCATE ingredient_lists RESTART IDENTITY CASCADE;')
    db.session.commit()
