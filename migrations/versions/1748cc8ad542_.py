"""empty message

Revision ID: 1748cc8ad542
Revises: 8231374f2231
Create Date: 2023-12-18 16:46:16.121765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1748cc8ad542'
down_revision = '8231374f2231'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
