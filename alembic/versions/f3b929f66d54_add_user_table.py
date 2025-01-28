"""add user table

Revision ID: f3b929f66d54
Revises: 344a663369c1
Create Date: 2025-01-25 19:33:34.158191

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f3b929f66d54"
down_revision: Union[str, None] = "344a663369c1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.Integer(), nullable=False),
        sa.Column("password", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )

def downgrade() -> None:
    op.drop_table('users')