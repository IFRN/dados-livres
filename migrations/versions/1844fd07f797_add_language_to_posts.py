"""add language to posts

Revision ID: 1844fd07f797
Revises: 3251458bf6f0
Create Date: 2020-03-24 00:57:22.367666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1844fd07f797'
down_revision = '3251458bf6f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'language')
    # ### end Alembic commands ###