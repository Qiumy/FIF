"""change topic model

Revision ID: b3a4d9afc884
Revises: 24b7f8236987
Create Date: 2017-05-16 16:20:12.835051

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b3a4d9afc884'
down_revision = '24b7f8236987'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topics', sa.Column('cat_type', sa.Integer(), nullable=True))
    op.drop_constraint('topics_ibfk_3', 'topics', type_='foreignkey')
    op.create_foreign_key(None, 'topics', 'category', ['cat_type'], ['id'])
    op.drop_column('topics', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topics', sa.Column('type', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'topics', type_='foreignkey')
    op.create_foreign_key('topics_ibfk_3', 'topics', 'category', ['type'], ['id'])
    op.drop_column('topics', 'cat_type')
    # ### end Alembic commands ###