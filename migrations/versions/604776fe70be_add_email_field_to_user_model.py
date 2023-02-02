"""Add email field to user model



Revision ID: 604776fe70be
Revises: 
Create Date: 2023-02-02 03:05:04.346937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '604776fe70be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=255), server_default='', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###
