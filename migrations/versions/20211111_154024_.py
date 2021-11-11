"""empty message

Revision ID: b9b66e87cab7
Revises: ffdc0a98111c
Create Date: 2021-11-11 15:40:24.191010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9b66e87cab7'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient_units',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unit_name', sa.String(length=5), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu_item_ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ingredient_name', sa.String(length=100), nullable=False),
    sa.Column('ingredient_unit', sa.Integer(), nullable=False),
    sa.Column('ingredient_qty', sa.Integer(), nullable=False),
    sa.Column('menu_item_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_unit'], ['ingredient_units.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(length=100), nullable=False),
    sa.Column('item_cost', sa.Integer(), nullable=False),
    sa.Column('item_price', sa.Integer(), nullable=False),
    sa.Column('menu_category_id', sa.Integer(), nullable=False),
    sa.Column('menu_item_ingredients_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['menu_category_id'], ['menu_categories.id'], ),
    sa.ForeignKeyConstraint(['menu_item_ingredients_id'], ['menu_item_ingredients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu_items')
    op.drop_table('menu_item_ingredients')
    op.drop_table('menu_categories')
    op.drop_table('ingredient_units')
    # ### end Alembic commands ###