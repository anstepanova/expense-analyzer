"""Added user table.

Revision ID: 53312486e3d3
Revises:
Create Date: 2023-11-20 17:32:32.193193
"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '53312486e3d3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'user',
        sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('created_at', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('updated_at', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='id'),
    )
    # ### end Alembic commands ###