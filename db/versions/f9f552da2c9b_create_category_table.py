"""create category table

Revision ID: f9f552da2c9b
Revises: 1fbc85ca7268
Create Date: 2021-07-12 02:57:10.558528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9f552da2c9b'
down_revision = '1fbc85ca7268'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'category',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column(
            'group_id',
            sa.String(36),
            sa.ForeignKey('group.id'),
            nullable=False
        ),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('index', sa.SMALLINT(), nullable=False),
        sa.Column(
            'disabled',
            sa.BOOLEAN,
            server_default="0",
            nullable=False
        ),
    )


def downgrade():
    op.drop_table('category')
