"""First migration

Revision ID: ef44555654
Revises: None
Create Date: 2016-01-15 00:16:22.161396

"""

# revision identifiers, used by Alembic.
revision = 'ef44555654'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('words',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=64), nullable=True),
    sa.Column('meaning', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('word')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('words')
    ### end Alembic commands ###