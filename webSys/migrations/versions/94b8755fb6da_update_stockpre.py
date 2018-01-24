"""update stockPre

Revision ID: 94b8755fb6da
Revises: 6220275ca17d
Create Date: 2017-04-28 16:41:33.299187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94b8755fb6da'
down_revision = '6220275ca17d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('predicts', sa.Column('date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('predicts', 'date')
    # ### end Alembic commands ###
