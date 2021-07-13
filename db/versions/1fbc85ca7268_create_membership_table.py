"""create membership table

Revision ID: 1fbc85ca7268
Revises: e93ade9606b4
Create Date: 2021-07-12 02:51:35.104765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fbc85ca7268'
down_revision = 'e93ade9606b4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'membership',
        sa.Column(
            'group_id',
            sa.String(36),
            sa.ForeignKey('group.id'),
            primary_key=True
        ),
        sa.Column(
            'user_id',
            sa.String(255),
            sa.ForeignKey('user.id'),
            primary_key=True
        ),
    )


def downgrade():
    op.drop_table('membership')
