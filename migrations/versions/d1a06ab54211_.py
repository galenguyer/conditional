"""Add Accept Dues Until site setting

Revision ID: d1a06ab54211
Revises: 117567def844
Create Date: 2017-07-21 17:09:37.540766

"""

# revision identifiers, used by Alembic.
revision = 'd1a06ab54211'
down_revision = '117567def844'

from alembic import op
import sqlalchemy as sa
from datetime import datetime

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('accept_dues_until', sa.Date(), server_default=datetime.now().strftime("%Y-%m-%d"), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('settings', 'accept_dues_until')
    # ### end Alembic commands ###
