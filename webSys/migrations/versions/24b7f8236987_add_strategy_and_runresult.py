"""add strategy and RunResult

Revision ID: 24b7f8236987
Revises: 03031080b2db
Create Date: 2017-05-16 11:02:12.467425

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '24b7f8236987'
down_revision = '03031080b2db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('groups')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('title', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('about', mysql.TEXT(), nullable=False),
    sa.Column('logo', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('topic_num', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('created_time', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
