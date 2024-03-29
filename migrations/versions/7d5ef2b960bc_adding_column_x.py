"""Adding column x.

Revision ID: 7d5ef2b960bc
Revises: 4496c7c486be
Create Date: 2024-02-22 10:37:45.838367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d5ef2b960bc'
down_revision = '4496c7c486be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('ix_user_age')
        batch_op.drop_index('ix_user_email')
        batch_op.drop_index('ix_user_username')

    op.drop_table('user')
    with op.batch_alter_table('k8s_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('posted', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('k8s_info', schema=None) as batch_op:
        batch_op.drop_column('posted')

    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=64), nullable=True),
    sa.Column('address', sa.VARCHAR(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('ix_user_username', ['username'], unique=False)
        batch_op.create_index('ix_user_email', ['email'], unique=False)
        batch_op.create_index('ix_user_age', ['age'], unique=False)

    # ### end Alembic commands ###
