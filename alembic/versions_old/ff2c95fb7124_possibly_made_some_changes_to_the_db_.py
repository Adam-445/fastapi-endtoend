"""Possibly made some changes to the db without noticing

Revision ID: ff2c95fb7124
Revises: a4640965504e
Create Date: 2025-01-28 10:48:23.281375

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff2c95fb7124'
down_revision: Union[str, None] = 'a4640965504e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('published', sa.Boolean(), server_default='true', nullable=False))
    op.drop_column('posts', 'pusblished')
    op.create_foreign_key(None, 'votes', 'posts', ['post_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'votes', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'votes', type_='foreignkey')
    op.drop_constraint(None, 'votes', type_='foreignkey')
    op.add_column('posts', sa.Column('pusblished', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False))
    op.drop_column('posts', 'published')
    # ### end Alembic commands ###
