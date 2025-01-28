"""add content column to posts table

Revision ID: 344a663369c1
Revises: ec3d53033f99
Create Date: 2025-01-25 19:29:20.056436

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '344a663369c1'
down_revision: Union[str, None] = 'ec3d53033f99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', sa.Column('content'))
