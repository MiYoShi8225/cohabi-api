"""update categoly disable column

Revision ID: 2f69111f0fea
Revises: f9f552da2c9b
Create Date: 2021-07-18 22:48:43.703958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f69111f0fea'
down_revision = 'f9f552da2c9b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('category',
                  sa.Column('status', sa.String(length=36), nullable=False))
    op.drop_column('category', 'disabled')
    pass


def downgrade():
    op.add_column('category',
                  sa.Column(
                      'disabled',
                      sa.BOOLEAN,
                      server_default="0",
                      nullable=False
                  ))
    op.drop_column('category', 'status')
    pass
