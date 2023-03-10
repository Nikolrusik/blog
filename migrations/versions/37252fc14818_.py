"""empty message

Revision ID: 37252fc14818
Revises: 
Create Date: 2023-02-06 22:40:17.710155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37252fc14818'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=120), server_default='', nullable=False),
    sa.Column('last_name', sa.String(length=120), server_default='', nullable=False),
    sa.Column('username', sa.String(length=0), nullable=True),
    sa.Column('email', sa.String(length=255), server_default='', nullable=False),
    sa.Column('is_staff', sa.Boolean(), nullable=False),
    sa.Column('_password', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_author_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_author'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('author')
    op.drop_table('user')
    # ### end Alembic commands ###
