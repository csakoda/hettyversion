"""empty message

Revision ID: 84af03853905
Revises: 
Create Date: 2017-01-04 17:47:21.304137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84af03853905'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('desc', sa.String(length=128), nullable=True),
    sa.Column('bandid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song')
    # ### end Alembic commands ###