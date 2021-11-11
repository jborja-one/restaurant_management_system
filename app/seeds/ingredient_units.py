from app.models import db, IngredientUnit


def seed_ingredient_units():
    gram = IngredientUnit(
        id=1,
        unit_name='gram'
    )
    ounce = IngredientUnit(
        id=2,
        unit_name='oz'
    )
    cup = IngredientUnit(
        id=3,
        unit_name='cup'
    )
    small_table_spoon = IngredientUnit(
        id=4,
        unit_name='tsp'
    )
    big_table_spoon = IngredientUnit(
        id=5,
        unit_name='Tbsp'
    )
    pound = IngredientUnit(
        id=6,
        unit_name='lbs'
    )
    milliliter = IngredientUnit(
        id=7,
        unit_name='ml'
    )
    litre = IngredientUnit(
        id=8,
        unit_name='ltr'
    )
    gallon = IngredientUnit(
        id=9,
        unit_name='gal'
    )
    unit = IngredientUnit(
        id=10,
        unit_name='unit'
    )

    db.session.add(gram)
    db.session.add(ounce)
    db.session.add(cup)
    db.session.add(small_table_spoon)
    db.session.add(big_table_spoon)
    db.session.add(pound)
    db.session.add(milliliter)
    db.session.add(litre)
    db.session.add(gallon)
    db.session.add(unit)

    db.session.commit()


def undo_ingredient_units():
    db.session.execute('TRUNCATE ingredient_units RESTART IDENTITY CASCADE;')
    db.session.commit()
