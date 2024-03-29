"""init

Revision ID: ff146b50ed12
Revises: 466313f539b9
Create Date: 2024-01-24 23:43:43.420313

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff146b50ed12'
down_revision: Union[str, None] = '466313f539b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('iris')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('iris',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('sepal_length', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('petal_length', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('sepal_width', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('petal_width', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('species', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='iris_pkey')
    )
    # ### end Alembic commands ###
