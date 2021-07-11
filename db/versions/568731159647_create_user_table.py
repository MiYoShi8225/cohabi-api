"""create user table

Revision ID: 568731159647
Revises: 
Create Date: 2021-07-12 02:14:28.555245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '568731159647'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('idp_id', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('icon', sa.String(255)),
    )


def downgrade():
    op.drop_table('user')
