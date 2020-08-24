"""empty message

Revision ID: eaf9832552bd
Revises: 45b02a969736
Create Date: 2020-08-24 18:52:23.182711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eaf9832552bd'
down_revision = '45b02a969736'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('NY', sa.Column('sex', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('NY', 'sex')
    # ### end Alembic commands ###