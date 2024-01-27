"""change attr species

Revision ID: 07a9227ea34b
Revises: f88ce0386196
Create Date: 2024-01-27 00:28:07.175899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07a9227ea34b'
down_revision: Union[str, None] = 'f88ce0386196'
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
    sa.Column('species', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='iris_pkey')
    )
    # ### end Alembic commands ###
