"""relacionamentos user e source

Revision ID: 7e0e3fef043b
Revises: 7ebe0b20b76d
Create Date: 2019-11-11 00:33:41.872715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e0e3fef043b'
down_revision = '7ebe0b20b76d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'source', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'source', type_='foreignkey')
    # ### end Alembic commands ###
