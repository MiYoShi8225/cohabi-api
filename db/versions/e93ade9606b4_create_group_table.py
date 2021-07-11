"""create group table

Revision ID: e93ade9606b4
Revises: 568731159647
Create Date: 2021-07-12 02:48:56.968049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e93ade9606b4'
down_revision = '568731159647'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'group',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table('group')
